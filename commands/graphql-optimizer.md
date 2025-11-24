# GraphQL Optimizer

**Optimize GraphQL queries, schemas, and resolvers for maximum performance.**

**IMPORTANT: Analyze GraphQL operations and provide optimization strategies.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 GRAPHQL OPTIMIZER v3.3                            ║
║      Query Analysis · Schema Design · N+1 · Caching · Federation     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  GRAPHQL PERFORMANCE OVERVIEW
════════════════════════════════════════════════════════════════════════

**API Performance Score: 42/100** 🔴

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Current │ Target  │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Average Query Time     │ 847ms   │ < 200ms │ 🔴 Too Slow         │
│ P95 Query Time         │ 2.3s    │ < 500ms │ 🔴 Critical         │
│ Query Complexity       │ 234     │ < 100   │ 🔴 Too Complex      │
│ N+1 Queries            │ 47      │ 0       │ 🔴 Major Issue      │
│ Cache Hit Rate         │ 12%     │ > 80%   │ 🔴 Poor Caching     │
│ Over-fetching          │ 67%     │ < 10%   │ 🔴 Excessive        │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  QUERY ANALYSIS
════════════════════════════════════════════════════════════════════════

**Most Expensive Queries:**

┌────────────────────────────────────────────────────────────────────┐
│ Query                  │ Time    │ DB Calls│ Issue               │
├────────────────────────────────────────────────────────────────────┤
│ getUserWithPosts       │ 1,234ms │ 101     │ 🔴 N+1 query        │
│ searchProducts         │ 890ms   │ 1       │ 🔴 No pagination    │
│ getDashboardData       │ 2,456ms │ 234     │ 🔴 Over-fetching    │
│ getComments            │ 567ms   │ 51      │ 🔴 N+1 query        │
│ getOrderHistory        │ 1,890ms │ 89      │ 🔴 No caching       │
└────────────────────────────────────────────────────────────────────┘

**Query Optimization Examples:**

```graphql
# ❌ BAD - N+1 Query Problem
query GetUsers {
  users {
    id
    name
    posts {  # Separate query for each user!
      id
      title
      comments {  # Another N+1 for each post!
        id
        text
      }
    }
  }
}

# ✅ GOOD - Optimized with DataLoader
query GetUsersOptimized {
  users {
    id
    name
    posts @include(if: $includePosts) {
      id
      title
      commentsCount  # Aggregated field instead of full list
    }
  }
}
```

**DataLoader Implementation:**

```typescript
// ✅ Fix N+1 with DataLoader
import DataLoader from 'dataloader';

// Batch loading function
const batchLoadPosts = async (userIds: string[]) => {
  const posts = await db.post.findMany({
    where: { userId: { in: userIds } }
  });

  // Group posts by userId
  const postsByUser = userIds.map(userId =>
    posts.filter(post => post.userId === userId)
  );

  return postsByUser;
};

// Create DataLoader instance
const postLoader = new DataLoader(batchLoadPosts);

// Resolver using DataLoader
const resolvers = {
  User: {
    posts: (user) => postLoader.load(user.id), // Batched!
  },
};

// ✅ Query Complexity Analysis
import { getComplexity, simpleEstimator } from 'graphql-query-complexity';

const server = new ApolloServer({
  validationRules: [
    createComplexityRule({
      maximumComplexity: 100,
      estimators: [
        simpleEstimator({ defaultComplexity: 1 }),
      ],
      onComplete: (complexity) => {
        console.log('Query Complexity:', complexity);
      },
    }),
  ],
});
```

════════════════════════════════════════════════════════════════════════
  SCHEMA OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Schema Issues Found:**

┌────────────────────────────────────────────────────────────────────┐
│ Issue                  │ Count │ Impact  │ Fix                     │
├────────────────────────────────────────────────────────────────────┤
│ Circular Dependencies  │ 12    │ 🔴 HIGH │ Refactor schema         │
│ Deep Nesting (>5)      │ 8     │ 🔴 HIGH │ Limit depth             │
│ Missing Pagination     │ 23    │ 🔴 HIGH │ Add cursor pagination   │
│ No Field Deprecation   │ 45    │ ⚠️ MED  │ Use @deprecated         │
│ Inconsistent Naming    │ 67    │ 🟡 LOW  │ Follow conventions      │
└────────────────────────────────────────────────────────────────────┘

**Optimized Schema Design:**

```graphql
# ✅ OPTIMIZED Schema with Best Practices

type Query {
  # Paginated queries with filtering
  users(
    first: Int = 10
    after: String
    filter: UserFilter
    orderBy: UserOrderBy
  ): UserConnection!

  # Single resource with ID
  user(id: ID!): User

  # Search with pagination
  searchUsers(
    query: String!
    first: Int = 10
    after: String
  ): SearchResult!
}

# Connection type for cursor pagination
type UserConnection {
  edges: [UserEdge!]!
  pageInfo: PageInfo!
  totalCount: Int!
}

type UserEdge {
  cursor: String!
  node: User!
}

type PageInfo {
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
  endCursor: String
}

# Optimized User type
type User {
  id: ID!
  name: String!
  email: String!

  # Lazy-loaded relationships
  posts(first: Int = 10, after: String): PostConnection! @cost(complexity: 10)

  # Aggregated fields instead of full lists
  postsCount: Int! @cost(complexity: 1)
  followersCount: Int! @cost(complexity: 1)

  # Computed fields with caching
  avatarUrl: String! @cacheControl(maxAge: 3600)
}

# Input types for mutations
input CreateUserInput {
  name: String! @constraint(minLength: 2, maxLength: 100)
  email: String! @constraint(format: "email")
  password: String! @constraint(minLength: 8)
}

# Consistent error handling
interface Error {
  message: String!
  code: String!
}

type ValidationError implements Error {
  message: String!
  code: String!
  field: String!
}

# Mutation responses with errors
type CreateUserPayload {
  user: User
  errors: [Error!]
  userErrors: [ValidationError!] @deprecated(reason: "Use errors field")
}
```

════════════════════════════════════════════════════════════════════════
  RESOLVER OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Resolver Performance Issues:**

┌────────────────────────────────────────────────────────────────────┐
│ Resolver               │ Avg Time│ DB Calls│ Cache │ Issue         │
├────────────────────────────────────────────────────────────────────┤
│ User.posts             │ 234ms   │ 1/user  │ 0%    │ 🔴 N+1        │
│ Post.author            │ 89ms    │ 1/post  │ 0%    │ 🔴 N+1        │
│ Query.searchProducts   │ 890ms   │ 1       │ 0%    │ 🔴 No cache   │
│ User.friends           │ 456ms   │ Multiple│ 12%   │ ⚠️ Complex    │
└────────────────────────────────────────────────────────────────────┘

**Optimized Resolvers:**

```typescript
// ✅ OPTIMIZED Resolvers with Caching & Batching

import { RedisCache } from './cache';
import DataLoader from 'dataloader';

const resolvers = {
  Query: {
    // Cached query
    users: async (_, args, { dataSources, cache }) => {
      const cacheKey = `users:${JSON.stringify(args)}`;

      // Try cache first
      const cached = await cache.get(cacheKey);
      if (cached) return cached;

      // Fetch from database
      const users = await dataSources.userAPI.getUsers(args);

      // Cache for 5 minutes
      await cache.set(cacheKey, users, { ttl: 300 });

      return users;
    },

    // Optimized search with Elasticsearch
    searchProducts: async (_, { query, first, after }) => {
      return dataSources.searchAPI.searchProducts({
        query,
        size: first,
        from: after,
      });
    },
  },

  User: {
    // Batched loading
    posts: (user, args, { loaders }) =>
      loaders.postsByUserLoader.load({ userId: user.id, ...args }),

    // Cached computed field
    avatarUrl: async (user, _, { cache }) => {
      const cacheKey = `avatar:${user.id}`;
      const cached = await cache.get(cacheKey);
      if (cached) return cached;

      const url = await generateAvatarUrl(user);
      await cache.set(cacheKey, url, { ttl: 3600 });
      return url;
    },

    // Aggregated field (no N+1)
    postsCount: async (user, _, { dataSources }) =>
      dataSources.postAPI.countByUser(user.id),
  },

  Mutation: {
    createUser: async (_, { input }, { dataSources, pubsub }) => {
      try {
        const user = await dataSources.userAPI.create(input);

        // Publish event for subscriptions
        pubsub.publish('USER_CREATED', { userCreated: user });

        // Invalidate cache
        await cache.delete('users:*');

        return { user, errors: [] };
      } catch (error) {
        return {
          user: null,
          errors: [{ message: error.message, code: 'CREATE_FAILED' }],
        };
      }
    },
  },
};

// DataLoader Factory
const createLoaders = () => ({
  userLoader: new DataLoader(async (ids) => {
    const users = await db.user.findMany({
      where: { id: { in: ids } }
    });
    return ids.map(id => users.find(u => u.id === id));
  }),

  postsByUserLoader: new DataLoader(async (queries) => {
    const userIds = queries.map(q => q.userId);
    const posts = await db.post.findMany({
      where: { userId: { in: userIds } },
      take: queries[0].first || 10,
    });

    return queries.map(query =>
      posts.filter(p => p.userId === query.userId)
    );
  }, {
    cacheKeyFn: (query) => JSON.stringify(query),
  }),
});
```

════════════════════════════════════════════════════════════════════════
  CACHING STRATEGY
════════════════════════════════════════════════════════════════════════

**Cache Configuration:**

```typescript
// ✅ Multi-layer Caching Strategy

// 1. Response Cache (CDN/Apollo)
const server = new ApolloServer({
  plugins: [
    responseCachePlugin({
      sessionId: (requestContext) =>
        requestContext.request.http.headers.get('session-id') || 'public',
    }),
  ],
  cacheControl: {
    defaultMaxAge: 0,
    calculateHttpHeaders: true,
  },
});

// 2. Redis Cache for Data
const cache = new RedisCache({
  host: process.env.REDIS_HOST,
  ttl: 300, // 5 minutes default
});

// 3. In-Memory Cache for Hot Data
const memoryCache = new LRUCache({
  max: 500,
  maxAge: 1000 * 60 * 5, // 5 minutes
});

// 4. Cache Directives in Schema
type Product @cacheControl(maxAge: 300) {
  id: ID!
  name: String!
  price: Float! @cacheControl(maxAge: 60)
  inventory: Int! @cacheControl(maxAge: 0) # Never cache
}

// 5. Smart Cache Invalidation
const invalidateUserCache = async (userId: string) => {
  await Promise.all([
    cache.delete(`user:${userId}`),
    cache.delete(`users:*`), // Wildcard deletion
    cache.delete(`posts:user:${userId}`),
  ]);
};
```

════════════════════════════════════════════════════════════════════════
  FEDERATION & MICROSERVICES
════════════════════════════════════════════════════════════════════════

**Federation Setup:**

```graphql
# User Service Schema
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.0")

type User @key(fields: "id") {
  id: ID!
  name: String!
  email: String!
}

# Product Service Schema
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.0")

type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Float!
}

type User @key(fields: "id") @extends {
  id: ID! @external
  purchases: [Product!]! # Federated relationship
}

# Gateway Configuration
const gateway = new ApolloGateway({
  supergraphSdl,
  buildService({ url }) {
    return new RemoteGraphQLDataSource({
      url,
      willSendRequest({ request, context }) {
        request.http.headers.set('user-id', context.userId);
      },
    });
  },
});
```

════════════════════════════════════════════════════════════════════════
  MONITORING & OBSERVABILITY
════════════════════════════════════════════════════════════════════════

**Performance Monitoring:**

```typescript
// Apollo Studio Integration
const server = new ApolloServer({
  plugins: [
    ApolloServerPluginUsageReporting({
      sendVariableValues: { all: true },
      sendHeaders: { all: true },
    }),
    {
      requestDidStart() {
        return {
          willSendResponse(requestContext) {
            // Custom metrics
            const { query, operationName, variables } = requestContext.request;
            const duration = Date.now() - requestContext.startTime;

            metrics.histogram('graphql.query.duration', duration, {
              operation: operationName,
            });

            if (duration > 1000) {
              logger.warn('Slow query detected', {
                operation: operationName,
                duration,
                query,
                variables,
              });
            }
          },
        };
      },
    },
  ],
});
```

════════════════════════════════════════════════════════════════════════
  OPTIMIZATION CHECKLIST
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL:**
□ Implement DataLoader for all relationships
□ Add pagination to all list queries
□ Set up Redis caching
□ Fix N+1 queries (47 instances)
□ Limit query depth to 5 levels

**⚠️ HIGH:**
□ Add query complexity limits
□ Implement field-level caching
□ Optimize database queries
□ Add request batching
□ Set up monitoring

**🟡 MEDIUM:**
□ Implement schema stitching
□ Add persistent queries
□ Set up subscription scaling
□ Add rate limiting
□ Document API

════════════════════════════════════════════════════════════════════════
  PERFORMANCE GAINS
════════════════════════════════════════════════════════════════════════

**Expected Improvements:**

┌────────────────────────────────────────────────────────────────────┐
│ Metric                 │ Before  │ After   │ Improvement         │
├────────────────────────────────────────────────────────────────────┤
│ Average Query Time     │ 847ms   │ 125ms   │ -85% 🚀            │
│ P95 Query Time         │ 2.3s    │ 400ms   │ -83% 🚀            │
│ Database Queries       │ 234/req │ 12/req  │ -95% 🚀            │
│ Cache Hit Rate         │ 12%     │ 85%     │ +608% 🚀           │
│ Over-fetching          │ 67%     │ 8%      │ -88% 🚀            │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/graphql-optimizer` - Full GraphQL analysis
• `/graphql-optimizer --queries` - Query performance audit
• `/graphql-optimizer --schema` - Schema optimization
• `/graphql-optimizer --n1` - N+1 query detection
• `/graphql-optimizer --cache` - Caching strategy
• `/graphql-optimizer --federation` - Federation setup

════════════════════════════════════════════════════════════════════════

**SENA 🦁 GraphQL Optimizer** - Lightning fast GraphQL APIs