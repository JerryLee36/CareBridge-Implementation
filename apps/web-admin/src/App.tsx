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
      <h1>CareBridge Admin Platform</h1>
      <p>Institution command center for risk visibility, quality governance, and closed-loop care operations.</p>

      <section style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 12 }}>
        <article style={cardStyle}>
          <h2>Operations Dashboard</h2>
          <ul>
            <li>Organization overview</li>
            <li>Risk map and statistics</li>
            <li>Alert and task throughput</li>
          </ul>
        </article>
        <article style={cardStyle}>
          <h2>Data & Device Governance</h2>
          <ul>
            <li>Device inventory and status</li>
            <li>Data quality score</li>
            <li>Duplicate and anomaly checks</li>
          </ul>
        </article>
        <article style={cardStyle}>
          <h2>Rule & AI Services</h2>
          <ul>
            <li>Rule-set version management</li>
            <li>Care guidance templates</li>
            <li>Knowledge base operations</li>
          </ul>
        </article>
        <article style={cardStyle}>
          <h2>Platform Control</h2>
          <ul>
            <li>Role and permission management</li>
            <li>Audit and traceability logs</li>
            <li>Notification center and exports</li>
          </ul>
        </article>
      </section>
    </main>
  )
}
