export type SourceType = 'iot' | 'bluetooth' | 'manual' | 'import' | 'external'
export type DomainType = 'vital' | 'behavior' | 'environment' | 'care_record' | 'medication' | 'event'

export interface UnifiedObservation {
  observationId: string
  personId: string
  metric: string
  value: number | string
  unit?: string
  occurredAt: string
  sourceType: SourceType
  sourceDeviceId?: string
  domain: DomainType
  tags?: string[]
  rawPayload?: Record<string, unknown>
}

export interface Alert {
  alertId: string
  personId: string
  observationId: string
  level: 'medium' | 'high' | 'critical'
  reason: string
  status: 'open' | 'closed'
}

export interface CareTask {
  taskId: string
  alertId: string
  assigneeRole: 'caregiver' | 'nurse' | 'doctor'
  title: string
  status: 'todo' | 'done'
}
