# Folder Architecture Analyzer

**Analyze and optimize project folder structure and file organization.**

---

╔══════════════════════════════════════════════════════════════════════╗
║            SENA 🦁 FOLDER ARCHITECTURE ANALYZER v3.3                 ║
╚══════════════════════════════════════════════════════════════════════╝

**Current Structure Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Issue                  │ Count   │ Impact  │ Fix                 │
├────────────────────────────────────────────────────────────────────┤
│ Deep Nesting (>5)      │ 23      │ 🔴 High │ Flatten structure   │
│ Mixed Concerns         │ 45      │ 🔴 High │ Separate by feature │
│ Duplicate Files        │ 12      │ ⚠️ Med  │ Consolidate         │
│ Inconsistent Naming    │ 67      │ ⚠️ Med  │ Apply conventions   │
└────────────────────────────────────────────────────────────────────┘

**Recommended Structure:**
```
src/
├── features/        # Feature-based organization
├── shared/          # Shared components/utils
├── core/            # Core business logic
└── infrastructure/  # External services
```

**Commands:**
• `/folder-architect` - Analyze structure
• `/folder-architect --generate` - Generate ideal structure
• `/folder-architect --migrate` - Migration plan