# Component Generator

**Generate React components with TypeScript, tests, stories, and best practices built-in.**

**IMPORTANT: Generate production-ready component code following atomic design principles.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 COMPONENT GENERATOR v3.3                          ║
║     React · TypeScript · Tests · Stories · Atomic Design             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  COMPONENT TEMPLATES
════════════════════════════════════════════════════════════════════════

**Available Component Types:**

┌────────────────────────────────────────────────────────────────────┐
│ Type                    │ Use Case           │ Files Generated      │
├────────────────────────────────────────────────────────────────────┤
│ Atom                    │ Button, Input      │ 5 files             │
│ Molecule                │ SearchBar, Card    │ 6 files             │
│ Organism                │ Header, Form       │ 7 files             │
│ Template                │ Layout, Grid       │ 6 files             │
│ Page                    │ Dashboard, Profile │ 8 files             │
│ Hook                    │ useApi, useForm    │ 4 files             │
│ Context                 │ Theme, Auth        │ 5 files             │
│ HOC                     │ withAuth, withData │ 4 files             │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  EXAMPLE: GENERATE BUTTON COMPONENT
════════════════════════════════════════════════════════════════════════

**Command:** `/component-generator Button --atom`

**Generated Structure:**
```
src/components/atoms/Button/
├── Button.tsx           // Component
├── Button.types.ts      // TypeScript interfaces
├── Button.styles.ts     // Styled components/CSS
├── Button.test.tsx      // Unit tests
├── Button.stories.tsx   // Storybook stories
└── index.ts            // Barrel export
```

**Button.tsx:**
```tsx
import React, { FC, memo } from 'react';
import { ButtonProps } from './Button.types';
import { StyledButton } from './Button.styles';

/**
 * Button component following design system guidelines
 * @component
 * @example
 * <Button variant="primary" size="medium" onClick={handleClick}>
 *   Click Me
 * </Button>
 */
export const Button: FC<ButtonProps> = memo(({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  loading = false,
  fullWidth = false,
  startIcon,
  endIcon,
  onClick,
  type = 'button',
  className,
  'aria-label': ariaLabel,
  ...rest
}) => {
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    if (!disabled && !loading && onClick) {
      onClick(e);
    }
  };

  return (
    <StyledButton
      variant={variant}
      size={size}
      disabled={disabled || loading}
      fullWidth={fullWidth}
      onClick={handleClick}
      type={type}
      className={className}
      aria-label={ariaLabel || (typeof children === 'string' ? children : undefined)}
      aria-busy={loading}
      aria-disabled={disabled}
      {...rest}
    >
      {loading && <Spinner size="small" />}
      {startIcon && <IconWrapper position="start">{startIcon}</IconWrapper>}
      <ButtonContent>{children}</ButtonContent>
      {endIcon && <IconWrapper position="end">{endIcon}</IconWrapper>}
    </StyledButton>
  );
});

Button.displayName = 'Button';

export default Button;
```

**Button.types.ts:**
```tsx
import { ReactNode, MouseEvent, ButtonHTMLAttributes } from 'react';

export type ButtonVariant = 'primary' | 'secondary' | 'tertiary' | 'danger' | 'ghost';
export type ButtonSize = 'small' | 'medium' | 'large';

export interface ButtonProps extends Omit<ButtonHTMLAttributes<HTMLButtonElement>, 'type'> {
  /** Button content */
  children: ReactNode;
  /** Visual style variant */
  variant?: ButtonVariant;
  /** Button size */
  size?: ButtonSize;
  /** Disabled state */
  disabled?: boolean;
  /** Loading state with spinner */
  loading?: boolean;
  /** Full width button */
  fullWidth?: boolean;
  /** Icon before text */
  startIcon?: ReactNode;
  /** Icon after text */
  endIcon?: ReactNode;
  /** Click handler */
  onClick?: (e: MouseEvent<HTMLButtonElement>) => void;
  /** HTML button type */
  type?: 'button' | 'submit' | 'reset';
  /** Accessible label */
  'aria-label'?: string;
}
```

**Button.test.tsx:**
```tsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button Component', () => {
  it('renders with children', () => {
    render(<Button>Click Me</Button>);
    expect(screen.getByText('Click Me')).toBeInTheDocument();
  });

  it('handles click events', async () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click</Button>);

    await userEvent.click(screen.getByText('Click'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('prevents click when disabled', async () => {
    const handleClick = jest.fn();
    render(<Button disabled onClick={handleClick}>Click</Button>);

    await userEvent.click(screen.getByText('Click'));
    expect(handleClick).not.toHaveBeenCalled();
  });

  it('shows loading spinner', () => {
    render(<Button loading>Loading</Button>);
    expect(screen.getByLabelText('Loading')).toHaveAttribute('aria-busy', 'true');
  });

  it('applies correct variant styles', () => {
    const { rerender } = render(<Button variant="primary">Primary</Button>);
    expect(screen.getByText('Primary')).toHaveClass('variant-primary');

    rerender(<Button variant="danger">Danger</Button>);
    expect(screen.getByText('Danger')).toHaveClass('variant-danger');
  });

  it('renders with icons', () => {
    const StartIcon = () => <span>👈</span>;
    const EndIcon = () => <span>👉</span>;

    render(
      <Button startIcon={<StartIcon />} endIcon={<EndIcon />}>
        With Icons
      </Button>
    );

    expect(screen.getByText('👈')).toBeInTheDocument();
    expect(screen.getByText('👉')).toBeInTheDocument();
  });
});
```

**Button.stories.tsx:**
```tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta = {
  title: 'Atoms/Button',
  component: Button,
  parameters: {
    layout: 'centered',
    docs: {
      description: {
        component: 'Base button component with multiple variants and states',
      },
    },
  },
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'tertiary', 'danger', 'ghost'],
    },
    size: {
      control: 'select',
      options: ['small', 'medium', 'large'],
    },
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: {
    children: 'Primary Button',
    variant: 'primary',
  },
};

export const Secondary: Story = {
  args: {
    children: 'Secondary Button',
    variant: 'secondary',
  },
};

export const WithIcons: Story = {
  args: {
    children: 'With Icons',
    startIcon: <span>🚀</span>,
    endIcon: <span>→</span>,
  },
};

export const Loading: Story = {
  args: {
    children: 'Loading...',
    loading: true,
  },
};

export const Disabled: Story = {
  args: {
    children: 'Disabled',
    disabled: true,
  },
};

export const AllVariants: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="tertiary">Tertiary</Button>
      <Button variant="danger">Danger</Button>
      <Button variant="ghost">Ghost</Button>
    </div>
  ),
};

export const AllSizes: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
      <Button size="small">Small</Button>
      <Button size="medium">Medium</Button>
      <Button size="large">Large</Button>
    </div>
  ),
};
```

════════════════════════════════════════════════════════════════════════
  ADVANCED COMPONENT TEMPLATES
════════════════════════════════════════════════════════════════════════

**Form Component with Validation:**

```tsx
// Generated with: /component-generator ContactForm --organism --with-validation

export const ContactForm: FC<ContactFormProps> = ({
  onSubmit,
  initialValues,
}) => {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm<FormData>({
    resolver: zodResolver(contactSchema),
    defaultValues: initialValues,
  });

  return (
    <StyledForm onSubmit={handleSubmit(onSubmit)}>
      <FormField>
        <Label htmlFor="name">Name</Label>
        <Input
          id="name"
          {...register('name')}
          error={!!errors.name}
          aria-describedby="name-error"
        />
        {errors.name && (
          <ErrorMessage id="name-error">{errors.name.message}</ErrorMessage>
        )}
      </FormField>

      {/* More fields... */}

      <Button type="submit" loading={isSubmitting}>
        Submit
      </Button>
    </StyledForm>
  );
};
```

**Data Table Component:**

```tsx
// Generated with: /component-generator DataTable --organism --generic

export function DataTable<T extends Record<string, any>>({
  data,
  columns,
  onSort,
  onFilter,
  onPaginate,
  loading,
}: DataTableProps<T>) {
  // Implementation with sorting, filtering, pagination
}
```

════════════════════════════════════════════════════════════════════════
  CUSTOM HOOKS GENERATOR
════════════════════════════════════════════════════════════════════════

**Generate Custom Hook:** `/component-generator useApi --hook`

```tsx
// Generated useApi.ts
import { useState, useEffect, useCallback } from 'react';
import { AxiosError } from 'axios';

interface UseApiOptions {
  immediate?: boolean;
  onSuccess?: (data: any) => void;
  onError?: (error: AxiosError) => void;
}

export function useApi<T = any>(
  apiFunc: () => Promise<T>,
  options: UseApiOptions = {}
) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<AxiosError | null>(null);

  const execute = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const result = await apiFunc();
      setData(result);
      options.onSuccess?.(result);
      return result;
    } catch (err) {
      const axiosError = err as AxiosError;
      setError(axiosError);
      options.onError?.(axiosError);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [apiFunc]);

  useEffect(() => {
    if (options.immediate) {
      execute();
    }
  }, []);

  return { data, loading, error, execute, refetch: execute };
}
```

════════════════════════════════════════════════════════════════════════
  GENERATION OPTIONS
════════════════════════════════════════════════════════════════════════

**Command Flags:**

```bash
# Basic generation
/component-generator Button --atom

# With specific features
/component-generator Card --molecule --with-animation
/component-generator Form --organism --with-validation
/component-generator Dashboard --page --with-auth

# Custom styling
/component-generator Header --styled-components
/component-generator Footer --css-modules
/component-generator Nav --tailwind

# Testing options
/component-generator Table --with-e2e
/component-generator Modal --with-a11y-tests

# Advanced patterns
/component-generator DataGrid --generic
/component-generator AuthProvider --context
/component-generator withAnalytics --hoc
```

**Configuration Options:**

┌────────────────────────────────────────────────────────────────────┐
│ Flag                    │ Description                              │
├────────────────────────────────────────────────────────────────────┤
│ --atom/molecule/etc     │ Atomic design level                     │
│ --with-validation       │ Add form validation (react-hook-form)   │
│ --with-animation        │ Add Framer Motion animations            │
│ --with-auth            │ Add authentication checks                │
│ --generic              │ Make component generic <T>               │
│ --styled-components    │ Use styled-components                    │
│ --css-modules          │ Use CSS Modules                          │
│ --tailwind            │ Use Tailwind CSS                         │
│ --with-e2e            │ Add Playwright tests                     │
│ --with-a11y-tests     │ Add accessibility tests                  │
│ --memo                │ Wrap in React.memo                       │
│ --forward-ref         │ Use forwardRef                           │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  FOLDER STRUCTURE PATTERNS
════════════════════════════════════════════════════════════════════════

**Feature-First Structure (Recommended):**
```
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── types/
│   └── dashboard/
│       ├── components/
│       ├── hooks/
│       └── pages/
├── shared/
│   ├── components/
│   ├── hooks/
│   └── utils/
```

**Atomic Design Structure:**
```
src/
├── components/
│   ├── atoms/
│   ├── molecules/
│   ├── organisms/
│   ├── templates/
│   └── pages/
```

════════════════════════════════════════════════════════════════════════
  BEST PRACTICES ENFORCED
════════════════════════════════════════════════════════════════════════

✅ **Always Included:**
- TypeScript interfaces
- Props documentation
- Display name for debugging
- Memoization where appropriate
- Accessibility attributes
- Error boundaries (for pages)
- Loading states
- Error states

✅ **Testing Coverage:**
- Unit tests with RTL
- User interaction tests
- Accessibility tests
- Snapshot tests (optional)
- Visual regression (Storybook)

✅ **Documentation:**
- JSDoc comments
- Storybook stories
- Usage examples
- Props table
- Design tokens

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/component-generator <name> --type` - Generate component
• `/component-generator --list` - List all templates
• `/component-generator --config` - Configure defaults
• `/component-generator --preview <name>` - Preview before generating

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Component Generator** - Production-ready components in seconds