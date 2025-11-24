# CSS Architect

**Optimize CSS architecture, enforce design systems, and implement best practices for styling.**

**IMPORTANT: Analyze and optimize CSS/Tailwind/CSS-in-JS with actionable improvements.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 CSS ARCHITECT v3.3                                ║
║    Tailwind · CSS Modules · Styled Components · Design Tokens        ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  CSS ANALYSIS OVERVIEW
════════════════════════════════════════════════════════════════════════

**Current Styling Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                  │ Current  │ Optimal  │ Status             │
├────────────────────────────────────────────────────────────────────┤
│ Total CSS Size          │ 234 KB   │ < 50 KB  │ 🔴 Too Large       │
│ Unused CSS              │ 67%      │ < 20%    │ 🔴 Critical        │
│ Duplicate Rules         │ 892      │ < 50     │ 🔴 Too Many        │
│ !important Usage        │ 147      │ 0        │ 🔴 Avoid           │
│ Specificity Max         │ 0,4,3,2  │ 0,1,2,0  │ ⚠️ Too Complex     │
│ Color Variables         │ 45%      │ 100%     │ ⚠️ Use Tokens      │
│ Responsive Breakpoints  │ 7        │ 3-5      │ ⚠️ Simplify        │
│ CSS-in-JS Bundle        │ 89 KB    │ < 30 KB  │ ⚠️ Optimize        │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  TAILWIND CSS OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Tailwind Usage Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Pattern                 │ Count │ Issue           │ Solution        │
├────────────────────────────────────────────────────────────────────┤
│ Arbitrary values        │ 234   │ Not reusable    │ Use config      │
│ Long className strings  │ 89    │ Hard to read    │ Use cn() helper │
│ Duplicate combinations  │ 156   │ Repetition      │ Extract component│
│ Inline responsive       │ 78    │ Verbose         │ Use containers  │
│ Custom CSS overrides    │ 45    │ Fighting Tailwind│ Extend theme   │
└────────────────────────────────────────────────────────────────────┘

**Tailwind Config Optimization:**

```javascript
// tailwind.config.js - Optimized
module.exports = {
  content: [
    './src/**/*.{ts,tsx}',
    // ✅ Specific paths prevent unused CSS
  ],
  theme: {
    extend: {
      // ✅ Design tokens as Tailwind theme
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        },
        gray: {
          // Custom gray scale matching design
        }
      },
      spacing: {
        // Consistent spacing scale
        '18': '4.5rem',
        '88': '22rem',
      },
      fontFamily: {
        sans: ['Inter var', 'system-ui'],
      },
      animation: {
        // Custom animations
        'slide-up': 'slideUp 0.3s ease-out',
        'fade-in': 'fadeIn 0.2s ease-in',
      },
    },
  },
  plugins: [
    // ✅ Only needed plugins
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
  // ✅ Production optimizations
  ...(process.env.NODE_ENV === 'production' && {
    purge: {
      enabled: true,
      safeList: [
        // Dynamic classes that shouldn't be purged
        /^bg-(red|green|blue)-/,
      ],
    },
  }),
}
```

**Better Tailwind Patterns:**

```tsx
// ❌ BAD - Long, unreadable className
<div className="flex items-center justify-between px-4 py-2 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200 border border-gray-200 hover:border-gray-300">

// ✅ GOOD - Using cn() helper with variants
import { cn } from '@/lib/utils';

const cardStyles = cn(
  // Base styles
  'flex items-center justify-between',
  'px-4 py-2',
  'bg-white rounded-lg',
  'border border-gray-200',
  // Interactive states
  'transition-shadow duration-200',
  'hover:shadow-lg hover:border-gray-300',
  // Conditional styles
  isActive && 'ring-2 ring-primary-500',
  isDisabled && 'opacity-50 cursor-not-allowed'
);
```

**Component Classes Pattern:**

```tsx
// ✅ Extract repeated combinations
const buttonVariants = {
  primary: 'bg-blue-500 text-white hover:bg-blue-600',
  secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
  danger: 'bg-red-500 text-white hover:bg-red-600',
};

const buttonSizes = {
  sm: 'px-3 py-1 text-sm',
  md: 'px-4 py-2',
  lg: 'px-6 py-3 text-lg',
};

// Usage
<button className={cn(buttonVariants[variant], buttonSizes[size])} />
```

════════════════════════════════════════════════════════════════════════
  CSS MODULES BEST PRACTICES
════════════════════════════════════════════════════════════════════════

**CSS Module Structure:**

```scss
// Button.module.scss
.button {
  // Base styles using CSS variables
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
  font-weight: var(--font-medium);
  transition: all 0.2s;

  // Variants using data attributes
  &[data-variant="primary"] {
    background: var(--color-primary);
    color: var(--color-primary-foreground);

    &:hover {
      background: var(--color-primary-hover);
    }
  }

  &[data-size="large"] {
    padding: var(--spacing-3) var(--spacing-6);
    font-size: var(--text-lg);
  }

  // State modifiers
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  // Responsive without media queries
  container-type: inline-size;

  @container (min-width: 400px) {
    padding: var(--spacing-3) var(--spacing-5);
  }
}
```

**TypeScript Integration:**

```tsx
// Button.tsx with CSS Modules
import styles from './Button.module.scss';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'small' | 'medium' | 'large';
}

export const Button: FC<ButtonProps> = ({
  variant = 'primary',
  size = 'medium',
  ...props
}) => {
  return (
    <button
      className={styles.button}
      data-variant={variant}
      data-size={size}
      {...props}
    />
  );
};
```

════════════════════════════════════════════════════════════════════════
  STYLED COMPONENTS OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Optimized Styled Components:**

```tsx
// ❌ BAD - Runtime style generation
const Button = styled.button`
  background: ${props => props.primary ? 'blue' : 'gray'};
  padding: ${props => props.large ? '16px' : '8px'};
`;

// ✅ GOOD - Static extraction with variants
const Button = styled.button<{ $variant: 'primary' | 'secondary' }>`
  /* Base styles */
  padding: var(--spacing-2) var(--spacing-4);
  border-radius: var(--radius-md);
  transition: all 0.2s;

  /* Variant styles using CSS */
  ${({ $variant }) => {
    switch ($variant) {
      case 'primary':
        return css`
          background: var(--color-primary);
          color: white;

          &:hover {
            background: var(--color-primary-dark);
          }
        `;
      case 'secondary':
        return css`
          background: var(--color-gray-200);
          color: var(--color-gray-900);
        `;
    }
  }}
`;

// ✅ BETTER - Using CSS variables for theming
const Button = styled.button`
  background: var(--button-bg);
  color: var(--button-text);
  padding: var(--button-padding);

  &:hover {
    background: var(--button-bg-hover);
  }
`;
```

════════════════════════════════════════════════════════════════════════
  DESIGN TOKENS SYSTEM
════════════════════════════════════════════════════════════════════════

**Complete Design Token Structure:**

```typescript
// design-tokens.ts
export const tokens = {
  colors: {
    // Semantic colors
    primary: {
      DEFAULT: '#3b82f6',
      hover: '#2563eb',
      active: '#1d4ed8',
      foreground: '#ffffff',
    },
    destructive: {
      DEFAULT: '#ef4444',
      hover: '#dc2626',
      foreground: '#ffffff',
    },
    // Primitive colors
    gray: {
      50: '#f9fafb',
      100: '#f3f4f6',
      // ... full scale
      900: '#111827',
    },
  },
  spacing: {
    0: '0',
    1: '0.25rem',  // 4px
    2: '0.5rem',   // 8px
    3: '0.75rem',  // 12px
    4: '1rem',     // 16px
    // ... consistent scale
  },
  typography: {
    fontFamily: {
      sans: 'Inter, system-ui, sans-serif',
      mono: 'JetBrains Mono, monospace',
    },
    fontSize: {
      xs: '0.75rem',   // 12px
      sm: '0.875rem',  // 14px
      base: '1rem',    // 16px
      lg: '1.125rem',  // 18px
      // ... full scale
    },
    fontWeight: {
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
  },
  borderRadius: {
    none: '0',
    sm: '0.125rem',
    DEFAULT: '0.25rem',
    md: '0.375rem',
    lg: '0.5rem',
    full: '9999px',
  },
  shadows: {
    sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    DEFAULT: '0 1px 3px 0 rgb(0 0 0 / 0.1)',
    md: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
    // ... full scale
  },
  animation: {
    duration: {
      instant: '0ms',
      fast: '150ms',
      normal: '300ms',
      slow: '500ms',
    },
    easing: {
      linear: 'linear',
      in: 'cubic-bezier(0.4, 0, 1, 1)',
      out: 'cubic-bezier(0, 0, 0.2, 1)',
      inOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
    },
  },
};

// CSS Variables generation
export const cssVariables = generateCSSVariables(tokens);
```

**Using Design Tokens:**

```css
/* Generated CSS Variables */
:root {
  --color-primary: #3b82f6;
  --color-primary-hover: #2563eb;
  --spacing-4: 1rem;
  --font-size-base: 1rem;
  --radius-md: 0.375rem;
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --duration-normal: 300ms;
  --easing-out: cubic-bezier(0, 0, 0.2, 1);
}

/* Dark mode */
[data-theme="dark"] {
  --color-primary: #60a5fa;
  --color-primary-hover: #93bbfc;
  /* ... dark variants */
}
```

════════════════════════════════════════════════════════════════════════
  RESPONSIVE DESIGN PATTERNS
════════════════════════════════════════════════════════════════════════

**Mobile-First Responsive System:**

```scss
// Breakpoints following design system
$breakpoints: (
  sm: 640px,   // Mobile landscape
  md: 768px,   // Tablet
  lg: 1024px,  // Desktop
  xl: 1280px,  // Large desktop
);

// Responsive mixins
@mixin media-up($breakpoint) {
  @media (min-width: map-get($breakpoints, $breakpoint)) {
    @content;
  }
}

// Container queries for components
.card {
  container-type: inline-size;

  .title {
    font-size: 1rem;
  }

  @container (min-width: 400px) {
    .title {
      font-size: 1.25rem;
    }
  }
}
```

**Fluid Typography:**

```css
/* Fluid type scale */
:root {
  --font-size-sm: clamp(0.875rem, 0.8rem + 0.3vw, 1rem);
  --font-size-base: clamp(1rem, 0.9rem + 0.4vw, 1.125rem);
  --font-size-lg: clamp(1.125rem, 1rem + 0.5vw, 1.5rem);
  --font-size-xl: clamp(1.25rem, 1.1rem + 0.6vw, 2rem);
}
```

════════════════════════════════════════════════════════════════════════
  CSS PERFORMANCE METRICS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Metric                  │ Before   │ After    │ Improvement       │
├────────────────────────────────────────────────────────────────────┤
│ CSS Bundle Size         │ 234 KB   │ 42 KB    │ -82% 🚀          │
│ Unused CSS              │ 67%      │ 8%       │ -88% 🚀          │
│ Parse Time              │ 89ms     │ 12ms     │ -87% 🚀          │
│ Style Recalc            │ 45ms     │ 8ms      │ -82% 🚀          │
│ Layout Thrashing        │ 23 events│ 2 events │ -91% 🚀          │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  CRITICAL CSS EXTRACTION
════════════════════════════════════════════════════════════════════════

```javascript
// next.config.js - Critical CSS
const criticalCSS = {
  // Inline critical CSS
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'Link',
            value: '</styles/critical.css>; rel=preload; as=style',
          },
        ],
      },
    ];
  },
};
```

════════════════════════════════════════════════════════════════════════
  ACTION ITEMS
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL:**
1. Remove 67% unused CSS (-157 KB)
2. Replace arbitrary Tailwind values with config
3. Extract critical CSS for above-fold

**⚠️ HIGH:**
4. Implement design token system
5. Setup PurgeCSS for production
6. Consolidate breakpoints to 3-5

**🟡 MEDIUM:**
7. Convert to CSS modules or styled-components
8. Add CSS linting (Stylelint)
9. Implement container queries

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/css-architect` - Full CSS analysis
• `/css-architect --tailwind` - Tailwind optimization
• `/css-architect --tokens` - Design token audit
• `/css-architect --critical` - Extract critical CSS
• `/css-architect --performance` - Performance analysis

════════════════════════════════════════════════════════════════════════

**SENA 🦁 CSS Architect** - Build scalable, performant styling systems