from app.models.platform import TrendInsight
from app.models.unified import UnifiedObservation


class TrendAnalysisService:
    def summarize(self, person_id: str, metric: str, observations: list[UnifiedObservation], period: str = "daily") -> TrendInsight:
        values = [float(item.value) for item in observations if item.person_id == person_id and item.metric == metric]

        if not values:
            return TrendInsight(
                person_id=person_id,
                metric=metric,
                period=period,
                min_value=0,
                max_value=0,
                avg_value=0,
                sample_count=0,
            )

        return TrendInsight(
            person_id=person_id,
            metric=metric,
            period=period,
            min_value=min(values),
            max_value=max(values),
            avg_value=round(sum(values) / len(values), 2),
            sample_count=len(values),
        )
