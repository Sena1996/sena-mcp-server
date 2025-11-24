# TypeScript Guardian

**Enforce TypeScript best practices, eliminate 'any' types, and maximize type safety.**

**IMPORTANT: Provide comprehensive TypeScript analysis with actionable improvements.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 TYPESCRIPT GUARDIAN v3.3                          ║
║        Type Safety · Strict Mode · Zero 'any' · Generics             ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  TYPE SAFETY ANALYSIS
════════════════════════════════════════════════════════════════════════

**Project Type Coverage:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                  │ Current  │ Target  │ Status             │
├────────────────────────────────────────────────────────────────────┤
│ Overall Type Coverage   │ 73.4%    │ > 95%   │ 🔴 Needs Work      │
│ 'any' Type Usage        │ 147      │ 0       │ 🔴 Critical        │
│ 'unknown' Usage         │ 3        │ -       │ ✅ Good Practice   │
│ Strict Mode Enabled     │ Partial  │ Full    │ ⚠️ Enable All      │
│ No Implicit Any         │ false    │ true    │ 🔴 Must Enable     │
│ Strict Null Checks      │ true     │ true    │ ✅ Enabled         │
│ Type Assertions (<>)    │ 89       │ < 20    │ ⚠️ Too Many        │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  'ANY' TYPE VIOLATIONS
════════════════════════════════════════════════════════════════════════

**Top Files with 'any' Usage:**

┌────────────────────────────────────────────────────────────────────┐
│ File                    │ Count │ Critical │ Suggested Fix         │
├────────────────────────────────────────────────────────────────────┤
│ api/handlers.ts         │ 23    │ 🔴 YES   │ Define interfaces     │
│ utils/helpers.ts        │ 18    │ 🔴 YES   │ Use generics          │
│ components/Table.tsx    │ 15    │ ⚠️ HIGH  │ Generic Table<T>      │
│ hooks/useApi.ts         │ 12    │ 🔴 YES   │ Type API responses    │
│ services/auth.ts        │ 9     │ 🔴 YES   │ User interface        │
└────────────────────────────────────────────────────────────────────┘

**Common 'any' Patterns to Fix:**

```typescript
// ❌ BAD - Using 'any'
const handleResponse = (data: any) => {
  return data.result;
};

// ✅ GOOD - Proper typing
interface ApiResponse<T> {
  result: T;
  status: number;
  message: string;
}

const handleResponse = <T>(data: ApiResponse<T>): T => {
  return data.result;
};
```

```typescript
// ❌ BAD - Event handler with 'any'
const onClick = (e: any) => {
  console.log(e.target.value);
};

// ✅ GOOD - Proper event typing
const onClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  console.log(e.currentTarget.value);
};
```

════════════════════════════════════════════════════════════════════════
  STRICT MODE CONFIGURATION
════════════════════════════════════════════════════════════════════════

**Current tsconfig.json:**

```json
{
  "compilerOptions": {
    "strict": false,              // 🔴 Should be true
    "noImplicitAny": false,       // 🔴 Should be true
    "strictNullChecks": true,     // ✅ Good
    "strictFunctionTypes": false, // 🔴 Should be true
    "strictBindCallApply": false, // 🔴 Should be true
    "noImplicitThis": false,      // 🔴 Should be true
    "alwaysStrict": false         // 🔴 Should be true
  }
}
```

**Recommended Configuration:**

```json
{
  "compilerOptions": {
    "strict": true,                    // ✅ Enables all strict checks
    "noUncheckedIndexedAccess": true, // ✅ Safer array access
    "noImplicitReturns": true,        // ✅ Explicit returns
    "noFallthroughCasesInSwitch": true, // ✅ Switch safety
    "noUnusedLocals": true,           // ✅ Clean code
    "noUnusedParameters": true,       // ✅ Clean functions
    "exactOptionalPropertyTypes": true, // ✅ Stricter optionals
    "noImplicitOverride": true        // ✅ Clear inheritance
  }
}
```

**Migration Path:** Enable one flag per week to avoid overwhelming errors

════════════════════════════════════════════════════════════════════════
  TYPE DEFINITION QUALITY
════════════════════════════════════════════════════════════════════════

**Interface/Type Analysis:**

┌────────────────────────────────────────────────────────────────────┐
│ Pattern                 │ Count │ Issue      │ Better Approach     │
├────────────────────────────────────────────────────────────────────┤
│ Optional everything     │ 34    │ Too loose  │ Required + Partial<>│
│ String literals         │ 12    │ Not typed  │ Use union types     │
│ Number for IDs          │ 28    │ Type weak  │ Brand types         │
│ Boolean flags           │ 45    │ Unclear    │ Discriminated unions│
│ Nested any              │ 19    │ Hidden any │ Deep interfaces     │
└────────────────────────────────────────────────────────────────────┘

**Examples of Better Types:**

```typescript
// ❌ WEAK - Everything optional
interface User {
  id?: number;
  name?: string;
  email?: string;
  role?: string;
}

// ✅ STRONG - Clear requirements
interface User {
  id: UserId;  // Branded type
  name: string;
  email: Email;  // Branded type
  role: 'admin' | 'user' | 'guest';  // Union type
}

// Branded types for safety
type UserId = number & { __brand: 'UserId' };
type Email = string & { __brand: 'Email' };
```

```typescript
// ❌ WEAK - Boolean flags
interface State {
  isLoading: boolean;
  isError: boolean;
  isSuccess: boolean;
}

// ✅ STRONG - Discriminated union
type State =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'error'; error: Error }
  | { status: 'success'; data: Data };
```

════════════════════════════════════════════════════════════════════════
  GENERIC TYPE USAGE
════════════════════════════════════════════════════════════════════════

**Generic Opportunities Found:**

┌────────────────────────────────────────────────────────────────────┐
│ Component/Function      │ Current           │ With Generics        │
├────────────────────────────────────────────────────────────────────┤
│ DataTable              │ props: any        │ DataTable<T>         │
│ useApi                 │ returns any       │ useApi<T>()          │
│ createStore            │ state: any        │ createStore<S,A>()   │
│ FormField              │ value: any        │ FormField<T>         │
│ apiClient.get          │ Promise<any>      │ Promise<T>           │
└────────────────────────────────────────────────────────────────────┘

**Generic Implementation Examples:**

```typescript
// ✅ Generic Table Component
interface DataTable<T> {
  data: T[];
  columns: Array<keyof T>;
  onRowClick?: (row: T) => void;
}

// ✅ Generic API Hook
function useApi<T>(url: string): {
  data: T | null;
  loading: boolean;
  error: Error | null;
} {
  // Implementation
}

// ✅ Generic Form Handler
function useForm<T extends Record<string, any>>(
  initialValues: T
): {
  values: T;
  setValue: <K extends keyof T>(key: K, value: T[K]) => void;
  handleSubmit: (onSubmit: (values: T) => void) => void;
}
```

════════════════════════════════════════════════════════════════════════
  UTILITY TYPE USAGE
════════════════════════════════════════════════════════════════════════

**Underutilized TypeScript Utilities:**

┌────────────────────────────────────────────────────────────────────┐
│ Utility Type            │ Usage │ Could Use │ Example Use Case    │
├────────────────────────────────────────────────────────────────────┤
│ Partial<T>              │ 3     │ 15+       │ Update operations   │
│ Pick<T,K>               │ 1     │ 10+       │ DTO objects         │
│ Omit<T,K>               │ 2     │ 8+        │ Exclude fields      │
│ Record<K,V>             │ 5     │ 12+       │ Object maps         │
│ Extract/Exclude         │ 0     │ 5+        │ Type filtering      │
│ NonNullable<T>          │ 0     │ 8+        │ Remove null/undef   │
│ Parameters<T>           │ 0     │ 4+        │ Function args       │
│ ReturnType<T>           │ 1     │ 6+        │ Function returns    │
└────────────────────────────────────────────────────────────────────┘

**Practical Examples:**

```typescript
// Using Partial for updates
type UpdateUser = Partial<User>;

// Using Pick for DTOs
type UserDTO = Pick<User, 'id' | 'name' | 'email'>;

// Using Omit for security
type PublicUser = Omit<User, 'password' | 'ssn'>;

// Using Record for maps
type ErrorMessages = Record<ErrorCode, string>;

// Using template literal types
type ApiEndpoint = `/api/${string}`;
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
```

════════════════════════════════════════════════════════════════════════
  TYPE ASSERTION AUDIT
════════════════════════════════════════════════════════════════════════

**Dangerous Type Assertions Found:**

┌────────────────────────────────────────────────────────────────────┐
│ File                    │ Line  │ Assertion          │ Risk         │
├────────────────────────────────────────────────────────────────────┤
│ auth.service.ts         │ 45    │ as User            │ 🔴 Unsafe    │
│ api.client.ts           │ 89    │ as any             │ 🔴 Critical  │
│ utils.ts                │ 123   │ as unknown as T    │ 🔴 Double    │
│ component.tsx           │ 67    │ as HTMLElement     │ ⚠️ Check     │
│ reducer.ts              │ 234   │ as State           │ ⚠️ Validate  │
└────────────────────────────────────────────────────────────────────┘

**Safe Alternatives:**

```typescript
// ❌ UNSAFE - Type assertion
const user = response.data as User;

// ✅ SAFE - Type guard
function isUser(obj: any): obj is User {
  return obj && typeof obj.id === 'number' && typeof obj.name === 'string';
}

if (isUser(response.data)) {
  // response.data is now typed as User
}

// ✅ SAFE - Zod validation
const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
  email: z.string().email()
});

const user = UserSchema.parse(response.data);
```

════════════════════════════════════════════════════════════════════════
  MIGRATION PRIORITY
════════════════════════════════════════════════════════════════════════

**Week 1 - Critical:**
```bash
1. Enable "noImplicitAny": true
2. Fix 147 'any' types in critical paths
3. Define API response interfaces
```

**Week 2 - High:**
```bash
4. Enable full strict mode
5. Replace type assertions with guards
6. Add generics to reusable components
```

**Week 3 - Medium:**
```bash
7. Implement branded types for IDs
8. Convert boolean flags to unions
9. Add utility types usage
```

**Week 4 - Polish:**
```bash
10. Achieve 95%+ type coverage
11. Document type patterns
12. Setup type checking in CI
```

════════════════════════════════════════════════════════════════════════
  TYPE CHECKING COMMANDS
════════════════════════════════════════════════════════════════════════

• `/typescript-guardian` - Full type analysis
• `/typescript-guardian --any` - Hunt 'any' types
• `/typescript-guardian --coverage` - Type coverage report
• `/typescript-guardian --strict` - Strict mode audit
• `/typescript-guardian --migrate` - Migration plan

════════════════════════════════════════════════════════════════════════

**SENA 🦁 TypeScript Guardian** - Zero 'any', maximum type safety