from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph

from .audit import AuditLog
from .config import DEFAULT_SETTINGS, Settings
from .mcp_clients.base import Clients
from .nodes.actions import make_action_nodes
from .nodes.checkpoints import make_checkpoint_nodes
from .nodes.correlate import make_correlate_node
from .nodes.draft import Drafter, TemplateDrafter, make_draft_nodes
from .nodes.fetch import make_fetch_nodes
from .nodes.session import make_session_nodes
from .state import AgentState


def build_graph(
    clients: Clients,
    drafter: Drafter | None = None,
    audit: AuditLog | None = None,
    settings: Settings = DEFAULT_SETTINGS,
    checkpointer=None,
):
    """Luồng:
    init_session -> (fetch_jira | fetch_github | fetch_slack) -> correlate_signals
      -> LOW/MEDIUM : draft_digest -> spot_check -> send_digest -> cleanup
      -> HIGH/CRIT  : draft_action_plan -> human_approval -> escalate -> cleanup
    edit -> quay lại node soạn thảo (tối đa settings.max_revisions); reject -> cleanup, không gửi.
    checkpointer mặc định MemorySaver (dev/test: mất state khi restart process).
    """
    drafter = drafter or TemplateDrafter()
    audit = audit or AuditLog()
    init_session, route_after_init, cleanup_session = make_session_nodes(audit, settings)
    fetch_jira, fetch_github, fetch_slack = make_fetch_nodes(clients)
    correlate_signals, route_after_correlate = make_correlate_node(settings)
    draft_digest, draft_action_plan = make_draft_nodes(drafter)
    spot_check, human_approval = make_checkpoint_nodes(settings)
    send_digest, escalate = make_action_nodes(clients, settings)

    g = StateGraph(AgentState)
    for name, fn in [
        ("init_session", init_session), ("fetch_jira", fetch_jira), ("fetch_github", fetch_github),
        ("fetch_slack", fetch_slack), ("correlate_signals", correlate_signals),
        ("draft_digest", draft_digest), ("spot_check", spot_check), ("send_digest", send_digest),
        ("draft_action_plan", draft_action_plan), ("human_approval", human_approval),
        ("escalate", escalate), ("cleanup_session", cleanup_session),
    ]:
        g.add_node(name, fn)

    g.set_entry_point("init_session")
    g.add_conditional_edges("init_session", route_after_init)
    g.add_edge(["fetch_jira", "fetch_github", "fetch_slack"], "correlate_signals")
    g.add_conditional_edges("correlate_signals", route_after_correlate,
                            {"draft_digest": "draft_digest", "draft_action_plan": "draft_action_plan"})
    g.add_edge("draft_digest", "spot_check")        # spot_check định tuyến bằng Command(goto=...)
    g.add_edge("send_digest", "cleanup_session")
    g.add_edge("draft_action_plan", "human_approval")  # human_approval định tuyến bằng Command(goto=...)
    g.add_edge("escalate", "cleanup_session")
    g.add_edge("cleanup_session", END)
    return g.compile(checkpointer=checkpointer or MemorySaver())
