# Design System Manager

**Manage design tokens, component library, and ensure design consistency across the application.**

**IMPORTANT: Create and maintain a scalable design system with automated documentation.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 DESIGN SYSTEM MANAGER v3.3                        ║
║       Tokens · Components · Patterns · Documentation                 ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  DESIGN SYSTEM OVERVIEW
════════════════════════════════════════════════════════════════════════

**System Health Score: 58/100** ⚠️

┌────────────────────────────────────────────────────────────────────┐
│ Aspect                  │ Status  │ Coverage │ Issues              │
├────────────────────────────────────────────────────────────────────┤
│ Design Tokens           │ ⚠️      │ 45%      │ Inconsistent usage  │
│ Component Library       │ 🔴      │ 23%      │ No documentation    │
│ Pattern Consistency     │ 🔴      │ 34%      │ Multiple variants   │
│ Accessibility           │ ⚠️      │ 67%      │ Missing ARIA        │
│ Documentation           │ 🔴      │ 12%      │ Outdated            │
│ Theme Support           │ ✅      │ 89%      │ Good                │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  DESIGN TOKENS ARCHITECTURE
════════════════════════════════════════════════════════════════════════

**Token Structure (Generated):**

```typescript
// design-tokens.ts
export const tokens = {
  // Color Primitives
  colors: {
    blue: {
      50: '#eff6ff',
      100: '#dbeafe',
      200: '#bfdbfe',
      300: '#93c5fd',
      400: '#60a5fa',
      500: '#3b82f6',
      600: '#2563eb',
      700: '#1d4ed8',
      800: '#1e40af',
      900: '#1e3a8a',
    },
    // Semantic Tokens
    semantic: {
      primary: '$colors.blue.500',
      primaryHover: '$colors.blue.600',
      success: '$colors.green.500',
      warning: '$colors.yellow.500',
      error: '$colors.red.500',
      background: '$colors.white',
      surface: '$colors.gray.50',
      text: '$colors.gray.900',
      textMuted: '$colors.gray.500',
      border: '$colors.gray.200',
    }
  },

  // Typography System
  typography: {
    fonts: {
      sans: 'Inter, system-ui, -apple-system, sans-serif',
      mono: 'JetBrains Mono, Menlo, monospace',
    },
    sizes: {
      xs: '0.75rem',    // 12px
      sm: '0.875rem',   // 14px
      base: '1rem',     // 16px
      lg: '1.125rem',   // 18px
      xl: '1.25rem',    // 20px
      '2xl': '1.5rem',  // 24px
      '3xl': '1.875rem',// 30px
      '4xl': '2.25rem', // 36px
      '5xl': '3rem',    // 48px
    },
    weights: {
      thin: 100,
      light: 300,
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
      black: 900,
    },
    lineHeights: {
      tight: 1.25,
      snug: 1.375,
      normal: 1.5,
      relaxed: 1.625,
      loose: 2,
    },
  },

  // Spacing Scale
  spacing: {
    0: '0',
    px: '1px',
    0.5: '0.125rem',  // 2px
    1: '0.25rem',     // 4px
    2: '0.5rem',      // 8px
    3: '0.75rem',     // 12px
    4: '1rem',        // 16px
    5: '1.25rem',     // 20px
    6: '1.5rem',      // 24px
    8: '2rem',        // 32px
    10: '2.5rem',     // 40px
    12: '3rem',       // 48px
    16: '4rem',       // 64px
    20: '5rem',       // 80px
    24: '6rem',       // 96px
  },

  // Component Tokens
  components: {
    button: {
      padding: {
        sm: '$spacing.2 $spacing.3',
        md: '$spacing.2 $spacing.4',
        lg: '$spacing.3 $spacing.6',
      },
      borderRadius: '$radii.md',
      fontSize: {
        sm: '$typography.sizes.sm',
        md: '$typography.sizes.base',
        lg: '$typography.sizes.lg',
      },
    },
    input: {
      padding: '$spacing.2 $spacing.3',
      borderRadius: '$radii.md',
      borderColor: '$colors.semantic.border',
      focusColor: '$colors.semantic.primary',
    },
  },
};

// Token to CSS Variables
export function generateCSSVariables(tokens: any, prefix = ''): string {
  let css = ':root {\n';

  function traverse(obj: any, path: string) {
    for (const [key, value] of Object.entries(obj)) {
      const varName = `--${path}${path ? '-' : ''}${key}`;
      if (typeof value === 'object') {
        traverse(value, `${path}${path ? '-' : ''}${key}`);
      } else {
        css += `  ${varName}: ${value};\n`;
      }
    }
  }

  traverse(tokens, prefix);
  css += '}\n';
  return css;
}
```

════════════════════════════════════════════════════════════════════════
  COMPONENT LIBRARY STATUS
════════════════════════════════════════════════════════════════════════

**Component Inventory:**

┌────────────────────────────────────────────────────────────────────┐
│ Component          │ Variants │ States │ Docs │ Tests │ A11y      │
├────────────────────────────────────────────────────────────────────┤
│ Button             │ 5        │ 4      │ ✅   │ ✅    │ ✅        │
│ Input              │ 3        │ 5      │ ❌   │ ⚠️    │ ⚠️        │
│ Select             │ 2        │ 4      │ ❌   │ ❌    │ 🔴        │
│ Modal              │ 3        │ 2      │ ⚠️   │ ✅    │ ✅        │
│ Card               │ 4        │ 1      │ ❌   │ ❌    │ ✅        │
│ Table              │ 2        │ 3      │ ❌   │ ⚠️    │ 🔴        │
│ Navigation         │ 2        │ 2      │ ❌   │ ❌    │ ⚠️        │
│ Tooltip            │ 1        │ 2      │ ✅   │ ✅    │ ✅        │
│ Badge              │ 5        │ 1      │ ❌   │ ❌    │ ✅        │
│ Alert              │ 4        │ 1      │ ⚠️   │ ✅    │ ✅        │
└────────────────────────────────────────────────────────────────────┘

**Component Template Generator:**

```typescript
// Generated Component with Design System
import { styled } from '@/design-system';
import { tokens } from '@/design-system/tokens';

const StyledButton = styled('button', {
  // Base styles from tokens
  padding: tokens.components.button.padding.md,
  borderRadius: tokens.components.button.borderRadius,
  fontSize: tokens.components.button.fontSize.md,
  fontWeight: tokens.typography.weights.medium,
  transition: 'all 0.2s',

  // Variants
  variants: {
    variant: {
      primary: {
        backgroundColor: tokens.colors.semantic.primary,
        color: 'white',
        '&:hover': {
          backgroundColor: tokens.colors.semantic.primaryHover,
        },
      },
      secondary: {
        backgroundColor: 'transparent',
        color: tokens.colors.semantic.primary,
        border: `2px solid ${tokens.colors.semantic.primary}`,
      },
    },
    size: {
      sm: {
        padding: tokens.components.button.padding.sm,
        fontSize: tokens.components.button.fontSize.sm,
      },
      lg: {
        padding: tokens.components.button.padding.lg,
        fontSize: tokens.components.button.fontSize.lg,
      },
    },
  },
});
```

════════════════════════════════════════════════════════════════════════
  PATTERN LIBRARY
════════════════════════════════════════════════════════════════════════

**UI Patterns Catalog:**

┌────────────────────────────────────────────────────────────────────┐
│ Pattern                 │ Usage    │ Consistency │ Documentation   │
├────────────────────────────────────────────────────────────────────┤
│ Form Validation         │ 23 files │ 45%         │ ❌ Missing      │
│ Loading States          │ 34 files │ 67%         │ ⚠️ Partial      │
│ Error Handling          │ 45 files │ 23%         │ 🔴 Inconsistent │
│ Empty States            │ 12 files │ 78%         │ ✅ Good         │
│ Data Tables             │ 8 files  │ 34%         │ 🔴 Various      │
│ Navigation Patterns     │ 5 files  │ 89%         │ ✅ Consistent   │
│ Modal Dialogs           │ 15 files │ 56%         │ ⚠️ Mixed        │
│ Toast Notifications     │ 9 files  │ 91%         │ ✅ Good         │
└────────────────────────────────────────────────────────────────────┘

**Pattern Implementation:**

```typescript
// Consistent Loading Pattern
export const LoadingPattern = {
  skeleton: () => (
    <div className="animate-pulse">
      <div className="h-4 bg-gray-200 rounded w-3/4 mb-2" />
      <div className="h-4 bg-gray-200 rounded w-1/2" />
    </div>
  ),

  spinner: () => (
    <div className="flex items-center justify-center p-4">
      <Spinner size="md" />
      <span className="ml-2 text-gray-500">Loading...</span>
    </div>
  ),

  overlay: () => (
    <div className="absolute inset-0 bg-white/80 flex items-center justify-center">
      <Spinner size="lg" />
    </div>
  ),
};

// Consistent Error Pattern
export const ErrorPattern = {
  inline: ({ error }) => (
    <div className="text-red-600 text-sm mt-1">{error}</div>
  ),

  banner: ({ error, onDismiss }) => (
    <Alert variant="error" dismissible onDismiss={onDismiss}>
      {error}
    </Alert>
  ),

  fullPage: ({ error, onRetry }) => (
    <div className="flex flex-col items-center justify-center min-h-[400px]">
      <Icon name="error" className="text-red-500 w-16 h-16 mb-4" />
      <h2 className="text-xl font-semibold mb-2">Something went wrong</h2>
      <p className="text-gray-600 mb-4">{error}</p>
      <Button onClick={onRetry}>Try Again</Button>
    </div>
  ),
};
```

════════════════════════════════════════════════════════════════════════
  ACCESSIBILITY AUDIT
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ WCAG Criterion         │ Pass │ Fail │ N/A │ Compliance          │
├────────────────────────────────────────────────────────────────────┤
│ Color Contrast (AA)    │ 67%  │ 33%  │ 0%  │ ⚠️ Needs Work       │
│ Keyboard Navigation    │ 78%  │ 22%  │ 0%  │ ⚠️ Good            │
│ Screen Reader Support  │ 45%  │ 55%  │ 0%  │ 🔴 Critical         │
│ Focus Indicators       │ 56%  │ 44%  │ 0%  │ ⚠️ Improve         │
│ ARIA Labels            │ 34%  │ 66%  │ 0%  │ 🔴 Many Missing     │
│ Touch Targets          │ 89%  │ 11%  │ 0%  │ ✅ Good            │
└────────────────────────────────────────────────────────────────────┘

**Accessibility Fixes:**

```typescript
// ✅ Accessible Component Template
export const AccessibleButton = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ children, label, ...props }, ref) => {
    return (
      <button
        ref={ref}
        aria-label={label || (typeof children === 'string' ? children : undefined)}
        aria-pressed={props.pressed}
        aria-disabled={props.disabled}
        {...props}
      >
        {children}
      </button>
    );
  }
);

// Focus Management
export const useFocusTrap = (ref: RefObject<HTMLElement>) => {
  useEffect(() => {
    const element = ref.current;
    if (!element) return;

    const focusableElements = element.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );

    const firstElement = focusableElements[0] as HTMLElement;
    const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

    const handleTab = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;

      if (e.shiftKey && document.activeElement === firstElement) {
        lastElement.focus();
        e.preventDefault();
      } else if (!e.shiftKey && document.activeElement === lastElement) {
        firstElement.focus();
        e.preventDefault();
      }
    };

    element.addEventListener('keydown', handleTab);
    return () => element.removeEventListener('keydown', handleTab);
  }, [ref]);
};
```

════════════════════════════════════════════════════════════════════════
  THEME MANAGEMENT
════════════════════════════════════════════════════════════════════════

**Theme Configuration:**

```typescript
// theme.config.ts
export const themes = {
  light: {
    colors: {
      background: '#ffffff',
      foreground: '#000000',
      primary: '#3b82f6',
      // ... rest of light theme
    },
  },
  dark: {
    colors: {
      background: '#0a0a0a',
      foreground: '#ffffff',
      primary: '#60a5fa',
      // ... rest of dark theme
    },
  },
};

// Theme Provider
export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');

  useEffect(() => {
    const root = document.documentElement;
    Object.entries(themes[theme].colors).forEach(([key, value]) => {
      root.style.setProperty(`--color-${key}`, value);
    });
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
```

════════════════════════════════════════════════════════════════════════
  AUTO-GENERATED DOCUMENTATION
════════════════════════════════════════════════════════════════════════

**Storybook Configuration:**

```typescript
// Generated stories for all components
export default {
  title: 'Design System/Button',
  component: Button,
  parameters: {
    docs: {
      description: {
        component: 'Base button component with multiple variants',
      },
    },
  },
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'danger'],
      description: 'Visual style variant',
    },
    size: {
      control: 'radio',
      options: ['sm', 'md', 'lg'],
      description: 'Button size',
    },
  },
};

// Auto-generate all variant combinations
const variants = ['primary', 'secondary', 'danger'];
const sizes = ['sm', 'md', 'lg'];

export const AllVariants = () => (
  <div className="grid gap-4">
    {variants.map(variant => (
      <div key={variant} className="flex gap-2">
        {sizes.map(size => (
          <Button key={size} variant={variant} size={size}>
            {variant} {size}
          </Button>
        ))}
      </div>
    ))}
  </div>
);
```

════════════════════════════════════════════════════════════════════════
  DESIGN SYSTEM METRICS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Current │ Target  │ Progress            │
├────────────────────────────────────────────────────────────────────┤
│ Token Adoption         │ 45%     │ 100%    │ ████████░░░░░░░░░  │
│ Component Coverage     │ 23%     │ 80%     │ ████░░░░░░░░░░░░░  │
│ Pattern Consistency    │ 34%     │ 90%     │ ██████░░░░░░░░░░░  │
│ Documentation          │ 12%     │ 100%    │ ██░░░░░░░░░░░░░░░  │
│ Accessibility          │ 67%     │ 100%    │ █████████████░░░░  │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/design-system` - Full design system audit
• `/design-system --tokens` - Generate design tokens
• `/design-system --components` - Component library status
• `/design-system --patterns` - UI pattern analysis
• `/design-system --docs` - Generate documentation
• `/design-system --a11y` - Accessibility audit

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Design System Manager** - Consistent, scalable, beautiful UIs