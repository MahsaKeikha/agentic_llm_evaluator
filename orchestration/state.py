from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass
class EvaluationState:
    case: dict[str, Any]
    run_id: str = field(default_factory=lambda: str(uuid4()))
    plan: dict[str, Any] = field(default_factory=dict)
    judgments: dict[str, dict[str, Any]] = field(default_factory=dict)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    disagreements: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)
    trace: list[dict[str, Any]] = field(default_factory=list)

    def record(self, actor: str, event: str, artifact: Any = None) -> None:
        self.trace.append({"step": len(self.trace) + 1, "actor": actor, "event": event, "artifact": artifact})
