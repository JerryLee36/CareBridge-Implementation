from app.api.routes_admin import router as admin_router
from app.api.routes_caregiver import router as caregiver_router
from app.api.routes_clinician import router as clinician_router
from app.api.routes_family import router as family_router
from fastapi import FastAPI

from app.api.routes_ingestion import router as ingestion_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.include_router(ingestion_router)
app.include_router(admin_router)
app.include_router(caregiver_router)
app.include_router(clinician_router)
app.include_router(family_router)


@app.get("/health")
def health_check():
    return {"status": "ok", "service": settings.app_name}
