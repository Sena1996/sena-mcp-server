# Responsive Validator

**Test responsive design across all devices, validate touch targets, and ensure mobile usability.**

**IMPORTANT: Comprehensive responsive design validation with visual testing capabilities.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 RESPONSIVE VALIDATOR v3.3                         ║
║      Mobile · Tablet · Desktop · Touch · Accessibility               ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  RESPONSIVE ANALYSIS
════════════════════════════════════════════════════════════════════════

**Device Coverage Report:**

┌────────────────────────────────────────────────────────────────────┐
│ Device Category         │ Tested  │ Issues  │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Mobile (320-768px)      │ ✅      │ 12      │ 🔴 Critical Issues  │
│ Tablet (768-1024px)     │ ✅      │ 5       │ ⚠️ Minor Issues     │
│ Desktop (1024-1920px)   │ ✅      │ 2       │ ✅ Good             │
│ Ultra-wide (>1920px)    │ ❌      │ -       │ 🔴 Not Tested       │
│ Touch Devices           │ ✅      │ 8       │ ⚠️ Touch Issues     │
│ Landscape Orientation   │ ⚠️       │ 6       │ ⚠️ Problems Found   │
└────────────────────────────────────────────────────────────────────┘

**Critical Breakpoint Issues:**

┌────────────────────────────────────────────────────────────────────┐
│ Breakpoint │ Component         │ Issue                │ Severity   │
├────────────────────────────────────────────────────────────────────┤
│ 320px      │ Navigation        │ Menu overflow        │ 🔴 High    │
│ 375px      │ Form inputs       │ Text truncation      │ ⚠️ Medium  │
│ 414px      │ Data table        │ Horizontal scroll    │ 🔴 High    │
│ 768px      │ Grid layout       │ Improper stacking    │ ⚠️ Medium  │
│ 1024px     │ Sidebar           │ Overlap with content │ 🟡 Low     │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  TOUCH TARGET VALIDATION
════════════════════════════════════════════════════════════════════════

**Touch Target Analysis (WCAG 2.5.5):**

┌────────────────────────────────────────────────────────────────────┐
│ Element                 │ Size    │ Min Required │ Status         │
├────────────────────────────────────────────────────────────────────┤
│ Primary buttons         │ 44×44px │ 44×44px      │ ✅ Pass        │
│ Navigation links        │ 32×24px │ 44×44px      │ 🔴 Too Small   │
│ Checkbox inputs         │ 18×18px │ 44×44px      │ 🔴 Too Small   │
│ Close buttons (×)       │ 24×24px │ 44×44px      │ 🔴 Too Small   │
│ Dropdown items          │ 44×32px │ 44×44px      │ ⚠️ Height Issue │
│ Tab navigation          │ 60×40px │ 44×44px      │ ⚠️ Height Issue │
│ Icon buttons            │ 36×36px │ 44×44px      │ 🔴 Too Small   │
└────────────────────────────────────────────────────────────────────┘

**Touch Target Fixes:**

```css
/* ❌ BAD - Too small for touch */
.icon-button {
  width: 24px;
  height: 24px;
  padding: 0;
}

/* ✅ GOOD - Proper touch target */
.icon-button {
  min-width: 44px;
  min-height: 44px;
  padding: 10px;
  /* Visual size can be smaller with padding */

  &::before {
    content: '';
    position: absolute;
    inset: -10px;
    /* Extends touch area beyond visual bounds */
  }
}
```

════════════════════════════════════════════════════════════════════════
  VIEWPORT CONFIGURATION
════════════════════════════════════════════════════════════════════════

**Current Viewport Issues:**

```html
<!-- ❌ CURRENT - Problems found -->
<meta name="viewport" content="width=device-width">
<!-- Missing: initial-scale, user-scalable -->

<!-- ✅ RECOMMENDED -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<!-- viewport-fit=cover for iPhone notch support -->
```

**Safe Area Handling (iPhone X+):**

```css
/* Handle device safe areas */
.app-container {
  padding-top: env(safe-area-inset-top);
  padding-right: env(safe-area-inset-right);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
}

/* Bottom navigation with safe area */
.bottom-nav {
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}
```

════════════════════════════════════════════════════════════════════════
  RESPONSIVE TYPOGRAPHY
════════════════════════════════════════════════════════════════════════

**Text Readability Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Screen Width │ Font Size │ Line Length │ Status                    │
├────────────────────────────────────────────────────────────────────┤
│ 320px        │ 14px      │ 45 chars    │ ⚠️ Too small font        │
│ 375px        │ 14px      │ 52 chars    │ ⚠️ Too small font        │
│ 768px        │ 16px      │ 75 chars    │ ✅ Good                  │
│ 1024px       │ 16px      │ 95 chars    │ 🔴 Line too long         │
│ 1440px       │ 16px      │ 120 chars   │ 🔴 Way too long          │
└────────────────────────────────────────────────────────────────────┘

**Optimal Typography Settings:**

```css
/* Fluid typography with constraints */
:root {
  --font-size-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --line-height-base: 1.5;
  --max-content-width: 65ch; /* Optimal reading length */
}

body {
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
}

.content {
  max-width: var(--max-content-width);
  margin: 0 auto;
  padding: 0 1rem;
}

/* Responsive heading scale */
h1 {
  font-size: clamp(1.75rem, 1.5rem + 2vw, 3rem);
}

h2 {
  font-size: clamp(1.5rem, 1.3rem + 1.5vw, 2.25rem);
}
```

════════════════════════════════════════════════════════════════════════
  RESPONSIVE IMAGES
════════════════════════════════════════════════════════════════════════

**Image Optimization Report:**

┌────────────────────────────────────────────────────────────────────┐
│ Image                   │ Mobile  │ Desktop │ Issue               │
├────────────────────────────────────────────────────────────────────┤
│ hero-banner.jpg         │ 2MB     │ 2MB     │ 🔴 Same size all devices│
│ product-gallery/*.jpg   │ 450KB   │ 450KB   │ ⚠️ No responsive images│
│ team-photos/*.png       │ 890KB   │ 890KB   │ 🔴 PNG on mobile      │
│ background-pattern.svg  │ 45KB    │ 45KB    │ ✅ Vector, OK         │
└────────────────────────────────────────────────────────────────────┘

**Responsive Image Implementation:**

```html
<!-- ✅ GOOD - Art direction with <picture> -->
<picture>
  <source
    media="(max-width: 640px)"
    srcset="/hero-mobile.webp 640w,
            /hero-mobile@2x.webp 1280w"
    sizes="100vw"
  />
  <source
    media="(max-width: 1024px)"
    srcset="/hero-tablet.webp 1024w,
            /hero-tablet@2x.webp 2048w"
    sizes="100vw"
  />
  <img
    src="/hero-desktop.webp"
    srcset="/hero-desktop.webp 1920w,
            /hero-desktop@2x.webp 3840w"
    sizes="100vw"
    alt="Hero banner"
    loading="lazy"
    decoding="async"
  />
</picture>
```

**Next.js Image Optimization:**

```tsx
import Image from 'next/image';

// Responsive with Next.js
<Image
  src="/hero.jpg"
  alt="Hero"
  sizes="(max-width: 640px) 100vw,
         (max-width: 1024px) 50vw,
         33vw"
  fill
  priority
  quality={{ default: 75, mobile: 60 }}
/>
```

════════════════════════════════════════════════════════════════════════
  RESPONSIVE LAYOUT PATTERNS
════════════════════════════════════════════════════════════════════════

**Common Layout Issues:**

┌────────────────────────────────────────────────────────────────────┐
│ Pattern                 │ Issue at Breakpoint     │ Fix Required    │
├────────────────────────────────────────────────────────────────────┤
│ Navigation menu         │ Breaks at 850px         │ Earlier hamburger│
│ Sidebar + content       │ Overlaps at 1000px      │ Stack vertically │
│ Card grid               │ 1 column until 768px     │ 2 cols at 640px │
│ Data table              │ Scrolls at 900px         │ Responsive table │
│ Modal dialogs           │ Full screen on mobile    │ Good ✅         │
│ Form layout             │ Single column always     │ 2 cols on tablet │
└────────────────────────────────────────────────────────────────────┘

**Responsive Grid System:**

```css
/* Mobile-first responsive grid */
.grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;

  @media (min-width: 640px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 1024px) {
    grid-template-columns: repeat(3, 1fr);
  }

  @media (min-width: 1280px) {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* Auto-fit grid */
.auto-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}
```

════════════════════════════════════════════════════════════════════════
  RESPONSIVE TABLES
════════════════════════════════════════════════════════════════════════

**Mobile Table Patterns:**

```css
/* Pattern 1: Stack on mobile */
@media (max-width: 640px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }

  thead tr {
    position: absolute;
    top: -9999px;
    left: -9999px;
  }

  tr {
    border: 1px solid #ccc;
    margin-bottom: 10px;
  }

  td {
    border: none;
    position: relative;
    padding-left: 50%;
  }

  td:before {
    content: attr(data-label);
    position: absolute;
    left: 6px;
    width: 45%;
    font-weight: bold;
  }
}

/* Pattern 2: Horizontal scroll with sticky column */
.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table th:first-child,
.table td:first-child {
  position: sticky;
  left: 0;
  background: white;
  z-index: 1;
}
```

════════════════════════════════════════════════════════════════════════
  PERFORMANCE METRICS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Device          │ FCP    │ LCP    │ CLS    │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Mobile 3G       │ 4.2s   │ 6.8s   │ 0.23   │ 🔴 Too Slow         │
│ Mobile 4G       │ 1.8s   │ 3.2s   │ 0.15   │ ⚠️ Optimize         │
│ Tablet WiFi     │ 0.9s   │ 1.8s   │ 0.08   │ ✅ Good             │
│ Desktop Cable   │ 0.4s   │ 0.9s   │ 0.02   │ ✅ Excellent        │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  RESPONSIVE TESTING CHECKLIST
════════════════════════════════════════════════════════════════════════

**✅ Complete:**
- [ ] Test all major breakpoints
- [ ] Verify touch targets (44×44px minimum)
- [ ] Check landscape orientation
- [ ] Test with real devices
- [ ] Validate viewport meta tag
- [ ] Test with slow 3G network
- [ ] Verify font sizes are readable
- [ ] Check image loading on mobile
- [ ] Test form usability on touch
- [ ] Validate gesture support

**📱 Device Testing Matrix:**
- iPhone SE (375×667)
- iPhone 14 Pro (393×852)
- iPad (768×1024)
- iPad Pro (1024×1366)
- Android Phone (360×800)
- Android Tablet (800×1280)

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/responsive-validator` - Full responsive audit
• `/responsive-validator --touch` - Touch target validation
• `/responsive-validator --images` - Responsive image audit
• `/responsive-validator --performance` - Mobile performance
• `/responsive-validator --devices <list>` - Test specific devices

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Responsive Validator** - Perfect experience on every device