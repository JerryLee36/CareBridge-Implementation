from fastapi import APIRouter

from app.models.platform import NotificationChannel, UserRole
from app.services.observation_store import observation_store
from app.services.platform_context import platform_context

router = APIRouter(prefix="/clinician", tags=["clinician"])


@router.get("/trend/{person_id}/{metric}")
def trend(person_id: str, metric: str):
    insight = platform_context.trend.summarize(person_id, metric, observation_store.list(), period="daily")
    return insight.model_dump(mode="json")


@router.post("/advice/send")
def send_guidance(person_id: str, guidance: str):
    msg = platform_context.notifications.send(
        person_id=person_id,
        recipient_role=UserRole.CAREGIVER,
        channel=NotificationChannel.WECHAT,
        title="Clinician Guidance",
        body=guidance,
    )
    return msg.model_dump(mode="json")
