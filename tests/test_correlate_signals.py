import pytest

from sprint_risk_agent.config import DEFAULT_SETTINGS as S
from sprint_risk_agent.nodes.correlate import classify, make_correlate_node

correlate, route = make_correlate_node(S)


@pytest.mark.parametrize(
    "n,days,expected",
    [
        (0, 1, None), (1, 0, None), (1, None, None),
        (2, 2, "MEDIUM"), (2, None, "MEDIUM"), (2, 5, "MEDIUM"), (2, 6, "LOW"),
        (3, 5, "HIGH"), (3, None, "HIGH"), (3, 2, "HIGH"),
        (3, 1, "CRITICAL"), (3, 0, "CRITICAL"), (3, -2, "CRITICAL"),
    ],
)
def test_classify_table(n, days, expected):
    assert classify(n, days, S) == expected


def state(jira=(), github=(), slack=(), as_of="2026-10-07"):
    return {"sprint_id": "SPRINT-1", "as_of": as_of, "jira_raw": list(jira),
            "github_raw": list(github), "slack_raw": list(slack)}


J = {"ticket_id": "AA-1", "status": "In Progress", "due_date": "2026-10-09"}
G = {"title": "AA-1: fix", "review_wait_hours": 49, "ci_status": "passed"}
SL = {"text": "AA-1 is blocked"}


def test_single_source_is_ignored_not_scored():
    out = correlate(state(jira=[J]))
    assert out["ticket_risk"] == {} and out["unconfirmed_tickets"] == ["AA-1"] and out["risk_level"] == "LOW"


def test_two_sources_medium():
    assert correlate(state(jira=[J], github=[G]))["ticket_risk"] == {"AA-1": "MEDIUM"}


def test_three_sources_high_and_critical_when_near_due():
    assert correlate(state(jira=[J], github=[G], slack=[SL]))["ticket_risk"] == {"AA-1": "HIGH"}
    near = {**J, "due_date": "2026-10-08"}
    out = correlate(state(jira=[near], github=[G], slack=[SL]))
    assert out["ticket_risk"] == {"AA-1": "CRITICAL"} and out["risk_level"] == "CRITICAL"


def test_done_ticket_gives_no_jira_signal():
    out = correlate(state(jira=[{**J, "status": "Done"}], github=[G], slack=[SL]))
    assert out["ticket_risk"] == {"AA-1": "MEDIUM"}  # chỉ còn github + slack


def test_thresholds_are_strict():
    ok_pr = {**G, "review_wait_hours": 48}  # đúng ngưỡng: chưa tính
    assert correlate(state(jira=[J], github=[ok_pr]))["ticket_risk"] == {}
    assert correlate(state(jira=[{**J, "due_date": "2026-10-10"}], github=[G]))["ticket_risk"] == {}  # còn 3 ngày


def test_slack_without_blocker_keyword_or_ticket_id_is_ignored():
    sl = [{"text": "AA-1 đang ổn"}, {"text": "mọi thứ bị chặn hết rồi"}]
    assert correlate(state(jira=[J], slack=sl))["ticket_risk"] == {}


def test_multiple_signals_from_same_source_count_once():
    out = correlate(state(jira=[J], slack=[SL, {"text": "AA-1 stuck again"}]))
    assert out["ticket_risk"] == {"AA-1": "MEDIUM"}


def test_routing():
    assert route({"risk_level": "MEDIUM"}) == "draft_digest"
    assert route({"risk_level": "HIGH"}) == "draft_action_plan"
    assert route({"risk_level": "CRITICAL"}) == "draft_action_plan"


def test_invalid_due_date_is_tolerated():
    assert correlate(state(jira=[{**J, "due_date": "tbd"}], github=[G]))["ticket_risk"] == {}
