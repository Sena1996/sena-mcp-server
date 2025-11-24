# Web Vitals Monitor

**Monitor Core Web Vitals metrics: LCP, FID, CLS, FCP, TTFB, INP.**

---

╔══════════════════════════════════════════════════════════════════════╗
║            SENA 🦁 WEB VITALS MONITOR v3.3                           ║
╚══════════════════════════════════════════════════════════════════════╝

**Core Web Vitals:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Value   │ Target  │ Percentile │ Status   │
├────────────────────────────────────────────────────────────────────┤
│ LCP (Largest Paint)    │ 3.2s    │ < 2.5s  │ P75        │ 🔴 Poor  │
│ FID (First Input)      │ 125ms   │ < 100ms │ P75        │ ⚠️ Needs │
│ CLS (Layout Shift)     │ 0.18    │ < 0.1   │ P75        │ ⚠️ Needs │
│ INP (Next Paint)       │ 234ms   │ < 200ms │ P75        │ ⚠️ Needs │
│ TTFB (First Byte)      │ 890ms   │ < 600ms │ P75        │ 🔴 Poor  │
└────────────────────────────────────────────────────────────────────┘

**Commands:**
• `/web-vitals` - Current metrics
• `/web-vitals --monitor` - Real-time monitoring
• `/web-vitals --field` - Field data analysis