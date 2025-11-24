# State Manager Analyzer

**Analyze and optimize state management patterns (Redux, Zustand, Context API, MobX).**

**IMPORTANT: Identify state management issues and provide optimization strategies.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 STATE MANAGER ANALYZER v3.3                       ║
║        Redux · Zustand · Context · MobX · Performance                ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  STATE MANAGEMENT OVERVIEW
════════════════════════════════════════════════════════════════════════

**Current State Architecture:**

┌────────────────────────────────────────────────────────────────────┐
│ Library/Pattern        │ Usage   │ Issues  │ Performance         │
├────────────────────────────────────────────────────────────────────┤
│ Redux                  │ 45%     │ 12      │ ⚠️ Over-rendering   │
│ Context API            │ 35%     │ 8       │ 🔴 Provider hell    │
│ Local State (useState) │ 15%     │ 23      │ 🔴 Prop drilling    │
│ Zustand               │ 5%      │ 2       │ ✅ Good            │
│ Global Variables       │ 2%      │ 5       │ 🔴 Anti-pattern     │
└────────────────────────────────────────────────────────────────────┘

**State Complexity Score:** 34/100 🔴 (Too Complex!)

════════════════════════════════════════════════════════════════════════
  REDUX OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Redux Store Analysis:**

```javascript
// Current Redux Issues Found:
Store Size: 12.3 MB 🔴 (Too Large!)
Normalized: 23% 🔴 (Should be 80%+)
Selectors: 12 🔴 (Need more memoization)
Actions: 234 ⚠️ (Could be reduced)
Reducers: 45 ⚠️ (Some duplicate logic)
```

**Redux Optimization Patterns:**

```typescript
// ❌ BAD - Storing denormalized data
const state = {
  posts: [
    {
      id: 1,
      title: 'Post 1',
      author: { id: 1, name: 'John', email: 'john@example.com' },
      comments: [{ id: 1, text: 'Great!', author: {...} }]
    }
  ]
};

// ✅ GOOD - Normalized state
const state = {
  posts: {
    byId: {
      '1': { id: 1, title: 'Post 1', authorId: 1, commentIds: [1] }
    },
    allIds: ['1']
  },
  users: {
    byId: {
      '1': { id: 1, name: 'John', email: 'john@example.com' }
    },
    allIds: ['1']
  },
  comments: {
    byId: {
      '1': { id: 1, text: 'Great!', authorId: 1 }
    },
    allIds: ['1']
  }
};

// ✅ OPTIMIZED - Memoized selectors
import { createSelector } from '@reduxjs/toolkit';

export const selectPostWithAuthor = createSelector(
  [
    (state, postId) => state.posts.byId[postId],
    (state, postId) => state.users.byId[state.posts.byId[postId]?.authorId]
  ],
  (post, author) => ({ ...post, author })
);

// ✅ RTK Query for API state
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['Post', 'User'],
  endpoints: (builder) => ({
    getPosts: builder.query({
      query: () => 'posts',
      providesTags: ['Post'],
    }),
    updatePost: builder.mutation({
      query: ({ id, ...patch }) => ({
        url: `posts/${id}`,
        method: 'PATCH',
        body: patch,
      }),
      invalidatesTags: ['Post'],
    }),
  }),
});
```

════════════════════════════════════════════════════════════════════════
  ZUSTAND OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Zustand Best Practices:**

```typescript
// ✅ OPTIMIZED Zustand Store
import { create } from 'zustand';
import { devtools, persist, subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

interface StoreState {
  users: Record<string, User>;
  posts: Post[];
  loading: boolean;
  error: string | null;
  // Actions
  fetchUsers: () => Promise<void>;
  updateUser: (id: string, data: Partial<User>) => void;
  reset: () => void;
}

const useStore = create<StoreState>()(
  devtools(
    persist(
      subscribeWithSelector(
        immer((set, get) => ({
          users: {},
          posts: [],
          loading: false,
          error: null,

          fetchUsers: async () => {
            set((state) => {
              state.loading = true;
              state.error = null;
            });

            try {
              const users = await api.getUsers();
              set((state) => {
                state.users = users.reduce((acc, user) => {
                  acc[user.id] = user;
                  return acc;
                }, {});
              });
            } catch (error) {
              set((state) => {
                state.error = error.message;
              });
            } finally {
              set((state) => {
                state.loading = false;
              });
            }
          },

          updateUser: (id, data) =>
            set((state) => {
              if (state.users[id]) {
                Object.assign(state.users[id], data);
              }
            }),

          reset: () =>
            set(() => ({
              users: {},
              posts: [],
              loading: false,
              error: null,
            })),
        }))
      ),
      {
        name: 'app-storage',
        partialize: (state) => ({ users: state.users }), // Only persist users
      }
    )
  )
);

// Selectors with automatic memoization
export const useUser = (id: string) => useStore((state) => state.users[id]);
export const useUsers = () => useStore((state) => Object.values(state.users));
export const useIsLoading = () => useStore((state) => state.loading);
```

════════════════════════════════════════════════════════════════════════
  CONTEXT API OPTIMIZATION
════════════════════════════════════════════════════════════════════════

**Context Issues Found:**

┌────────────────────────────────────────────────────────────────────┐
│ Issue                  │ Count │ Impact  │ Fix                     │
├────────────────────────────────────────────────────────────────────┤
│ Provider Hell          │ 8     │ 🔴 HIGH │ Combine contexts        │
│ Unnecessary Re-renders │ 234   │ 🔴 HIGH │ Split contexts          │
│ Missing Memoization    │ 45    │ ⚠️ MED  │ Add useMemo            │
│ Direct Mutations       │ 12    │ 🔴 HIGH │ Immutable updates       │
└────────────────────────────────────────────────────────────────────┘

**Context Optimization Patterns:**

```typescript
// ❌ BAD - Single context causes all consumers to re-render
const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [theme, setTheme] = useState('light');
  const [settings, setSettings] = useState({});

  return (
    <AppContext.Provider value={{ user, theme, settings, setUser, setTheme, setSettings }}>
      {children}
    </AppContext.Provider>
  );
};

// ✅ GOOD - Split contexts by update frequency
const UserContext = createContext();
const ThemeContext = createContext();
const SettingsContext = createContext();

// ✅ BETTER - Separate state and dispatch contexts
const StateContext = createContext();
const DispatchContext = createContext();

export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  // Memoize to prevent re-renders
  const stateValue = useMemo(() => state, [state]);
  const dispatchValue = useMemo(() => dispatch, []);

  return (
    <StateContext.Provider value={stateValue}>
      <DispatchContext.Provider value={dispatchValue}>
        {children}
      </DispatchContext.Provider>
    </StateContext.Provider>
  );
};

// ✅ BEST - Use selector pattern
export function useAppState<T>(selector: (state: AppState) => T) {
  const state = useContext(StateContext);
  return useMemo(() => selector(state), [state, selector]);
}

// Usage
const user = useAppState(state => state.user);
const theme = useAppState(state => state.theme);
```

════════════════════════════════════════════════════════════════════════
  STATE MIGRATION GUIDE
════════════════════════════════════════════════════════════════════════

**Migration from Redux to Zustand:**

```typescript
// Redux (Before)
const userSlice = createSlice({
  name: 'user',
  initialState: { data: null, loading: false },
  reducers: {
    setUser: (state, action) => {
      state.data = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
});

// Zustand (After)
const useUserStore = create((set) => ({
  data: null,
  loading: false,
  setUser: (user) => set({ data: user }),
  setLoading: (loading) => set({ loading }),
}));

// Migration utility
export function migrateReduxToZustand(reduxStore) {
  const state = reduxStore.getState();

  // Map Redux state to Zustand
  useUserStore.setState({
    data: state.user.data,
    loading: state.user.loading,
  });
}
```

════════════════════════════════════════════════════════════════════════
  PERFORMANCE METRICS
════════════════════════════════════════════════════════════════════════

**State Update Performance:**

┌────────────────────────────────────────────────────────────────────┐
│ Operation              │ Redux  │ Zustand│ Context│ Local State    │
├────────────────────────────────────────────────────────────────────┤
│ Simple Update          │ 12ms   │ 3ms    │ 8ms    │ 2ms            │
│ Batch Updates (10)     │ 89ms   │ 15ms   │ 45ms   │ 12ms           │
│ Selector (memoized)    │ 0.5ms  │ 0.3ms  │ 2ms    │ N/A            │
│ Re-renders Caused      │ 45     │ 12     │ 89     │ 5              │
│ Memory Usage           │ 12MB   │ 3MB    │ 5MB    │ 1MB            │
└────────────────────────────────────────────────────────────────────┘

**Render Optimization:**

```typescript
// Track unnecessary re-renders
if (process.env.NODE_ENV === 'development') {
  const useRenderCounter = () => {
    const renderCount = useRef(0);
    renderCount.current++;

    useEffect(() => {
      console.log(`Component rendered ${renderCount.current} times`);
    });
  };
}

// Prevent re-renders with stable references
const stableCallback = useCallback((data) => {
  // Process data
}, []); // Empty deps = stable forever

const stableValue = useMemo(() =>
  expensiveComputation(data),
  [data]
);
```

════════════════════════════════════════════════════════════════════════
  STATE DEBUGGING TOOLS
════════════════════════════════════════════════════════════════════════

**Redux DevTools Integration:**

```typescript
// Zustand with DevTools
const useStore = create(
  devtools(
    (set) => ({
      // Your store
    }),
    {
      name: 'AppStore',
      trace: true, // Stack traces
      anonymousActionType: 'unknown',
    }
  )
);

// Custom state logger
const logger = (config) => (set, get, api) =>
  config(
    (...args) => {
      console.log('Previous State:', get());
      set(...args);
      console.log('New State:', get());
    },
    get,
    api
  );
```

════════════════════════════════════════════════════════════════════════
  RECOMMENDATIONS
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL:**
1. Normalize Redux state (reduce from 12MB to 3MB)
2. Split monolithic contexts into smaller ones
3. Add selector memoization (prevent 234 re-renders)
4. Remove global variables (security risk)

**⚠️ HIGH:**
5. Migrate simple state from Redux to Zustand
6. Implement RTK Query for API state
7. Add state persistence layer
8. Setup state debugging tools

**🟡 MEDIUM:**
9. Document state architecture
10. Add state migration utilities
11. Implement optimistic updates
12. Add state validation layer

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/state-manager` - Full state analysis
• `/state-manager --redux` - Redux optimization
• `/state-manager --zustand` - Zustand patterns
• `/state-manager --context` - Context optimization
• `/state-manager --migrate` - Migration guide
• `/state-manager --performance` - Performance audit

════════════════════════════════════════════════════════════════════════

**SENA 🦁 State Manager** - Optimal state, zero re-renders