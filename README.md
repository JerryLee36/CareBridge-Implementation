# CareBridge-Implementation

CareBridge is a digital health and coordinated-care platform for community elderly care institutions.

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
│   ├── web-admin/                       # Admin operations portal (React)
│   ├── caregiver-h5/                    # Caregiver mobile H5 (React)
│   ├── clinician-web/                   # Clinician / professional workspace (React)
│   └── family-h5/                       # Family / elderly mobile H5 (React)
├── packages/
│   └── shared-types/                    # Shared TS domain contracts across frontend apps
├── infra/
│   └── docker-compose.yml               # PostgreSQL + Redis local startup
└── README.md
```

## 2) Product Blueprint (English Modules)

### Multi-role service layer
- **Admin Portal (PC/Big Screen)**: organization dashboard, risk map, quality stats, device and user management, export center.
- **Caregiver H5/App**: today’s tasks, operational instructions, execution feedback, task handover, knowledge guidance.
- **Clinician/Professional Web/App**: trend analytics, risk details, health report review, remote support, intervention management.
- **Family/Elderly H5**: health briefs, abnormal alerts, progress tracking, confirmation feedback, service history.

### AI service layer
- LLM-assisted outputs based on warning results, medical knowledge, and communication templates:
  - Care action recommendations
  - Family communication drafts
  - Health education content
  - Shift handover summaries
  - Weekly health reports

### Smart health core
- Data quality control
- Rule engine with version management
- Trend analysis
- Closed-loop care engine (Alert -> Task -> Execute -> Feedback -> Review)

### Data standardization and adapter layer
- Device adapter registry for IoT, Bluetooth, manual, imported, and external system sources.
- Unified data model for person profile, vital signs, behavior, environment, and event records.

### Platform foundation
- Role and permission management
- Data security and privacy guardrails
- Audit logging and traceability
- Notification center (SMS / phone call / WeChat / email integration points)
- Knowledge base, medical rule content management, and system configuration center

## 3) Initialization Recommendations & Core Config

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

## 4) MVP Unified Data Model & Closed-loop Prototype

Implemented in:
- Unified data model: `/apps/backend/app/models/unified.py`
- Device adaptation: `/apps/backend/app/adapters/`
- Rule engine: `/apps/backend/app/rules/engine.py`
- Closed-loop engine: `/apps/backend/app/care_loop/engine.py`
- End-to-end data flow pipeline: `/apps/backend/app/services/pipeline.py`
- API entrypoint for ingestion: `/apps/backend/app/api/routes_ingestion.py`

### Current data flow
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

## 5) Current Implementation Status
- Added role-based backend routes:
  - `/admin/dashboard`, `/admin/permissions/{role}`
  - `/caregiver/tasks/today`, `/caregiver/handover`
  - `/clinician/trend/{person_id}/{metric}`, `/clinician/advice/send`
  - `/family/reports/{person_id}`, `/family/feedback`
- Added backend platform services:
  - data quality checks
  - rule-set version registry
  - trend analytics
  - notifications
  - RBAC
  - audit logs
  - system settings
- Added adapter registry and in-memory observation store for demo analytics.
- Expanded frontend role experiences in English:
  - admin dashboard sections in `apps/web-admin`
  - caregiver task workflow in `apps/caregiver-h5`
  - clinician workspace in `apps/clinician-web`
  - family mobile experience in `apps/family-h5`
