# React Component Analyzer

**Analyze React components for anti-patterns, performance issues, and best practices.**

**IMPORTANT: When analyzing React code, provide comprehensive analysis directly. For actual project files, use Read tool first.**

---

╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║            SENA 🦁 REACT COMPONENT ANALYZER v3.3                     ║
║       Anti-Patterns · Performance · Hooks · Best Practices           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════
  ANALYSIS CAPABILITIES
════════════════════════════════════════════════════════════════════════

**What This Tool Analyzes:**

✅ **Hook Violations**
   • Missing dependencies in useEffect/useCallback/useMemo
   • Conditional hooks (violating Rules of Hooks)
   • Unnecessary dependency arrays
   • Stale closure issues

✅ **Performance Anti-Patterns**
   • Inline function definitions in render
   • Object/array literals in dependency arrays
   • Missing React.memo for pure components
   • Excessive re-renders
   • Large component trees without splitting

✅ **State Management Issues**
   • Prop drilling (passing props through many layers)
   • Duplicated state
   • State that should be derived
   • Missing state lifting
   • Overuse of useState vs useReducer

✅ **Component Structure**
   • Components doing too much (need splitting)
   • Missing error boundaries
   • Improper component composition
   • Missing key props in lists
   • Direct DOM manipulation

✅ **TypeScript Integration**
   • Missing or weak prop types
   • any types in component props
   • Missing return type annotations
   • Incorrect event handler types

════════════════════════════════════════════════════════════════════════
  EXAMPLE ANALYSIS OUTPUT
════════════════════════════════════════════════════════════════════════

**Component: UserDashboard.tsx**

┌────────────────────────────────────────────────────────────────────┐
│ Issue Type              │ Severity │ Location      │ Fix Required   │
├────────────────────────────────────────────────────────────────────┤
│ Missing Dependencies    │ 🔴 HIGH  │ Line 45       │ Add 'userId'   │
│ Inline Function        │ ⚠️ MEDIUM │ Line 67       │ Use useCallback│
│ Prop Drilling          │ ⚠️ MEDIUM │ Lines 89-125  │ Use Context    │
│ Large Component        │ 🟡 LOW   │ 450 lines     │ Split component│
│ any Type Usage         │ 🔴 HIGH  │ Line 34       │ Define type    │
└────────────────────────────────────────────────────────────────────┘

**Critical Issues Found: 2**
**Total Issues: 5**
**Component Health Score: 65/100**

════════════════════════════════════════════════════════════════════════
  COMMON REACT ANTI-PATTERNS DETECTED
════════════════════════════════════════════════════════════════════════

**1. useEffect Missing Dependencies**
```jsx
// ❌ BAD - Missing 'userId' dependency
useEffect(() => {
  fetchUserData(userId);
}, []);

// ✅ GOOD - All dependencies included
useEffect(() => {
  fetchUserData(userId);
}, [userId]);
```

**2. Inline Function Definitions**
```jsx
// ❌ BAD - Creates new function every render
<button onClick={() => handleClick(id)}>

// ✅ GOOD - Memoized callback
const handleButtonClick = useCallback(() => {
  handleClick(id);
}, [id]);
<button onClick={handleButtonClick}>
```

**3. Prop Drilling**
```jsx
// ❌ BAD - Passing through 5 levels
<App user={user}>
  <Layout user={user}>
    <Page user={user}>
      <Section user={user}>
        <Profile user={user}>

// ✅ GOOD - Using Context
const UserContext = React.createContext();
<UserContext.Provider value={user}>
  <App />
</UserContext.Provider>
```

════════════════════════════════════════════════════════════════════════
  PERFORMANCE OPTIMIZATION SUGGESTIONS
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Optimization            │ Impact   │ Difficulty │ Time Saved       │
├────────────────────────────────────────────────────────────────────┤
│ Add React.memo         │ HIGH     │ Easy       │ 40% rerenders    │
│ Use useMemo for lists  │ HIGH     │ Medium     │ 60% compute time │
│ Split large components │ MEDIUM   │ Medium     │ Better maintain. │
│ Virtualize long lists  │ HIGH     │ Hard       │ 80% render time  │
│ Lazy load routes       │ HIGH     │ Easy       │ 50% bundle size  │
└────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════
  HOOK ANALYSIS
════════════════════════════════════════════════════════════════════════

**Hook Usage Statistics:**
```
useState:        23 instances (5 could be combined)
useEffect:       12 instances (3 have missing deps)
useCallback:     4 instances (8 more needed)
useMemo:         2 instances (4 more recommended)
useContext:      1 instance (consider for prop drilling)
useReducer:      0 instances (recommended for complex state)
Custom Hooks:    3 instances (good abstraction!)
```

**Custom Hook Opportunities:**
• Extract `useFetchUser` from repeated fetch pattern
• Create `useDebounce` for search inputs
• Build `useLocalStorage` for persistent state

════════════════════════════════════════════════════════════════════════
  COMPONENT COMPLEXITY ANALYSIS
════════════════════════════════════════════════════════════════════════

**Complexity Metrics:**
```
Cyclomatic Complexity:  12 (threshold: 10) ⚠️
Cognitive Complexity:   18 (threshold: 15) ⚠️
Lines of Code:         450 (threshold: 300) 🔴
Number of Props:       23 (threshold: 15) 🔴
Nesting Depth:         5 (threshold: 4) ⚠️
```

**Refactoring Suggestions:**
1. Split into 3 components: Header, Content, Footer
2. Extract business logic to custom hooks
3. Move API calls to separate service layer
4. Reduce prop count using composition

════════════════════════════════════════════════════════════════════════
  TYPESCRIPT INTEGRATION REPORT
════════════════════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────────────────────┐
│ Type Coverage           │ Current  │ Target  │ Status             │
├────────────────────────────────────────────────────────────────────┤
│ Props Typed            │ 78%      │ 100%    │ ⚠️ Needs Work      │
│ State Typed            │ 92%      │ 100%    │ 🟡 Good            │
│ Event Handlers Typed   │ 45%      │ 100%    │ 🔴 Critical        │
│ Return Types           │ 67%      │ 100%    │ ⚠️ Needs Work      │
│ No 'any' Usage         │ 89%      │ 100%    │ 🟡 Good            │
└────────────────────────────────────────────────────────────────────┘

**Files Needing Type Improvements:**
• UserDashboard.tsx - 5 'any' types
• ProfileCard.tsx - Missing prop interface
• DataTable.tsx - Generic types needed

════════════════════════════════════════════════════════════════════════
  RECOMMENDED FIXES (Priority Order)
════════════════════════════════════════════════════════════════════════

**🔴 CRITICAL (Fix Immediately):**
1. Add missing useEffect dependencies (3 instances)
2. Replace 'any' types with proper interfaces (5 instances)
3. Add error boundaries to handle failures

**⚠️ HIGH (Fix This Sprint):**
4. Memoize expensive computations with useMemo
5. Replace inline functions with useCallback
6. Split components over 300 lines

**🟡 MEDIUM (Fix Next Sprint):**
7. Implement React.memo for pure components
8. Extract custom hooks for repeated logic
9. Add loading and error states

**🔵 LOW (Nice to Have):**
10. Improve component naming conventions
11. Add JSDoc comments to complex functions
12. Create Storybook stories for components

════════════════════════════════════════════════════════════════════════
  CODE GENERATION HELPERS
════════════════════════════════════════════════════════════════════════

**Generate Better Hooks:**
```bash
/generate-hook useFetchUser
/generate-hook useDebounce
/generate-hook useLocalStorage
```

**Generate Component Tests:**
```bash
/generate-test UserDashboard
/generate-test ProfileCard --with-rtl
```

**Generate TypeScript Interfaces:**
```bash
/generate-types UserDashboard
/generate-types --from-api /api/users
```

════════════════════════════════════════════════════════════════════════
  COMMANDS
════════════════════════════════════════════════════════════════════════

• `/react-analyzer <file>` - Analyze specific component
• `/react-analyzer --all` - Analyze entire project
• `/react-analyzer --hooks` - Focus on hooks analysis
• `/react-analyzer --performance` - Performance audit
• `/react-analyzer --types` - TypeScript coverage

════════════════════════════════════════════════════════════════════════

**SENA 🦁 React Analyzer** - Your component quality guardian