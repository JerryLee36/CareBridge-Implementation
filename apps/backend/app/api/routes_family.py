from fastapi import APIRouter

from app.models.platform import UserRole
from app.services.platform_context import platform_context

router = APIRouter(prefix="/family", tags=["family"])


@router.get("/reports/{person_id}")
def family_report(person_id: str):
    messages = [
        item.model_dump(mode="json")
        for item in platform_context.notifications.list_messages()
        if item.person_id == person_id
    ]
    return {
        "person_id": person_id,
        "weekly_summary": "Health metrics are stable with mild blood pressure fluctuation.",
        "alerts": messages,
    }


@router.post("/feedback")
def submit_feedback(person_id: str, feedback: str):
    entry = platform_context.audit.record(
        action="family_feedback_submitted",
        actor_role=UserRole.FAMILY,
        resource_type="feedback",
        resource_id=person_id,
    )
    return {"status": "received", "feedback": feedback, "audit": entry.model_dump(mode="json")}
