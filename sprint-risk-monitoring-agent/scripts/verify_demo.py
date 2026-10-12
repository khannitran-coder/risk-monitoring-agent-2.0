"""Verify synthetic risk flow with a human reject checkpoint; no external writes."""
from datetime import date
from sprint_risk_agent.graph import build_graph
from sprint_risk_agent.mcp_clients.fake import demo_clients
from sprint_risk_agent.runner import pending_interrupt, resume_run, start_run

def main():
    clients = demo_clients(date(2026, 10, 7))
    graph = build_graph(clients)
    thread_id, state = start_run(graph, "SPRINT-42", as_of="2026-10-07")
    checkpoint = pending_interrupt(state)
    assert checkpoint is not None, "Expected human checkpoint"
    assert clients.slack.sent == []
    assert clients.jira.create_calls == 0
    result = resume_run(graph, thread_id, "reject")
    assert result["status"] == "REJECTED"
    assert clients.slack.sent == []
    assert clients.jira.create_calls == 0
    print("DEMO VERIFIED: synthetic risk, human checkpoint, rejection, no writes")

if __name__ == "__main__":
    main()
