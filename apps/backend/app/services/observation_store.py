from app.models.unified import UnifiedObservation


class ObservationStore:
    def __init__(self) -> None:
        self._items: list[UnifiedObservation] = []

    def add(self, observation: UnifiedObservation) -> None:
        self._items.append(observation)

    def list(self) -> list[UnifiedObservation]:
        return self._items


observation_store = ObservationStore()
