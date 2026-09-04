from dataclasses import dataclass

from app.models.unified import UnifiedObservation


@dataclass(slots=True)
class RuleResult:
    triggered: bool
    level: str | None = None
    reason: str | None = None


class RuleEngine:
    """MVP medical rule base for threshold checks."""

    def evaluate(self, observation: UnifiedObservation) -> RuleResult:
        if observation.metric == "systolic_bp" and float(observation.value) >= 160:
            return RuleResult(triggered=True, level="high", reason="High systolic blood pressure")
        if observation.metric == "spo2" and float(observation.value) < 90:
            return RuleResult(triggered=True, level="critical", reason="Low blood oxygen")
        return RuleResult(triggered=False)
