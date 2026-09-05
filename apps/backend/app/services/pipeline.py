from app.care_loop.engine import Alert, CareTask, ClosedLoopEngine
from app.ingestion.schemas import RawDevicePayload
from app.models.unified import UnifiedObservation
from app.rules.engine import RuleEngine
from app.services.adapter_registry import AdapterRegistry


class PipelineResult(dict):
    observation: UnifiedObservation
    alert: Alert | None
    task: CareTask | None


class IngestionPipeline:
    """Data Ingestion -> Standardization -> Rule Engine -> Alert -> Task"""

    def __init__(self) -> None:
        self.adapter_registry = AdapterRegistry()
        self.rule_engine = RuleEngine()
        self.closed_loop = ClosedLoopEngine()

    def run(self, payload: RawDevicePayload) -> PipelineResult:
        adapter = self.adapter_registry.get(payload.source_type)
        observation = adapter.transform(payload)
        rule_result = self.rule_engine.evaluate(observation)

        if not rule_result.triggered:
            return PipelineResult(observation=observation, alert=None, task=None)

        alert = self.closed_loop.create_alert(observation, rule_result)
        task = self.closed_loop.dispatch_task(alert)
        return PipelineResult(observation=observation, alert=alert, task=task)
