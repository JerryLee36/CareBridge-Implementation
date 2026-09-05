from fastapi import APIRouter

from app.ingestion.schemas import RawDevicePayload
from app.services.pipeline import IngestionPipeline
from app.services.observation_store import observation_store

router = APIRouter(prefix="/ingestion", tags=["ingestion"])
pipeline = IngestionPipeline()


@router.post("/events")
def ingest_event(payload: RawDevicePayload):
    result = pipeline.run(payload)
    observation_store.add(result["observation"])
    return {
        "observation": result["observation"].model_dump(mode="json"),
        "alert": result["alert"].model_dump(mode="json") if result["alert"] else None,
        "task": result["task"].model_dump(mode="json") if result["task"] else None,
    }
