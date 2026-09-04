# CareBridge-Implementation

CareBridge-Demo is a digital health and care coordination platform for grassroots elderly care institutions.

## 1) Standard Repository Structure

```text
CareBridge-Implementation/
├── apps/
│   ├── backend/                         # FastAPI backend (ingestion, adaptation, rules, closed loop)
│   │   ├── app/
│   │   │   ├── api/                     # API routes (ingestion, multi-role service endpoints)
│   │   │   ├── ingestion/               # Multi-source payload schemas
│   │   │   ├── adapters/                # Device adapters and protocol mapping
│   │   │   ├── models/                  # Unified data model & core entities
│   │   │   ├── rules/                   # Medical rule engine
│   │   │   ├── care_loop/               # Alert -> Task -> Action -> Review -> Closure model
│   │   │   ├── services/                # Orchestration pipelines
│   │   │   ├── core/                    # Config/security/foundation setup
│   │   │   └── main.py
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   └── .env.example
│   ├── web-admin/                       # Institution management portal (React)
│   └── caregiver-h5/                    # Caregiver mobile H5 (React scaffold; Uni-app can replace later)
├── packages/
│   └── shared-types/                    # Shared TS domain contracts across frontend apps
├── infra/
│   └── docker-compose.yml               # PostgreSQL + Redis local startup
└── README.md
```

## 2) Initialization Recommendations & Core Config

### Backend (FastAPI)
- Use `pyproject.toml` for dependency and test baseline.
- Start app: `uvicorn app.main:app --reload --app-dir apps/backend`.
- Keep configurable runtime values in `apps/backend/.env.example`.

### Data & Cache
- Start baseline infra with `infra/docker-compose.yml` (PostgreSQL + Redis).
- Use PostgreSQL for longitudinal health/care records and Redis for alert/task queue and cache.

### Frontend
- `apps/web-admin`: institution/operations dashboard and management.
- `apps/caregiver-h5`: caregiver task execution and care logging.
- `packages/shared-types`: shared entity contracts to avoid schema drift.

## 3) MVP Unified Data Model & Closed-loop Prototype

Implemented in:
- Unified data model: `/apps/backend/app/models/unified.py`
- Device adaptation: `/apps/backend/app/adapters/`
- Rule engine: `/apps/backend/app/rules/engine.py`
- Closed-loop engine: `/apps/backend/app/care_loop/engine.py`
- End-to-end data flow pipeline: `/apps/backend/app/services/pipeline.py`
- API entrypoint for ingestion: `/apps/backend/app/api/routes_ingestion.py`

### Current data flow demo
1. Data Ingestion: `/ingestion/events` receives multi-source raw payload.
2. Standardization: adapter converts payload to `UnifiedObservation`.
3. Rule Engine: threshold rule evaluation on standardized metrics.
4. Alert Trigger: rule hit generates `Alert`.
5. Task Dispatch: closed-loop engine generates actionable `CareTask`.

### Covered MVP core entity domains (reserved baseline)
- Person & Contact (`Person`, `Contact`)
- Health observations (`UnifiedObservation`) including vital/behavior/environment
- Care/medication/event domains via `DomainType`
- Alert -> Task closed-loop baseline (`Alert`, `CareTask`)

## 4) Next Suggested Expansion
- Add ADL/MMSE/Risk Assessment dedicated models and scoring services.
- Add adapter registry for smart mattress, radar, glucose meters, and HIS sync.
- Add Action/Review/Closure states and workflow persistence tables.
- Add AI assistant module for care suggestions, family communication, and shift summaries.
- Add role/permission, audit log, and message notification modules.
