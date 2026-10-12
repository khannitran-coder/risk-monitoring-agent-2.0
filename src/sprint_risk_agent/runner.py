"""Helper chạy/resume graph theo thread_id."""

import uuid

from langgraph.types import Command


def _cfg(thread_id: str) -> dict:
    return {"configurable": {"thread_id": thread_id}}


def start_run(graph, sprint_id: str, thread_id: str | None = None, as_of: str | None = None):
    """Trả (thread_id, result). Nếu graph dừng ở checkpoint, dùng pending_interrupt(result)."""
    thread_id = thread_id or str(uuid.uuid4())
    initial = {"sprint_id": sprint_id}
    if as_of:
        initial["as_of"] = as_of
    return thread_id, graph.invoke(initial, _cfg(thread_id))


def resume_run(graph, thread_id: str, action: str, notes: str | None = None):
    return graph.invoke(Command(resume={"action": action, "notes": notes}), _cfg(thread_id))


def pending_interrupt(result) -> dict | None:
    items = result.get("__interrupt__") if isinstance(result, dict) else None
    return items[0].value if items else None
