"""Audit log (JSON lines) + circuit breaker. Đây là 'progress log' của cleanup_session."""

import json
from pathlib import Path


class AuditLog:
    def __init__(self, path: str | Path | None = None) -> None:
        self.path = Path(path) if path else None
        self._mem: list[dict] = []

    def append(self, record: dict) -> None:
        if self.path is None:
            self._mem.append(record)
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    def records(self) -> list[dict]:
        if self.path is None:
            return list(self._mem)
        if not self.path.exists():
            return []
        return [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines() if line.strip()]

    def breaker_tripped(self, sprint_id: str, threshold: int) -> bool:
        """Đúng khi `threshold` lần chạy hoàn tất gần nhất của sprint đều có grounding warning,
        tính từ lần reset gần nhất. Lần chạy MANUAL_MODE không được tính (breaker giữ tới khi reset)."""
        relevant: list[dict] = []
        for r in self.records():
            if r.get("sprint_id") != sprint_id:
                continue
            if r.get("event") == "breaker_reset":
                relevant = []
            elif r.get("event") == "run_end" and r.get("status") != "MANUAL_MODE":
                relevant.append(r)
        recent = relevant[-threshold:]
        return len(recent) >= threshold and all(r.get("grounding_warnings_count", 0) > 0 for r in recent)

    def reset_breaker(self, sprint_id: str) -> None:
        """PM xác nhận lại sau khi kiểm tra - cho phép agent chạy tự động trở lại."""
        self.append({"event": "breaker_reset", "sprint_id": sprint_id})
