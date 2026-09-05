from app.models.platform import DataQualityReport
from app.models.unified import UnifiedObservation


class DataQualityService:
    """Simple quality checks for normalized events."""

    def evaluate(self, observations: list[UnifiedObservation]) -> DataQualityReport:
        seen_ids: set[str] = set()
        duplicate_events = 0
        missing_value_events = 0
        abnormal_value_events = 0

        for item in observations:
            if item.observation_id in seen_ids:
                duplicate_events += 1
            seen_ids.add(item.observation_id)

            if item.value in {None, ""}:
                missing_value_events += 1

            if isinstance(item.value, (float, int)) and float(item.value) < 0:
                abnormal_value_events += 1

        total_events = len(observations)
        if total_events == 0:
            return DataQualityReport(
                total_events=0,
                missing_value_events=0,
                duplicate_events=0,
                abnormal_value_events=0,
                quality_score=100.0,
            )

        issue_count = missing_value_events + duplicate_events + abnormal_value_events
        quality_score = max(0.0, round(100 - (issue_count / total_events) * 100, 2))

        return DataQualityReport(
            total_events=total_events,
            missing_value_events=missing_value_events,
            duplicate_events=duplicate_events,
            abnormal_value_events=abnormal_value_events,
            quality_score=quality_score,
        )
