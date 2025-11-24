# Accessibility Checker

**Comprehensive WCAG compliance checking, accessibility testing, and automated fixes.**

**IMPORTANT: Ensure your application is accessible to all users with automated testing and fixes.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 ACCESSIBILITY CHECKER v3.3                        ║
║          WCAG 2.1 · ARIA · Screen Readers · Keyboard Nav             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  ACCESSIBILITY SCORE
════════════════════════════════════════════════════════════════════════

**Overall Accessibility: 67/100** ⚠️ (Target: 95+)

┌────────────────────────────────────────────────────────────────────┐
│ WCAG Level             │ Pass   │ Fail   │ Score               │
├────────────────────────────────────────────────────────────────────┤
│ Level A (Minimum)      │ 89%    │ 11%    │ ✅ Good             │
│ Level AA (Target)      │ 67%    │ 33%    │ ⚠️ Needs Work       │
│ Level AAA (Enhanced)   │ 23%    │ 77%    │ 🔴 Optional         │
└────────────────────────────────────────────────────────────────────┘

**Critical Issues:** 47 🔴
**Major Issues:** 89 ⚠️
**Minor Issues:** 123 🟡

════════════════════════════════════════════════════════════════════════
  CRITICAL VIOLATIONS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Issue                  │ Count │ WCAG    │ Impact              │
├────────────────────────────────────────────────────────────────────┤
│ Missing alt text       │ 23    │ 1.1.1   │ 🔴 Screen readers   │
│ Low color contrast     │ 45    │ 1.4.3   │ 🔴 Low vision       │
│ Missing form labels    │ 12    │ 3.3.2   │ 🔴 Screen readers   │
│ No keyboard access     │ 8     │ 2.1.1   │ 🔴 Keyboard users   │
│ Missing ARIA labels    │ 34    │ 4.1.2   │ 🔴 Assistive tech   │
│ Focus not visible      │ 15    │ 2.4.7   │ 🔴 Keyboard nav     │
│ No skip links          │ 1     │ 2.4.1   │ ⚠️ Keyboard users   │
└────────────────────────────────────────────────────────────────────┘

**Automated Fixes Available:** 89/137 (65%)

════════════════════════════════════════════════════════════════════════
  COLOR CONTRAST ANALYSIS
════════════════════════════════════════════════════════════════════════

**Contrast Violations:**

┌────────────────────────────────────────────────────────────────────┐
│ Element         │ Foreground │ Background │ Ratio │ Required │ Fix │
├────────────────────────────────────────────────────────────────────┤
│ .text-muted     │ #9CA3AF    │ #FFFFFF    │ 2.8:1 │ 4.5:1    │ 🔴  │
│ .btn-secondary  │ #60A5FA    │ #DBEAFE    │ 1.9:1 │ 3:1      │ 🔴  │
│ .link-subtle    │ #93C5FD    │ #FFFFFF    │ 2.1:1 │ 4.5:1    │ 🔴  │
│ .badge-warning  │ #FCD34D    │ #FFFFFF    │ 1.8:1 │ 3:1      │ 🔴  │
└────────────────────────────────────────────────────────────────────┘

**Auto-Fix Color Suggestions:**

```css
/* ❌ CURRENT - Failing contrast */
.text-muted {
  color: #9CA3AF; /* 2.8:1 ratio - FAILS */
}

/* ✅ FIXED - Meeting WCAG AA */
.text-muted {
  color: #6B7280; /* 4.5:1 ratio - PASSES */
}

/* Color Palette with Guaranteed Contrast */
:root {
  /* Text on white background (4.5:1 minimum) */
  --text-primary: #111827;   /* 19.5:1 ✅ */
  --text-secondary: #4B5563; /* 7.9:1 ✅ */
  --text-muted: #6B7280;     /* 4.5:1 ✅ */

  /* Large text on white (3:1 minimum) */
  --text-large-accent: #60A5FA; /* 3.1:1 ✅ */

  /* Interactive elements */
  --focus-ring: #3B82F6;     /* High visibility */
  --error: #DC2626;          /* 5.9:1 ✅ */
  --success: #059669;        /* 5.8:1 ✅ */
}
```

════════════════════════════════════════════════════════════════════════
  KEYBOARD NAVIGATION AUDIT
════════════════════════════════════════════════════════════════════════

**Keyboard Accessibility:**

┌────────────────────────────────────────────────────────────────────┐
│ Component              │ Tab Order │ Focus Trap │ Shortcuts │ Status│
├────────────────────────────────────────────────────────────────────┤
│ Navigation Menu        │ ✅        │ N/A        │ ❌        │ ⚠️    │
│ Modal Dialog           │ ❌        │ ❌         │ ❌        │ 🔴    │
│ Dropdown Menu          │ ⚠️        │ ❌         │ ❌        │ 🔴    │
│ Data Table             │ ✅        │ N/A        │ ✅        │ ✅    │
│ Form Controls          │ ✅        │ N/A        │ ⚠️        │ ⚠️    │
│ Carousel               │ ❌        │ ❌         │ ❌        │ 🔴    │
└────────────────────────────────────────────────────────────────────┘

**Keyboard Navigation Fixes:**

```typescript
// ✅ Proper Focus Management
export const Modal = ({ isOpen, onClose, children }) => {
  const modalRef = useRef<HTMLDivElement>(null);
  const previousFocus = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (isOpen) {
      // Store previous focus
      previousFocus.current = document.activeElement as HTMLElement;

      // Focus first focusable element
      const focusable = modalRef.current?.querySelector<HTMLElement>(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      );
      focusable?.focus();

      // Trap focus
      const handleTab = (e: KeyboardEvent) => {
        if (e.key === 'Tab') {
          const focusables = modalRef.current?.querySelectorAll<HTMLElement>(
            'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
          );

          if (focusables && focusables.length > 0) {
            const first = focusables[0];
            const last = focusables[focusables.length - 1];

            if (e.shiftKey && document.activeElement === first) {
              e.preventDefault();
              last.focus();
            } else if (!e.shiftKey && document.activeElement === last) {
              e.preventDefault();
              first.focus();
            }
          }
        }

        if (e.key === 'Escape') {
          onClose();
        }
      };

      document.addEventListener('keydown', handleTab);
      return () => document.removeEventListener('keydown', handleTab);
    } else {
      // Restore focus
      previousFocus.current?.focus();
    }
  }, [isOpen, onClose]);

  return (
    <div
      ref={modalRef}
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      className={isOpen ? 'block' : 'hidden'}
    >
      {children}
    </div>
  );
};

// ✅ Skip Links
export const SkipLinks = () => (
  <div className="sr-only focus:not-sr-only">
    <a href="#main-content" className="skip-link">
      Skip to main content
    </a>
    <a href="#main-navigation" className="skip-link">
      Skip to navigation
    </a>
  </div>
);
```

════════════════════════════════════════════════════════════════════════
  SCREEN READER SUPPORT
════════════════════════════════════════════════════════════════════════

**ARIA Implementation Status:**

┌────────────────────────────────────────────────────────────────────┐
│ ARIA Pattern           │ Correct │ Incorrect │ Missing │ Status   │
├────────────────────────────────────────────────────────────────────┤
│ Landmarks              │ 5       │ 2         │ 8       │ 🔴       │
│ Live Regions           │ 2       │ 3         │ 12      │ 🔴       │
│ Labels & Descriptions  │ 34      │ 12        │ 45      │ 🔴       │
│ Roles                  │ 23      │ 8         │ 19      │ ⚠️       │
│ States & Properties    │ 45      │ 15        │ 67      │ 🔴       │
└────────────────────────────────────────────────────────────────────┘

**ARIA Best Practices:**

```tsx
// ✅ Proper ARIA Implementation
export const AccessibleForm = () => {
  const [errors, setErrors] = useState({});
  const errorId = useId();

  return (
    <form aria-labelledby="form-title">
      <h2 id="form-title">Contact Form</h2>

      {/* Accessible Input with Error */}
      <div>
        <label htmlFor="email">
          Email Address
          <span aria-label="required">*</span>
        </label>
        <input
          id="email"
          type="email"
          aria-required="true"
          aria-invalid={!!errors.email}
          aria-describedby={errors.email ? errorId : undefined}
        />
        {errors.email && (
          <span id={errorId} role="alert" className="error">
            {errors.email}
          </span>
        )}
      </div>

      {/* Live Region for Status Updates */}
      <div
        role="status"
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {status && `Form status: ${status}`}
      </div>

      {/* Accessible Button */}
      <button
        type="submit"
        aria-busy={isSubmitting}
        disabled={isSubmitting}
      >
        {isSubmitting ? (
          <>
            <Spinner aria-hidden="true" />
            <span>Submitting...</span>
          </>
        ) : (
          'Submit'
        )}
      </button>
    </form>
  );
};

// ✅ Semantic HTML with ARIA
export const NavigationMenu = () => (
  <nav aria-label="Main navigation">
    <ul role="list">
      <li>
        <a href="/" aria-current={pathname === '/' ? 'page' : undefined}>
          Home
        </a>
      </li>
      <li>
        <button
          aria-expanded={isDropdownOpen}
          aria-controls="products-menu"
          aria-haspopup="true"
        >
          Products
        </button>
        <ul
          id="products-menu"
          role="menu"
          aria-label="Products submenu"
          hidden={!isDropdownOpen}
        >
          <li role="menuitem">
            <a href="/products/software">Software</a>
          </li>
        </ul>
      </li>
    </ul>
  </nav>
);
```

════════════════════════════════════════════════════════════════════════
  FORM ACCESSIBILITY
════════════════════════════════════════════════════════════════════════

**Form Issues:**

┌────────────────────────────────────────────────────────────────────┐
│ Issue                  │ Count │ Impact  │ Auto-Fix Available      │
├────────────────────────────────────────────────────────────────────┤
│ Missing labels         │ 12    │ 🔴 HIGH │ ✅ Yes                 │
│ No error associations  │ 23    │ 🔴 HIGH │ ✅ Yes                 │
│ Missing required attr  │ 8     │ ⚠️ MED  │ ✅ Yes                 │
│ No fieldset/legend     │ 5     │ ⚠️ MED  │ ✅ Yes                 │
│ Placeholder as label   │ 15    │ 🔴 HIGH │ ✅ Yes                 │
└────────────────────────────────────────────────────────────────────┘

**Form Accessibility Template:**

```tsx
// ✅ Fully Accessible Form Component
export const AccessibleFormField = ({
  label,
  error,
  required,
  helpText,
  ...inputProps
}) => {
  const inputId = useId();
  const errorId = useId();
  const helpId = useId();

  return (
    <div className="form-field">
      <label htmlFor={inputId} className="form-label">
        {label}
        {required && (
          <abbr title="required" aria-label="required">
            *
          </abbr>
        )}
      </label>

      {helpText && (
        <div id={helpId} className="form-help">
          {helpText}
        </div>
      )}

      <input
        id={inputId}
        aria-required={required}
        aria-invalid={!!error}
        aria-describedby={[
          helpText && helpId,
          error && errorId,
        ].filter(Boolean).join(' ')}
        {...inputProps}
      />

      {error && (
        <div id={errorId} role="alert" className="form-error">
          <Icon name="error" aria-hidden="true" />
          {error}
        </div>
      )}
    </div>
  );
};
```

════════════════════════════════════════════════════════════════════════
  IMAGE ACCESSIBILITY
════════════════════════════════════════════════════════════════════════

**Image Alt Text Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Image Type             │ Total │ With Alt │ Decorative │ Missing  │
├────────────────────────────────────────────────────────────────────┤
│ Content Images         │ 156   │ 89       │ N/A        │ 67 🔴    │
│ Icons                  │ 234   │ 12       │ 189        │ 33 🔴    │
│ Charts/Graphs          │ 23    │ 3        │ 0          │ 20 🔴    │
│ Background Images      │ 45    │ N/A      │ 45         │ 0 ✅     │
└────────────────────────────────────────────────────────────────────┘

**Image Accessibility Patterns:**

```tsx
// ✅ Content Image
<img
  src="team-photo.jpg"
  alt="Our development team at the 2024 company retreat"
/>

// ✅ Decorative Image
<img src="decorative-border.png" alt="" role="presentation" />

// ✅ Complex Image with Description
<figure>
  <img
    src="sales-chart.png"
    alt="Sales chart showing 40% growth"
    aria-describedby="chart-description"
  />
  <figcaption id="chart-description">
    Detailed sales data: Q1: $1.2M, Q2: $1.5M, Q3: $1.8M, Q4: $2.1M
  </figcaption>
</figure>

// ✅ Icon Buttons
<button aria-label="Close dialog">
  <Icon name="close" aria-hidden="true" />
</button>

// ✅ SVG Accessibility
<svg role="img" aria-labelledby="svg-title svg-desc">
  <title id="svg-title">Company Logo</title>
  <desc id="svg-desc">Abstract geometric shapes forming the letter A</desc>
  {/* SVG content */}
</svg>
```

════════════════════════════════════════════════════════════════════════
  AUTOMATED TESTING
════════════════════════════════════════════════════════════════════════

**Testing Configuration:**

```javascript
// jest-axe configuration
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('Accessibility Tests', () => {
  it('should have no accessibility violations', async () => {
    const { container } = render(<App />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('should have proper ARIA attributes', () => {
    render(<Modal isOpen />);
    const dialog = screen.getByRole('dialog');
    expect(dialog).toHaveAttribute('aria-modal', 'true');
    expect(dialog).toHaveAttribute('aria-labelledby');
  });
});

// Playwright accessibility testing
test('accessibility', async ({ page }) => {
  await page.goto('/');
  const accessibilityScanResults = await page.accessibility.snapshot();
  expect(accessibilityScanResults).toMatchSnapshot();
});
```

════════════════════════════════════════════════════════════════════════
  COMPLIANCE REPORT
════════════════════════════════════════════════════════════════════════

**Standards Compliance:**

┌────────────────────────────────────────────────────────────────────┐
│ Standard               │ Compliance │ Issues │ Status             │
├────────────────────────────────────────────────────────────────────┤
│ WCAG 2.1 Level AA      │ 67%        │ 89     │ ⚠️ Needs Work      │
│ Section 508            │ 71%        │ 67     │ ⚠️ Good           │
│ ADA                    │ 69%        │ 78     │ ⚠️ Needs Work      │
│ EN 301 549             │ 64%        │ 92     │ ⚠️ Needs Work      │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  ACTION PLAN
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL (Immediate):**
1. Fix 45 color contrast issues
2. Add missing alt text to 120 images
3. Label all form inputs (12 missing)
4. Implement keyboard navigation for modals
5. Add skip links to all pages

**⚠️ HIGH (This Week):**
6. Add ARIA landmarks
7. Implement focus management
8. Fix screen reader announcements
9. Add keyboard shortcuts
10. Test with real screen readers

**🟡 MEDIUM (This Sprint):**
11. Improve error messaging
12. Add transcripts for media
13. Implement high contrast mode
14. Add accessibility statement
15. Train team on a11y

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/accessibility-checker` - Full accessibility audit
• `/accessibility-checker --wcag` - WCAG compliance check
• `/accessibility-checker --contrast` - Color contrast analysis
• `/accessibility-checker --keyboard` - Keyboard navigation test
• `/accessibility-checker --aria` - ARIA implementation audit
• `/accessibility-checker --fix` - Apply automated fixes

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Accessibility Checker** - Build for everyone, exclude no one