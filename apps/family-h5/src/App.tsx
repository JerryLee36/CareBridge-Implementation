import type { CSSProperties } from 'react'

const cardStyle: CSSProperties = {
  border: '1px solid #d0d7de',
  borderRadius: 12,
  padding: 14,
  background: '#fff',
}

export default function App() {
  return (
    <main style={{ fontFamily: 'Inter, system-ui, sans-serif', margin: '0 auto', maxWidth: 480, padding: 16, background: '#f6f8fa', color: '#1f2328' }}>
      <h1>CareBridge Family H5</h1>
      <p>Family-facing updates, alert communication, and care feedback.</p>
      <section style={{ display: 'grid', gap: 10 }}>
        <article style={cardStyle}>
          <h2>Health Reports</h2>
          <p>Weekly summaries and trend highlights in plain language.</p>
        </article>
        <article style={cardStyle}>
          <h2>Alert Notices</h2>
          <p>Abnormal-event notifications and progress follow-up.</p>
        </article>
        <article style={cardStyle}>
          <h2>Service Records</h2>
          <p>Execution timeline and confirmation updates.</p>
        </article>
        <article style={cardStyle}>
          <h2>Feedback</h2>
          <p>Submit concerns and receive response status.</p>
        </article>
      </section>
    </main>
  )
}
