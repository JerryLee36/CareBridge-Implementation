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

export type UserRole = 'admin' | 'caregiver' | 'clinician' | 'family'
export type NotificationChannel = 'sms' | 'phone_call' | 'wechat' | 'email'

export interface RuleSetVersion {
  version: string
  description: string
  createdAt: string
  enabled: boolean
}

export interface DataQualityReport {
  totalEvents: number
  missingValueEvents: number
  duplicateEvents: number
  abnormalValueEvents: number
  qualityScore: number
}

export interface TrendInsight {
  personId: string
  metric: string
  period: 'daily' | 'weekly' | 'monthly'
  minValue: number
  maxValue: number
  avgValue: number
  sampleCount: number
}

export interface NotificationMessage {
  messageId: string
  personId: string
  recipientRole: UserRole
  channel: NotificationChannel
  title: string
  body: string
  sentAt: string
}
