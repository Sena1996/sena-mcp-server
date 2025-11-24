# Test Generator

**Generate comprehensive test suites with unit, integration, and e2e tests following best practices.**

**IMPORTANT: Create production-ready tests with high coverage and maintainability.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 TEST GENERATOR v3.3                               ║
║       Jest · React Testing Library · Playwright · Coverage           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  TEST COVERAGE ANALYSIS
════════════════════════════════════════════════════════════════════════

**Current Test Coverage:**

┌────────────────────────────────────────────────────────────────────┐
│ Category               │ Coverage │ Target  │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Statements             │ 47.3%    │ > 80%   │ 🔴 Critical         │
│ Branches               │ 34.2%    │ > 80%   │ 🔴 Critical         │
│ Functions              │ 52.8%    │ > 80%   │ 🔴 Needs Work       │
│ Lines                  │ 48.9%    │ > 80%   │ 🔴 Needs Work       │
│ Unit Tests             │ 234      │ -       │ ⚠️ Add More         │
│ Integration Tests      │ 12       │ -       │ 🔴 Too Few          │
│ E2E Tests              │ 3        │ -       │ 🔴 Critical         │
└────────────────────────────────────────────────────────────────────┘

**Uncovered Files:**

┌────────────────────────────────────────────────────────────────────┐
│ File                   │ Coverage │ Missing Tests For             │
├────────────────────────────────────────────────────────────────────┤
│ api/handlers.ts        │ 0%       │ All endpoints                 │
│ hooks/useAuth.ts       │ 12%      │ Login, logout, refresh        │
│ components/DataTable   │ 23%      │ Sorting, filtering, pagination│
│ utils/validation.ts    │ 34%      │ Edge cases, error paths       │
│ services/api-client.ts │ 8%       │ Error handling, retries       │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  UNIT TEST GENERATION
════════════════════════════════════════════════════════════════════════

**Generated Unit Test - React Component:**

```typescript
// Button.test.tsx - Comprehensive unit tests
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Button } from './Button';

describe('Button Component', () => {
  // Setup and teardown
  let user: ReturnType<typeof userEvent.setup>;

  beforeEach(() => {
    user = userEvent.setup();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('Rendering', () => {
    it('renders with text content', () => {
      render(<Button>Click me</Button>);
      expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
    });

    it('renders with correct variant styles', () => {
      const { rerender } = render(<Button variant="primary">Primary</Button>);
      expect(screen.getByRole('button')).toHaveClass('btn-primary');

      rerender(<Button variant="danger">Danger</Button>);
      expect(screen.getByRole('button')).toHaveClass('btn-danger');
    });

    it('renders with icons', () => {
      const StartIcon = () => <span data-testid="start-icon">←</span>;
      const EndIcon = () => <span data-testid="end-icon">→</span>;

      render(
        <Button startIcon={<StartIcon />} endIcon={<EndIcon />}>
          With Icons
        </Button>
      );

      expect(screen.getByTestId('start-icon')).toBeInTheDocument();
      expect(screen.getByTestId('end-icon')).toBeInTheDocument();
    });
  });

  describe('Interactions', () => {
    it('calls onClick when clicked', async () => {
      const handleClick = jest.fn();
      render(<Button onClick={handleClick}>Click</Button>);

      await user.click(screen.getByRole('button'));
      expect(handleClick).toHaveBeenCalledTimes(1);
    });

    it('prevents click when disabled', async () => {
      const handleClick = jest.fn();
      render(<Button disabled onClick={handleClick}>Disabled</Button>);

      await user.click(screen.getByRole('button'));
      expect(handleClick).not.toHaveBeenCalled();
    });

    it('prevents click when loading', async () => {
      const handleClick = jest.fn();
      render(<Button loading onClick={handleClick}>Loading</Button>);

      await user.click(screen.getByRole('button'));
      expect(handleClick).not.toHaveBeenCalled();
    });

    it('handles keyboard navigation', async () => {
      const handleClick = jest.fn();
      render(<Button onClick={handleClick}>Keyboard</Button>);

      const button = screen.getByRole('button');
      button.focus();
      expect(button).toHaveFocus();

      await user.keyboard('{Enter}');
      expect(handleClick).toHaveBeenCalledTimes(1);

      await user.keyboard(' '); // Space key
      expect(handleClick).toHaveBeenCalledTimes(2);
    });
  });

  describe('Accessibility', () => {
    it('has correct ARIA attributes when loading', () => {
      render(<Button loading>Loading</Button>);
      const button = screen.getByRole('button');

      expect(button).toHaveAttribute('aria-busy', 'true');
      expect(button).toHaveAttribute('aria-disabled', 'true');
    });

    it('has correct ARIA attributes when disabled', () => {
      render(<Button disabled>Disabled</Button>);
      expect(screen.getByRole('button')).toHaveAttribute('aria-disabled', 'true');
    });

    it('supports aria-label', () => {
      render(<Button aria-label="Custom label">Icon</Button>);
      expect(screen.getByRole('button', { name: 'Custom label' })).toBeInTheDocument();
    });

    it('announces state changes to screen readers', async () => {
      const { rerender } = render(<Button>Submit</Button>);
      const button = screen.getByRole('button');

      rerender(<Button loading>Submit</Button>);
      expect(button).toHaveAttribute('aria-busy', 'true');

      rerender(<Button disabled>Submit</Button>);
      expect(button).toHaveAttribute('aria-disabled', 'true');
    });
  });

  describe('Edge Cases', () => {
    it('handles rapid clicks', async () => {
      const handleClick = jest.fn();
      render(<Button onClick={handleClick}>Rapid</Button>);

      const button = screen.getByRole('button');
      await user.click(button);
      await user.click(button);
      await user.click(button);

      expect(handleClick).toHaveBeenCalledTimes(3);
    });

    it('handles long text content', () => {
      const longText = 'This is a very long button text that might cause overflow issues';
      render(<Button>{longText}</Button>);

      const button = screen.getByRole('button');
      expect(button).toHaveTextContent(longText);
      expect(button).toHaveStyle({ overflow: 'hidden' });
    });

    it('cleans up event listeners on unmount', () => {
      const { unmount } = render(<Button>Unmount test</Button>);
      const button = screen.getByRole('button');

      const spy = jest.spyOn(button, 'removeEventListener');
      unmount();

      expect(spy).toHaveBeenCalled();
    });
  });

  describe('Snapshot Tests', () => {
    it('matches snapshot for all variants', () => {
      const { container } = render(
        <>
          <Button variant="primary">Primary</Button>
          <Button variant="secondary">Secondary</Button>
          <Button variant="danger">Danger</Button>
        </>
      );

      expect(container).toMatchSnapshot();
    });
  });
});
```

**Generated Unit Test - Custom Hook:**

```typescript
// useApi.test.ts
import { renderHook, act, waitFor } from '@testing-library/react';
import { useApi } from './useApi';
import { apiClient } from '@/lib/api';

jest.mock('@/lib/api');

describe('useApi Hook', () => {
  const mockData = { id: 1, name: 'Test User' };
  const mockError = new Error('API Error');

  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Success Cases', () => {
    it('fetches data successfully', async () => {
      (apiClient.get as jest.Mock).mockResolvedValue(mockData);

      const { result } = renderHook(() =>
        useApi('/users/1')
      );

      // Initial state
      expect(result.current.loading).toBe(true);
      expect(result.current.data).toBe(null);
      expect(result.current.error).toBe(null);

      // After fetch
      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.data).toEqual(mockData);
      expect(result.current.error).toBe(null);
    });

    it('refetches data on demand', async () => {
      (apiClient.get as jest.Mock).mockResolvedValue(mockData);

      const { result } = renderHook(() => useApi('/users/1'));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      // Refetch
      act(() => {
        result.current.refetch();
      });

      expect(result.current.loading).toBe(true);

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(apiClient.get).toHaveBeenCalledTimes(2);
    });
  });

  describe('Error Handling', () => {
    it('handles API errors gracefully', async () => {
      (apiClient.get as jest.Mock).mockRejectedValue(mockError);

      const { result } = renderHook(() => useApi('/users/1'));

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.data).toBe(null);
      expect(result.current.error).toEqual(mockError);
    });

    it('retries on failure when configured', async () => {
      (apiClient.get as jest.Mock)
        .mockRejectedValueOnce(mockError)
        .mockResolvedValueOnce(mockData);

      const { result } = renderHook(() =>
        useApi('/users/1', { retry: true, retryCount: 2 })
      );

      await waitFor(() => {
        expect(result.current.loading).toBe(false);
      });

      expect(result.current.data).toEqual(mockData);
      expect(apiClient.get).toHaveBeenCalledTimes(2);
    });
  });

  describe('Caching', () => {
    it('uses cached data when available', async () => {
      (apiClient.get as jest.Mock).mockResolvedValue(mockData);

      const { result: result1 } = renderHook(() =>
        useApi('/users/1', { cache: true })
      );

      await waitFor(() => {
        expect(result1.current.data).toEqual(mockData);
      });

      // Second hook should use cache
      const { result: result2 } = renderHook(() =>
        useApi('/users/1', { cache: true })
      );

      expect(result2.current.data).toEqual(mockData);
      expect(result2.current.loading).toBe(false);
      expect(apiClient.get).toHaveBeenCalledTimes(1); // Not called again
    });
  });
});
```

════════════════════════════════════════════════════════════════════════
  INTEGRATION TEST GENERATION
════════════════════════════════════════════════════════════════════════

**Generated Integration Test - API Routes:**

```typescript
// api/users.integration.test.ts
import { createMocks } from 'node-mocks-http';
import { GET, POST, PUT, DELETE } from '@/app/api/users/route';
import { prisma } from '@/lib/prisma';

// Mock Prisma
jest.mock('@/lib/prisma', () => ({
  prisma: {
    user: {
      findMany: jest.fn(),
      findUnique: jest.fn(),
      create: jest.fn(),
      update: jest.fn(),
      delete: jest.fn(),
    },
  },
}));

describe('Users API Integration', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('GET /api/users', () => {
    it('returns paginated users list', async () => {
      const mockUsers = [
        { id: '1', name: 'User 1', email: 'user1@test.com' },
        { id: '2', name: 'User 2', email: 'user2@test.com' },
      ];

      (prisma.user.findMany as jest.Mock).mockResolvedValue(mockUsers);
      (prisma.user.count as jest.Mock).mockResolvedValue(50);

      const { req } = createMocks({
        method: 'GET',
        query: { page: '1', limit: '10' },
      });

      const response = await GET(req as any);
      const data = await response.json();

      expect(response.status).toBe(200);
      expect(data).toMatchObject({
        data: mockUsers,
        pagination: {
          page: 1,
          limit: 10,
          total: 50,
          totalPages: 5,
        },
      });

      expect(prisma.user.findMany).toHaveBeenCalledWith({
        skip: 0,
        take: 10,
      });
    });

    it('handles database errors', async () => {
      (prisma.user.findMany as jest.Mock).mockRejectedValue(
        new Error('Database connection failed')
      );

      const { req } = createMocks({ method: 'GET' });
      const response = await GET(req as any);
      const data = await response.json();

      expect(response.status).toBe(500);
      expect(data).toMatchObject({
        error: {
          code: 'INTERNAL_SERVER_ERROR',
          message: expect.any(String),
        },
      });
    });
  });

  describe('POST /api/users', () => {
    it('creates new user with validation', async () => {
      const newUser = {
        name: 'New User',
        email: 'new@test.com',
        role: 'user',
      };

      const createdUser = { id: '123', ...newUser };

      (prisma.user.findUnique as jest.Mock).mockResolvedValue(null);
      (prisma.user.create as jest.Mock).mockResolvedValue(createdUser);

      const { req } = createMocks({
        method: 'POST',
        body: newUser,
      });

      const response = await POST(req as any);
      const data = await response.json();

      expect(response.status).toBe(201);
      expect(data).toEqual(createdUser);
      expect(response.headers.get('Location')).toBe('/api/users/123');
    });

    it('validates required fields', async () => {
      const invalidUser = { name: 'Test' }; // Missing email

      const { req } = createMocks({
        method: 'POST',
        body: invalidUser,
      });

      const response = await POST(req as any);
      const data = await response.json();

      expect(response.status).toBe(400);
      expect(data.error.code).toBe('VALIDATION_ERROR');
      expect(data.error.details).toContainEqual(
        expect.objectContaining({
          path: ['email'],
          message: expect.any(String),
        })
      );
    });

    it('prevents duplicate emails', async () => {
      const existingUser = { id: '1', email: 'existing@test.com' };
      (prisma.user.findUnique as jest.Mock).mockResolvedValue(existingUser);

      const { req } = createMocks({
        method: 'POST',
        body: { name: 'Test', email: 'existing@test.com' },
      });

      const response = await POST(req as any);
      const data = await response.json();

      expect(response.status).toBe(409); // Conflict
      expect(data.error.code).toBe('DUPLICATE_EMAIL');
    });
  });
});
```

════════════════════════════════════════════════════════════════════════
  E2E TEST GENERATION
════════════════════════════════════════════════════════════════════════

**Generated E2E Test - Playwright:**

```typescript
// e2e/user-flow.spec.ts
import { test, expect } from '@playwright/test';

test.describe('User Registration Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/');
  });

  test('complete user registration journey', async ({ page }) => {
    // Navigate to registration
    await page.click('text=Sign Up');
    await expect(page).toHaveURL('/register');

    // Fill registration form
    await page.fill('[name="name"]', 'Test User');
    await page.fill('[name="email"]', 'test@example.com');
    await page.fill('[name="password"]', 'SecurePassword123!');
    await page.fill('[name="confirmPassword"]', 'SecurePassword123!');

    // Accept terms
    await page.check('[name="terms"]');

    // Submit form
    await page.click('button[type="submit"]');

    // Wait for redirect
    await page.waitForURL('/dashboard');

    // Verify welcome message
    await expect(page.locator('h1')).toContainText('Welcome, Test User');

    // Verify user menu
    await page.click('[data-testid="user-menu"]');
    await expect(page.locator('[data-testid="user-email"]')).toContainText('test@example.com');
  });

  test('handles validation errors', async ({ page }) => {
    await page.click('text=Sign Up');

    // Submit empty form
    await page.click('button[type="submit"]');

    // Check validation messages
    await expect(page.locator('text=Name is required')).toBeVisible();
    await expect(page.locator('text=Email is required')).toBeVisible();
    await expect(page.locator('text=Password is required')).toBeVisible();

    // Test invalid email
    await page.fill('[name="email"]', 'invalid-email');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Invalid email address')).toBeVisible();

    // Test password mismatch
    await page.fill('[name="password"]', 'Password123');
    await page.fill('[name="confirmPassword"]', 'DifferentPassword');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Passwords do not match')).toBeVisible();
  });

  test('responsive design on mobile', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });

    await page.goto('/register');

    // Check mobile menu
    await expect(page.locator('[data-testid="mobile-menu"]')).toBeVisible();
    await expect(page.locator('[data-testid="desktop-menu"]')).not.toBeVisible();

    // Check form is still usable
    await page.fill('[name="email"]', 'mobile@test.com');

    // Touch targets should be large enough
    const submitButton = page.locator('button[type="submit"]');
    const box = await submitButton.boundingBox();
    expect(box?.width).toBeGreaterThanOrEqual(44);
    expect(box?.height).toBeGreaterThanOrEqual(44);
  });

  test('accessibility compliance', async ({ page }) => {
    await page.goto('/register');

    // Check for accessibility violations
    const accessibilityScanResults = await page.evaluate(() => {
      // This would use axe-core in real implementation
      return {
        violations: [],
      };
    });

    expect(accessibilityScanResults.violations).toHaveLength(0);

    // Keyboard navigation
    await page.keyboard.press('Tab');
    await expect(page.locator('[name="name"]')).toBeFocused();

    await page.keyboard.press('Tab');
    await expect(page.locator('[name="email"]')).toBeFocused();

    // Screen reader labels
    await expect(page.locator('[name="email"]')).toHaveAttribute('aria-label', 'Email address');
    await expect(page.locator('[name="password"]')).toHaveAttribute('aria-label', 'Password');
  });

  test('performance metrics', async ({ page }) => {
    const metrics = await page.evaluate(() => {
      return JSON.stringify(performance.getEntriesByType('navigation'));
    });

    const navigation = JSON.parse(metrics)[0];

    // Check key performance metrics
    expect(navigation.domContentLoadedEventEnd).toBeLessThan(3000);
    expect(navigation.loadEventEnd).toBeLessThan(5000);
  });
});
```

════════════════════════════════════════════════════════════════════════
  TEST UTILITIES GENERATION
════════════════════════════════════════════════════════════════════════

**Test Helpers & Utilities:**

```typescript
// test-utils/render.tsx
import { render as rtlRender } from '@testing-library/react';
import { Provider } from 'react-redux';
import { ThemeProvider } from '@/contexts/ThemeContext';
import { AuthProvider } from '@/contexts/AuthContext';

function render(
  ui: React.ReactElement,
  {
    preloadedState,
    store = configureStore({ reducer, preloadedState }),
    ...renderOptions
  } = {}
) {
  function Wrapper({ children }: { children: React.ReactNode }) {
    return (
      <Provider store={store}>
        <ThemeProvider>
          <AuthProvider>
            {children}
          </AuthProvider>
        </ThemeProvider>
      </Provider>
    );
  }

  return rtlRender(ui, { wrapper: Wrapper, ...renderOptions });
}

// test-utils/factories.ts
export const userFactory = (overrides = {}) => ({
  id: faker.datatype.uuid(),
  name: faker.name.fullName(),
  email: faker.internet.email(),
  createdAt: faker.date.recent(),
  ...overrides,
});

// test-utils/mocks.ts
export const mockApiResponse = (data: any, status = 200) => {
  return jest.fn().mockResolvedValue({
    status,
    json: async () => data,
  });
};

// test-utils/assertions.ts
export const expectToBeAccessible = async (container: HTMLElement) => {
  const results = await axe(container);
  expect(results).toHaveNoViolations();
};
```

════════════════════════════════════════════════════════════════════════
  TEST CONFIGURATION
════════════════════════════════════════════════════════════════════════

**Generated Jest Configuration:**

```javascript
// jest.config.js
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
  },
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.stories.tsx',
    '!src/**/index.ts',
  ],
  coverageThresholds: {
    global: {
      statements: 80,
      branches: 80,
      functions: 80,
      lines: 80,
    },
  },
  testMatch: [
    '**/__tests__/**/*.ts?(x)',
    '**/?(*.)+(spec|test).ts?(x)',
  ],
};
```

════════════════════════════════════════════════════════════════════════
  TEST QUALITY METRICS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Metric                  │ Before  │ After   │ Improvement        │
├────────────────────────────────────────────────────────────────────┤
│ Code Coverage           │ 47%     │ 88%     │ +41% 🚀           │
│ Test Count              │ 249     │ 847     │ +240% 🚀          │
│ E2E Coverage            │ 3       │ 25      │ +733% 🚀          │
│ Test Execution Time     │ 45s     │ 12s     │ -73% 🚀           │
│ Flaky Tests             │ 12      │ 0       │ -100% 🚀          │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/test-generator <component>` - Generate tests for component
• `/test-generator --unit` - Generate unit tests
• `/test-generator --integration` - Generate integration tests
• `/test-generator --e2e` - Generate E2E tests
• `/test-generator --coverage` - Analyze test coverage
• `/test-generator --missing` - Find untested code

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Test Generator** - Ship with confidence, 80%+ coverage guaranteed