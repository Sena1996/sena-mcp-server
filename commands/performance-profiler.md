# Performance Profiler

**Profile application performance, identify bottlenecks, and optimize runtime execution.**

**IMPORTANT: Comprehensive performance analysis for frontend and backend with actionable insights.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 PERFORMANCE PROFILER v3.3                         ║
║       Runtime · Memory · Network · Database · Rendering              ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  PERFORMANCE OVERVIEW
════════════════════════════════════════════════════════════════════════

**Application Performance Score: 68/100** ⚠️

┌────────────────────────────────────────────────────────────────────┐
│ Metric                  │ Current │ Target  │ Status              │
├────────────────────────────────────────────────────────────────────┤
│ Time to Interactive     │ 4.5s    │ < 3.5s  │ 🔴 Too Slow         │
│ First Contentful Paint  │ 1.8s    │ < 1.5s  │ ⚠️ Optimize         │
│ Largest Contentful Paint│ 3.2s    │ < 2.5s  │ 🔴 Critical         │
│ Cumulative Layout Shift │ 0.18    │ < 0.1   │ ⚠️ Reduce Shifts    │
│ Total Blocking Time     │ 450ms   │ < 300ms │ ⚠️ Too Much JS      │
│ Speed Index             │ 4.8s    │ < 3.0s  │ 🔴 Slow             │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  JAVASCRIPT EXECUTION PROFILE
════════════════════════════════════════════════════════════════════════

**Main Thread Activity (5s window):**

```
Scripting    ████████████████░░░░ 78% (3.9s) 🔴
Rendering    ███░░░░░░░░░░░░░░░░░ 12% (0.6s)
Painting     ██░░░░░░░░░░░░░░░░░░  8% (0.4s)
System       ░░░░░░░░░░░░░░░░░░░░  2% (0.1s)
Idle         ░░░░░░░░░░░░░░░░░░░░  0% (0.0s) 🔴
```

**Long Tasks (>50ms):**

┌────────────────────────────────────────────────────────────────────┐
│ Task                    │ Duration │ Impact  │ Location            │
├────────────────────────────────────────────────────────────────────┤
│ React hydration         │ 847ms    │ 🔴 HIGH │ main.js:1847        │
│ Bundle evaluation       │ 623ms    │ 🔴 HIGH │ vendor.js:234       │
│ Event listener setup    │ 234ms    │ ⚠️ MED  │ app.js:567          │
│ Style recalculation     │ 189ms    │ ⚠️ MED  │ styles.css          │
│ Layout calculation      │ 156ms    │ ⚠️ MED  │ DOM                 │
│ JSON parsing            │ 134ms    │ ⚠️ MED  │ api-client.js:89    │
└────────────────────────────────────────────────────────────────────┘

**Call Stack Hot Path:**

```javascript
// 🔴 HOTTEST PATH - 34% of execution time
main.js:1847 > hydrate()
  └─ ReactDOM.hydrate()
      └─ reconcileChildren() // 423ms
          └─ updateFunctionComponent() // 234ms
              └─ useState() // 156ms
                  └─ dispatchAction() // 89ms
```

════════════════════════════════════════════════════════════════════════
  MEMORY PROFILING
════════════════════════════════════════════════════════════════════════

**Memory Usage Timeline:**

```
Heap Size:
120MB ┤                    ╭────────
100MB ┤                ╭───╯  ⚠️ Memory spike
 80MB ┤            ╭───╯
 60MB ┤        ╭───╯
 40MB ┤    ╭───╯
 20MB ┤────╯
      └────┬────┬────┬────┬────┬────
         0s   1s   2s   3s   4s   5s
```

**Memory Leak Detection:**

┌────────────────────────────────────────────────────────────────────┐
│ Component/Object        │ Instances │ Retained Size │ Leak?         │
├────────────────────────────────────────────────────────────────────┤
│ EventListener          │ 2,847     │ 12.3 MB       │ 🔴 Yes        │
│ Detached DOM nodes     │ 456       │ 8.7 MB        │ 🔴 Yes        │
│ Closures               │ 1,234     │ 5.4 MB        │ ⚠️ Maybe      │
│ React Fiber nodes      │ 8,923     │ 3.2 MB        │ ✅ Normal     │
│ Cached API responses   │ 89        │ 45.6 MB       │ 🔴 Too Large  │
└────────────────────────────────────────────────────────────────────┘

**Memory Leak Fix:**

```javascript
// ❌ LEAK - Event listeners not cleaned up
useEffect(() => {
  window.addEventListener('resize', handleResize);
  // Missing cleanup!
});

// ✅ FIXED - Proper cleanup
useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

// ❌ LEAK - Closure holding large data
function createHandler(largeData) {
  return function() {
    console.log('Event!');
    // largeData is retained even though unused
  };
}

// ✅ FIXED - Release reference
function createHandler(largeData) {
  const needed = largeData.id; // Extract only what's needed
  return function() {
    console.log('Event!', needed);
  };
}
```

════════════════════════════════════════════════════════════════════════
  NETWORK PERFORMANCE
════════════════════════════════════════════════════════════════════════

**Request Waterfall Analysis:**

```
Resource Timeline (0-5s):
HTML       ██░░░░░░░░░░░░░░░░░░ (200ms)
CSS        ░██░░░░░░░░░░░░░░░░░ (180ms)
JS Bundle  ░░████████░░░░░░░░░░ (800ms) 🔴
Fonts      ░░░░██░░░░░░░░░░░░░░ (150ms)
Images     ░░░░░░████████░░░░░░ (600ms)
API Calls  ░░░░░░░░░░████░░░░░░ (400ms)
```

**Network Bottlenecks:**

┌────────────────────────────────────────────────────────────────────┐
│ Resource               │ Size    │ Time   │ Issue                 │
├────────────────────────────────────────────────────────────────────┤
│ vendor.bundle.js       │ 892 KB  │ 2.3s   │ 🔴 Too large          │
│ main.bundle.js         │ 487 KB  │ 1.8s   │ ⚠️ Could split        │
│ hero-image.jpg         │ 2.3 MB  │ 3.4s   │ 🔴 Not optimized      │
│ /api/initial-data      │ 145 KB  │ 890ms  │ ⚠️ Could cache        │
│ fonts.googleapis.com   │ 67 KB   │ 450ms  │ ⚠️ Could self-host    │
└────────────────────────────────────────────────────────────────────┘

**Optimization Opportunities:**

```javascript
// ✅ Preload critical resources
<link rel="preload" href="/fonts/inter.woff2" as="font" crossorigin>
<link rel="preload" href="/api/initial-data" as="fetch" crossorigin>

// ✅ Lazy load images
<img loading="lazy" src="hero.jpg">

// ✅ Resource hints
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preconnect" href="https://api.example.com">
```

════════════════════════════════════════════════════════════════════════
  DATABASE QUERY PROFILING
════════════════════════════════════════════════════════════════════════

**Slow Query Log:**

┌────────────────────────────────────────────────────────────────────┐
│ Query                           │ Time   │ Rows  │ Issue           │
├────────────────────────────────────────────────────────────────────┤
│ SELECT * FROM users WHERE...    │ 234ms  │ 10K   │ 🔴 No index     │
│ JOIN orders ON users.id...      │ 456ms  │ 50K   │ 🔴 N+1 query    │
│ SELECT COUNT(*) FROM products   │ 123ms  │ 1     │ ⚠️ Could cache  │
│ UPDATE sessions SET...          │ 89ms   │ 1     │ ⚠️ Too frequent │
│ SELECT posts.*, users.*...      │ 567ms  │ 100   │ 🔴 Over-fetching│
└────────────────────────────────────────────────────────────────────┘

**N+1 Query Detection:**

```javascript
// ❌ N+1 QUERY - Makes 101 queries
const posts = await db.post.findMany({ take: 100 });
for (const post of posts) {
  post.author = await db.user.findUnique({ where: { id: post.authorId }});
}

// ✅ FIXED - Single query with join
const posts = await db.post.findMany({
  take: 100,
  include: { author: true }
});

// ✅ BETTER - Batch loading
const posts = await db.post.findMany({ take: 100 });
const authorIds = posts.map(p => p.authorId);
const authors = await db.user.findMany({
  where: { id: { in: authorIds }}
});
```

════════════════════════════════════════════════════════════════════════
  REACT PERFORMANCE
════════════════════════════════════════════════════════════════════════

**Component Render Profile:**

┌────────────────────────────────────────────────────────────────────┐
│ Component              │ Renders │ Avg Time │ Wasted │ Issue       │
├────────────────────────────────────────────────────────────────────┤
│ <App>                  │ 47      │ 23ms     │ 78%    │ 🔴 Too many │
│ <Dashboard>            │ 89      │ 45ms     │ 82%    │ 🔴 Too many │
│ <UserList>             │ 234     │ 12ms     │ 91%    │ 🔴 Critical │
│ <DataTable>            │ 156     │ 34ms     │ 67%    │ ⚠️ Optimize │
│ <SearchBar>            │ 456     │ 8ms      │ 94%    │ 🔴 Critical │
└────────────────────────────────────────────────────────────────────┘

**React Optimization Fixes:**

```javascript
// ❌ PROBLEM - Re-renders on every parent render
function ExpensiveComponent({ data }) {
  const processed = heavyComputation(data);
  return <div>{processed}</div>;
}

// ✅ SOLUTION 1 - Memoize component
const ExpensiveComponent = React.memo(({ data }) => {
  const processed = heavyComputation(data);
  return <div>{processed}</div>;
});

// ✅ SOLUTION 2 - Memoize computation
function ExpensiveComponent({ data }) {
  const processed = useMemo(() => heavyComputation(data), [data]);
  return <div>{processed}</div>;
}

// ❌ PROBLEM - Inline function causes re-renders
<ChildComponent onClick={() => handleClick(id)} />

// ✅ SOLUTION - Memoize callback
const handleChildClick = useCallback(() => {
  handleClick(id);
}, [id]);
<ChildComponent onClick={handleChildClick} />
```

════════════════════════════════════════════════════════════════════════
  RENDERING PERFORMANCE
════════════════════════════════════════════════════════════════════════

**Paint & Layout Timeline:**

```
Frame Budget (60fps = 16.67ms):
Frame 1: ████████████████████ 20ms 🔴 Jank
Frame 2: ████████████░░░░░░░░ 12ms ✅
Frame 3: ████████████████████ 24ms 🔴 Jank
Frame 4: ████████░░░░░░░░░░░░ 8ms  ✅
```

**Layout Thrashing Detection:**

```javascript
// ❌ LAYOUT THRASHING - Forces reflow
elements.forEach(el => {
  el.style.left = el.offsetLeft + 10 + 'px';  // Read
  el.style.top = el.offsetTop + 10 + 'px';    // Read
});

// ✅ FIXED - Batch reads then writes
const positions = elements.map(el => ({
  left: el.offsetLeft,
  top: el.offsetTop
}));

elements.forEach((el, i) => {
  el.style.left = positions[i].left + 10 + 'px';
  el.style.top = positions[i].top + 10 + 'px';
});
```

════════════════════════════════════════════════════════════════════════
  OPTIMIZATION RECOMMENDATIONS
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL (Immediate):**
1. Code split vendor bundle (-400KB initial load)
2. Fix React re-rendering in UserList component
3. Add database index on users.email column
4. Remove memory leaks (event listeners)
5. Optimize hero image (2.3MB → 200KB)

**⚠️ HIGH (This Week):**
6. Implement React.memo for pure components
7. Add request caching layer
8. Lazy load below-fold components
9. Fix N+1 queries in API
10. Reduce main thread blocking

**🟡 MEDIUM (This Sprint):**
11. Implement virtual scrolling for long lists
12. Add service worker for offline caching
13. Optimize web fonts loading
14. Implement request batching
15. Add performance monitoring

**Expected Improvements:**
- Page Load: 4.5s → 1.8s (-60%)
- Memory Usage: 120MB → 60MB (-50%)
- API Response: 890ms → 200ms (-78%)

════════════════════════════════════════════════════════════════════════
  MONITORING SETUP
════════════════════════════════════════════════════════════════════════

```javascript
// Real User Monitoring (RUM)
const perfObserver = new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    analytics.track('performance', {
      name: entry.name,
      duration: entry.duration,
      type: entry.entryType
    });
  }
});

perfObserver.observe({ entryTypes: ['navigation', 'resource', 'paint'] });

// Custom performance marks
performance.mark('myComponent-start');
// ... component code
performance.mark('myComponent-end');
performance.measure('myComponent', 'myComponent-start', 'myComponent-end');
```

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/performance-profiler` - Full performance audit
• `/performance-profiler --js` - JavaScript execution profile
• `/performance-profiler --memory` - Memory leak detection
• `/performance-profiler --network` - Network waterfall analysis
• `/performance-profiler --react` - React component profiling
• `/performance-profiler --database` - Query performance

════════════════════════════════════════════════════════════════════════

**SENA 🦁 Performance Profiler** - Find bottlenecks, ship faster apps