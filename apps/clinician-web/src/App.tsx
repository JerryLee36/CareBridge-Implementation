import type { CSSProperties } from 'react'

const cardStyle: CSSProperties = {
  border: '1px solid #d0d7de',
  borderRadius: 12,
  padding: 16,
  background: '#fff',
}

export default function App() {
  return (
    <main style={{ fontFamily: 'Inter, system-ui, sans-serif', padding: 24, background: '#f6f8fa', color: '#1f2328' }}>
      <h1>CareBridge Clinician Workspace</h1>
      <p>Professional insights and intervention support for cross-role care collaboration.</p>
      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(230px, 1fr))', gap: 12 }}>
        <article style={cardStyle}>
          <h2>Trend Analysis</h2>
          <p>Daily, weekly, and monthly trend views for key indicators.</p>
        </article>
        <article style={cardStyle}>
          <h2>Risk Review</h2>
          <p>Risk assessment details with trigger traceability.</p>
        </article>
        <article style={cardStyle}>
          <h2>Remote Guidance</h2>
          <p>Guidance delivery for caregiver execution and follow-up.</p>
        </article>
      </section>
    </main>
  )
}
