# API Architect

**Design and validate RESTful APIs, GraphQL schemas, and ensure consistency across endpoints.**

**IMPORTANT: Generate API specifications with validation, documentation, and TypeScript types.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 API ARCHITECT v3.3                                ║
║      REST · GraphQL · OpenAPI · Validation · Types · Docs            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  API DESIGN ANALYSIS
════════════════════════════════════════════════════════════════════════

**Current API Structure:**

┌────────────────────────────────────────────────────────────────────┐
│ Endpoint                │ Method │ Status │ Issues               │
├────────────────────────────────────────────────────────────────────┤
│ /api/users              │ GET    │ ✅     │ -                    │
│ /api/users/:id          │ GET    │ ⚠️      │ No 404 handling      │
│ /api/users              │ POST   │ 🔴     │ No validation        │
│ /api/users/:id          │ PUT    │ 🔴     │ Partial update?      │
│ /api/users/:id          │ DELETE │ ⚠️      │ No soft delete       │
│ /api/products/search    │ GET    │ 🔴     │ Inconsistent params  │
│ /api/auth/login         │ POST   │ ⚠️      │ Rate limiting?       │
│ /api/upload             │ POST   │ 🔴     │ No file validation   │
└────────────────────────────────────────────────────────────────────┘

**Consistency Score:** 45/100 🔴
**Documentation Coverage:** 23% 🔴
**Type Safety:** 67% ⚠️

════════════════════════════════════════════════════════════════════════
  RESTful API DESIGN
════════════════════════════════════════════════════════════════════════

**Standard REST Pattern:**

```typescript
// ✅ PROPER REST STRUCTURE
interface RestEndpoints {
  // Collection endpoints
  'GET    /api/users'           // List all users
  'POST   /api/users'           // Create new user

  // Resource endpoints
  'GET    /api/users/:id'       // Get specific user
  'PUT    /api/users/:id'       // Full update
  'PATCH  /api/users/:id'       // Partial update
  'DELETE /api/users/:id'       // Delete user

  // Sub-resources
  'GET    /api/users/:id/posts' // User's posts
  'POST   /api/users/:id/posts' // Create post for user

  // Actions (when REST doesn't fit)
  'POST   /api/users/:id/activate'
  'POST   /api/auth/refresh'
}
```

**Generated API Handler:**

```typescript
// api/users/route.ts - Next.js App Router
import { NextRequest, NextResponse } from 'next/server';
import { z } from 'zod';
import { validateRequest, handleError, rateLimit } from '@/lib/api';

// Request/Response schemas
const CreateUserSchema = z.object({
  name: z.string().min(2).max(100),
  email: z.string().email(),
  role: z.enum(['admin', 'user', 'guest']),
});

const UserResponseSchema = z.object({
  id: z.string().uuid(),
  name: z.string(),
  email: z.string().email(),
  role: z.string(),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
});

// Paginated response
const UsersListSchema = z.object({
  data: z.array(UserResponseSchema),
  pagination: z.object({
    page: z.number(),
    limit: z.number(),
    total: z.number(),
    totalPages: z.number(),
  }),
  links: z.object({
    self: z.string().url(),
    next: z.string().url().optional(),
    prev: z.string().url().optional(),
  }),
});

// GET /api/users
export async function GET(request: NextRequest) {
  try {
    // Rate limiting
    await rateLimit(request);

    // Parse query params
    const { searchParams } = new URL(request.url);
    const page = parseInt(searchParams.get('page') || '1');
    const limit = parseInt(searchParams.get('limit') || '10');
    const sort = searchParams.get('sort') || 'createdAt';
    const order = searchParams.get('order') || 'desc';

    // Fetch from database
    const users = await db.user.findMany({
      skip: (page - 1) * limit,
      take: limit,
      orderBy: { [sort]: order },
    });

    const total = await db.user.count();

    // Build response
    const response = UsersListSchema.parse({
      data: users,
      pagination: {
        page,
        limit,
        total,
        totalPages: Math.ceil(total / limit),
      },
      links: {
        self: `/api/users?page=${page}&limit=${limit}`,
        next: page * limit < total ? `/api/users?page=${page + 1}&limit=${limit}` : undefined,
        prev: page > 1 ? `/api/users?page=${page - 1}&limit=${limit}` : undefined,
      },
    });

    return NextResponse.json(response, {
      status: 200,
      headers: {
        'X-Total-Count': total.toString(),
        'Cache-Control': 'private, max-age=60',
      },
    });
  } catch (error) {
    return handleError(error);
  }
}

// POST /api/users
export async function POST(request: NextRequest) {
  try {
    await rateLimit(request);

    // Validate request body
    const body = await request.json();
    const validated = await validateRequest(CreateUserSchema, body);

    // Check duplicates
    const existing = await db.user.findUnique({
      where: { email: validated.email },
    });

    if (existing) {
      return NextResponse.json(
        { error: 'User with this email already exists' },
        { status: 409 } // Conflict
      );
    }

    // Create user
    const user = await db.user.create({
      data: validated,
    });

    // Return created resource
    return NextResponse.json(
      UserResponseSchema.parse(user),
      {
        status: 201, // Created
        headers: {
          'Location': `/api/users/${user.id}`,
        },
      }
    );
  } catch (error) {
    return handleError(error);
  }
}
```

════════════════════════════════════════════════════════════════════════
  ERROR RESPONSE STANDARDIZATION
════════════════════════════════════════════════════════════════════════

**Consistent Error Format:**

```typescript
interface ApiError {
  error: {
    code: string;           // Machine-readable
    message: string;        // Human-readable
    details?: any;          // Additional context
    timestamp: string;      // ISO 8601
    path: string;          // Request path
    requestId?: string;    // For debugging
  };
}

// Examples:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "name": "Name must be at least 2 characters",
      "email": "Invalid email format"
    },
    "timestamp": "2024-01-15T10:30:00Z",
    "path": "/api/users",
    "requestId": "req_abc123"
  }
}
```

**Status Code Guide:**

┌────────────────────────────────────────────────────────────────────┐
│ Code │ Meaning              │ When to Use                         │
├────────────────────────────────────────────────────────────────────┤
│ 200  │ OK                   │ Successful GET, PUT, PATCH         │
│ 201  │ Created              │ Successful POST creating resource  │
│ 204  │ No Content           │ Successful DELETE                  │
│ 400  │ Bad Request          │ Invalid syntax or parameters       │
│ 401  │ Unauthorized         │ Missing or invalid auth token       │
│ 403  │ Forbidden            │ Valid auth but no permission       │
│ 404  │ Not Found            │ Resource doesn't exist              │
│ 409  │ Conflict             │ Duplicate or conflicting state     │
│ 422  │ Unprocessable        │ Valid syntax but semantic errors   │
│ 429  │ Too Many Requests    │ Rate limit exceeded                 │
│ 500  │ Internal Error       │ Server error (log, don't expose)   │
│ 503  │ Service Unavailable  │ Temporary outage or maintenance    │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  OPENAPI SPECIFICATION GENERATOR
════════════════════════════════════════════════════════════════════════

**Generated OpenAPI 3.0 Spec:**

```yaml
openapi: 3.0.0
info:
  title: Your API
  version: 1.0.0
  description: Auto-generated API documentation

servers:
  - url: https://api.example.com/v1
    description: Production
  - url: http://localhost:3000/api
    description: Development

components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    User:
      type: object
      required: [id, name, email]
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
          minLength: 2
          maxLength: 100
        email:
          type: string
          format: email

    Error:
      type: object
      required: [error]
      properties:
        error:
          type: object
          required: [code, message]
          properties:
            code:
              type: string
            message:
              type: string

paths:
  /users:
    get:
      summary: List users
      parameters:
        - in: query
          name: page
          schema:
            type: integer
            default: 1
        - in: query
          name: limit
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/User'
```

════════════════════════════════════════════════════════════════════════
  GRAPHQL SCHEMA DESIGN
════════════════════════════════════════════════════════════════════════

**GraphQL Type Definitions:**

```graphql
# Generated GraphQL Schema
type User {
  id: ID!
  name: String!
  email: String!
  role: UserRole!
  posts(first: Int, after: String): PostConnection!
  createdAt: DateTime!
  updatedAt: DateTime!
}

enum UserRole {
  ADMIN
  USER
  GUEST
}

type PostConnection {
  edges: [PostEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type PostEdge {
  node: Post!
  cursor: String!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

type Query {
  # Get single user
  user(id: ID!): User

  # List users with filtering
  users(
    first: Int
    after: String
    filter: UserFilter
    orderBy: UserOrderBy
  ): UserConnection!
}

type Mutation {
  # Create new user
  createUser(input: CreateUserInput!): CreateUserPayload!

  # Update user
  updateUser(id: ID!, input: UpdateUserInput!): UpdateUserPayload!

  # Delete user
  deleteUser(id: ID!): DeleteUserPayload!
}

input CreateUserInput {
  name: String!
  email: String!
  role: UserRole
}

type CreateUserPayload {
  user: User
  errors: [Error!]
}
```

════════════════════════════════════════════════════════════════════════
  API VALIDATION MIDDLEWARE
════════════════════════════════════════════════════════════════════════

**Generated Validation Middleware:**

```typescript
// middleware/validation.ts
import { z } from 'zod';
import { NextRequest, NextResponse } from 'next/server';

export function validateBody(schema: z.ZodSchema) {
  return async (req: NextRequest) => {
    try {
      const body = await req.json();
      const validated = schema.parse(body);
      return { success: true, data: validated };
    } catch (error) {
      if (error instanceof z.ZodError) {
        return {
          success: false,
          error: NextResponse.json(
            {
              error: {
                code: 'VALIDATION_ERROR',
                message: 'Invalid request data',
                details: error.errors,
              },
            },
            { status: 400 }
          ),
        };
      }
      throw error;
    }
  };
}

// Rate limiting
export async function rateLimit(
  req: NextRequest,
  limit = 100,
  window = 60000
) {
  const ip = req.ip || 'unknown';
  const key = `rate_limit:${ip}`;

  // Check Redis or in-memory store
  const count = await redis.incr(key);

  if (count === 1) {
    await redis.expire(key, window / 1000);
  }

  if (count > limit) {
    throw new ApiError('RATE_LIMIT_EXCEEDED', 429);
  }
}

// Auth middleware
export async function requireAuth(req: NextRequest) {
  const token = req.headers.get('authorization')?.replace('Bearer ', '');

  if (!token) {
    throw new ApiError('UNAUTHORIZED', 401);
  }

  try {
    const payload = await verifyJWT(token);
    return payload;
  } catch {
    throw new ApiError('INVALID_TOKEN', 401);
  }
}
```

════════════════════════════════════════════════════════════════════════
  TYPESCRIPT CLIENT GENERATOR
════════════════════════════════════════════════════════════════════════

**Auto-Generated Type-Safe Client:**

```typescript
// Generated api-client.ts
export class ApiClient {
  constructor(private baseURL: string, private token?: string) {}

  private async request<T>(
    path: string,
    options?: RequestInit
  ): Promise<T> {
    const res = await fetch(`${this.baseURL}${path}`, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        ...(this.token && { Authorization: `Bearer ${this.token}` }),
        ...options?.headers,
      },
    });

    if (!res.ok) {
      const error = await res.json();
      throw new ApiError(error);
    }

    return res.json();
  }

  // Type-safe methods
  users = {
    list: (params?: UserListParams) =>
      this.request<UserListResponse>('/users?' + new URLSearchParams(params)),

    get: (id: string) =>
      this.request<User>(`/users/${id}`),

    create: (data: CreateUserInput) =>
      this.request<User>('/users', {
        method: 'POST',
        body: JSON.stringify(data),
      }),

    update: (id: string, data: UpdateUserInput) =>
      this.request<User>(`/users/${id}`, {
        method: 'PUT',
        body: JSON.stringify(data),
      }),

    delete: (id: string) =>
      this.request<void>(`/users/${id}`, {
        method: 'DELETE',
      }),
  };
}

// Usage:
const api = new ApiClient('https://api.example.com');
const users = await api.users.list({ page: 1, limit: 10 });
```

════════════════════════════════════════════════════════════════════════
  API TESTING SUITE
════════════════════════════════════════════════════════════════════════

**Generated API Tests:**

```typescript
// __tests__/api/users.test.ts
describe('Users API', () => {
  it('GET /api/users returns paginated list', async () => {
    const res = await request(app)
      .get('/api/users?page=1&limit=10')
      .expect(200)
      .expect('Content-Type', /json/);

    expect(res.body).toMatchObject({
      data: expect.any(Array),
      pagination: {
        page: 1,
        limit: 10,
        total: expect.any(Number),
      },
      links: {
        self: expect.any(String),
      },
    });
  });

  it('POST /api/users creates new user', async () => {
    const newUser = {
      name: 'Test User',
      email: 'test@example.com',
      role: 'user',
    };

    const res = await request(app)
      .post('/api/users')
      .send(newUser)
      .expect(201)
      .expect('Location', /\/api\/users\/[\w-]+/);

    expect(res.body).toMatchObject({
      id: expect.any(String),
      ...newUser,
    });
  });

  it('validates request body', async () => {
    const invalid = { name: 'A' }; // Too short

    const res = await request(app)
      .post('/api/users')
      .send(invalid)
      .expect(400);

    expect(res.body.error.code).toBe('VALIDATION_ERROR');
  });
});
```

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/api-architect` - Analyze API design
• `/api-architect --generate-rest` - Generate REST endpoints
• `/api-architect --generate-graphql` - Generate GraphQL schema
• `/api-architect --generate-types` - Generate TypeScript types
• `/api-architect --generate-client` - Generate API client
• `/api-architect --generate-docs` - Generate OpenAPI docs
• `/api-architect --generate-tests` - Generate API tests

════════════════════════════════════════════════════════════════════════

**SENA 🦁 API Architect** - Design consistent, type-safe APIs