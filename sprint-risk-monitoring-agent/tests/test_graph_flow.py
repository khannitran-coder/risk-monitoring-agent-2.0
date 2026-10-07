from datetime import date

import pytest

from sprint_risk_agent.audit import AuditLog
from sprint_risk_agent.config import Settings
from sprint_risk_agent.graph import build_graph
from sprint_risk_agent.mcp_clients.fake import FakeGitHub, FakeJira, FakeSlack, demo_clients
from sprint_risk_agent.nodes.draft import TemplateDrafter
from sprint_risk_agent.runner import pending_interrupt, resume_run, start_run
from sprint_risk_agent.schemas import RiskResponseOption, RiskResponsePlan

AS_OF = "2026-10-07"


def medium_clients():
    """Chỉ PAY-102 có 2 nguồn -> MEDIUM -> nhánh digest."""
    c = demo_clients(date.fromisoformat(AS_OF))
    c.slack.messages = []
    c.github.prs = [p for p in c.github.prs if p["title"].startswith("PAY-102")]
    c.jira.tickets = [t for t in c.jira.tickets if t["ticket_id"] == "PAY-102"]
    return c


def run(graph, sprint="SPRINT-42"):
    return start_run(graph, sprint, as_of=AS_OF)


# ---------- nhánh HIGH/CRITICAL ----------

def test_high_path_waits_for_human_and_sends_nothing(graph, clients):
    _, result = run(graph)
    payload = pending_interrupt(result)
    assert payload["risk_level"] == "CRITICAL"
    assert payload["grounding_warnings"] == []          # luôn có key, kể cả rỗng
    assert payload["action_plan"] is not None
    assert clients.slack.sent == [] and clients.jira.create_calls == 0


def test_high_path_approve_escalates_once(graph, clients, audit):
    tid, _ = run(graph)
    final = resume_run(graph, tid, "approve")
    assert final["status"] == "COMPLETED"
    assert final["jira_issue_ids"] == {"PAY-101": "RISK-1"}
    assert [ch for ch, _ in clients.slack.sent] == ["#leadership-escalation"]
    assert "RISK-1" in clients.slack.sent[0][1]
    end = audit.records()[-1]
    assert end["event"] == "run_end" and end["status"] == "COMPLETED" and end["decision"] == "approve"


def test_jira_creation_is_idempotent_across_runs(clients, audit):
    g = build_graph(clients, audit=audit)
    for _ in range(2):
        tid, _ = run(g)
        resume_run(g, tid, "approve")
    assert clients.jira.create_calls == 1 and len(clients.jira.issues) == 1


# ---------- nhánh LOW/MEDIUM ----------

def test_digest_path_sends_to_team_only_after_approve():
    c = medium_clients()
    g = build_graph(c)
    tid, result = run(g)
    assert pending_interrupt(result)["risk_level"] == "MEDIUM"
    assert c.slack.sent == []
    assert resume_run(g, tid, "approve")["status"] == "COMPLETED"
    assert [ch for ch, _ in c.slack.sent] == ["#team-sprint"] and c.jira.create_calls == 0


# ---------- checkpoint: edit / reject / giới hạn ----------

def test_edit_loops_back_to_drafting_with_notes():
    seen = []

    class Spy(TemplateDrafter):
        def digest(self, state):
            seen.append(state.get("checkpoint_notes"))
            return super().digest(state)

    c = medium_clients()
    g = build_graph(c, drafter=Spy())
    tid, _ = run(g)
    result = resume_run(g, tid, "edit", "thêm PAY-102 nhé, mật khẩu: abc123")
    payload = pending_interrupt(result)
    assert payload["revision_count"] == 1 and c.slack.sent == []
    assert seen[0] is None and "abc123" not in seen[1]       # ghi chú PM cũng được redact
    assert resume_run(g, tid, "approve")["status"] == "COMPLETED"


def test_reject_stops_without_sending(graph, clients, audit):
    tid, _ = run(graph)
    final = resume_run(graph, tid, "reject")
    assert final["status"] == "REJECTED"
    assert clients.slack.sent == [] and clients.jira.create_calls == 0
    assert audit.records()[-1]["status"] == "REJECTED"


@pytest.mark.parametrize("bad", ["yes", "", None, "APPROVE "])
def test_invalid_decision_fails_safe(graph, clients, bad):
    tid, _ = run(graph)
    final = resume_run(graph, tid, bad)
    assert final["status"] == "REJECTED" and clients.slack.sent == []


def test_revision_cap_aborts_instead_of_looping_forever(clients, audit):
    g = build_graph(clients, audit=audit, settings=Settings(max_revisions=2))
    tid, _ = run(g)
    assert pending_interrupt(resume_run(g, tid, "edit", "1"))["revision_count"] == 1
    assert pending_interrupt(resume_run(g, tid, "edit", "2"))["revision_count"] == 2
    final = resume_run(g, tid, "edit", "3")
    assert final["status"] == "ABORTED_MAX_REVISIONS" and clients.slack.sent == []


# ---------- guardrail trong luồng ----------

def test_secrets_never_enter_state_or_draft(graph):
    tid, result = run(graph)
    state = graph.get_state({"configurable": {"thread_id": tid}}).values
    blob = str(state)
    assert "sk_live_ABC123" not in blob and "[REDACTED_SECRET]" in blob


def test_fabricated_ticket_is_flagged_in_checkpoint_payload():
    class Liar(TemplateDrafter):
        def action_plan(self, state):
            refs = ["PAY-101", "PAY-999"]
            return RiskResponsePlan(root_cause="x", options=[
                RiskResponseOption(strategy="mitigate", description="a", evidence_refs=refs, tradeoff="t"),
                RiskResponseOption(strategy="accept", description="b", evidence_refs=["PAY-101"], tradeoff="t"),
            ])

    g = build_graph(demo_clients(date.fromisoformat(AS_OF)), drafter=Liar())
    _, result = run(g)
    assert pending_interrupt(result)["grounding_warnings"] == ["PAY-999"]


def test_source_failure_degrades_instead_of_crashing():
    c = demo_clients(date.fromisoformat(AS_OF))
    c.slack.fail = True
    g = build_graph(c)
    _, result = run(g)
    payload = pending_interrupt(result)
    assert payload["fetch_errors"] == ["slack: ConnectionError"]
    assert payload["draft_text"].startswith("⚠ Dữ liệu không đầy đủ")
    assert payload["risk_level"] == "MEDIUM"   # mất slack => PAY-101 chỉ còn 2 nguồn


# ---------- circuit breaker ----------

def test_circuit_breaker_trips_after_two_runs_with_warnings_then_resets():
    class Liar(TemplateDrafter):
        def digest(self, state):
            return super().digest(state) + "\nPAY-999 cũng trễ"

    audit = AuditLog()
    c = medium_clients()
    g = build_graph(c, drafter=Liar(), audit=audit)
    for _ in range(2):
        tid, _ = run(g)
        resume_run(g, tid, "reject")                      # kết thúc lượt, có warning
    _, result = run(g)                                    # lượt 3: breaker bật
    assert pending_interrupt(result) is None and result["status"] == "MANUAL_MODE"
    assert c.slack.sent == []
    _, result = run(g)                                    # vẫn bật cho tới khi PM reset
    assert result["status"] == "MANUAL_MODE"
    audit.reset_breaker("SPRINT-42")
    _, result = run(g)
    assert pending_interrupt(result) is not None


def test_breaker_is_per_sprint():
    audit = AuditLog()
    for _ in range(2):
        audit.append({"event": "run_end", "sprint_id": "S-1", "status": "REJECTED", "grounding_warnings_count": 1})
    assert audit.breaker_tripped("S-1", 2) and not audit.breaker_tripped("S-2", 2)
    audit.append({"event": "run_end", "sprint_id": "S-1", "status": "COMPLETED", "grounding_warnings_count": 0})
    assert not audit.breaker_tripped("S-1", 2)


def test_audit_log_persists_jsonl(tmp_path):
    a = AuditLog(tmp_path / "runs" / "audit.jsonl")
    a.append({"event": "run_end", "sprint_id": "S", "status": "COMPLETED"})
    assert AuditLog(tmp_path / "runs" / "audit.jsonl").records()[0]["sprint_id"] == "S"


def test_unused_fakes_are_importable():
    assert FakeJira() and FakeGitHub() and FakeSlack()
