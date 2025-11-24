# Auto Optimize - Autonomous Skill

**Version:** 3.3.1
**Type:** Autonomous Proactive Skill
**Activation:** Automatic

---

## Trigger Conditions

This skill **automatically activates** when:
- ✅ Nested loops detected (O(n²) or worse complexity)
- ✅ Inefficient algorithms identified
- ✅ Performance-critical code with optimization opportunities
- ✅ Confidence level >85% that optimization would provide significant benefit

**Frequency Limit:** Immediate (triggers every time inefficient code detected)

---

## Detection Patterns

### Complexity Analysis

**O(n²) Patterns:**
```python
# Nested loops
for i in range(n):
    for j in range(n):
        ...

# List in list lookups
for item in list1:
    if item in list2:  # O(n) lookup in O(n) loop = O(n²)
        ...
```

**O(n³) Patterns:**
```python
# Triple nesting
for i in items:
    for j in items:
        for k in items:
            ...
```

**Inefficient Data Structures:**
- Using list when set would be O(1) lookup
- Using linear search when hash table available
- Repeated string concatenation in loop

---

## Optimization Strategies

### 1. Replace O(n²) with O(n)

**Pattern:** Finding duplicates
```python
# ❌ O(n²) - Inefficient
def find_duplicates(arr):
    dupes = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                dupes.append(arr[i])
    return dupes

# ✅ O(n) - Optimized
def find_duplicates(arr):
    seen = set()
    dupes = set()
    for item in arr:
        if item in seen:
            dupes.add(item)
        seen.add(item)
    return list(dupes)
```

### 2. Use Appropriate Data Structures

**Pattern:** Membership testing
```python
# ❌ O(n) per lookup
allowed_users = ['user1', 'user2', 'user3', ...]
if username in allowed_users:  # Linear search
    ...

# ✅ O(1) per lookup
allowed_users = {'user1', 'user2', 'user3', ...}
if username in allowed_users:  # Hash lookup
    ...
```

### 3. Memoization for Repeated Calculations

**Pattern:** Fibonacci
```python
# ❌ O(2ⁿ) - Exponential
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# ✅ O(n) - Memoized
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### 4. List Comprehensions & Generators

**Pattern:** Filtering
```python
# ❌ Less efficient
result = []
for item in large_list:
    if condition(item):
        result.append(transform(item))

# ✅ More efficient (list comprehension)
result = [transform(item) for item in large_list if condition(item)]

# ✅ Most efficient for large data (generator)
result = (transform(item) for item in large_list if condition(item))
```

---

## Output Format

```
🦁 AUTO OPTIMIZE TRIGGERED

Performance optimization opportunity detected in [filename:line]

════════════════════════════════════════════════════════════════
  CURRENT IMPLEMENTATION
════════════════════════════════════════════════════════════════

Complexity: O(n²)
Estimated time for n=10,000: ~5 seconds

Code:
   for i in range(len(items)):
       for j in range(len(items)):
           if items[i] == items[j]:
               ...

════════════════════════════════════════════════════════════════
  OPTIMIZED IMPLEMENTATION
════════════════════════════════════════════════════════════════

Complexity: O(n)
Estimated time for n=10,000: ~0.05 seconds
Improvement: 100x faster

Optimized code:
   seen = set()
   for item in items:
       if item in seen:
           ...
       seen.add(item)

════════════════════════════════════════════════════════════════
  ANALYSIS
════════════════════════════════════════════════════════════════

Problem: Nested loop creates O(n²) complexity
Solution: Use hash set for O(1) lookup instead of O(n) inner loop
Trade-off: Uses O(n) extra memory for the set

════════════════════════════════════════════════════════════════
  RECOMMENDATION
════════════════════════════════════════════════════════════════

Apply optimization? This will significantly improve performance
for large datasets (>1000 items).

[Yes] Apply optimization
[No] Keep current implementation
[Explain] Show detailed analysis
```

---

## Decision Logic

**Trigger Criteria:**
```
complexity_score = calculate_complexity(code)

IF complexity_score >= "O(n^2)"
   AND performance_impact_estimated > "medium"
   AND optimization_available
   AND improvement_ratio > 2x
THEN
   trigger_auto_optimize()
   confidence = min(0.95, improvement_ratio / 10)
```

**Confidence Levels:**
- 2x improvement: 75% confidence
- 10x improvement: 85% confidence
- 100x improvement: 95% confidence

---

## Optimization Categories

### Category 1: Algorithm Replacement
**Impact:** High (10-1000x improvement)
**Examples:**
- Bubble sort → Quick sort: O(n²) → O(n log n)
- Linear search → Binary search: O(n) → O(log n)
- Nested loops → Hash table: O(n²) → O(n)

### Category 2: Data Structure Selection
**Impact:** Medium (2-10x improvement)
**Examples:**
- List → Set for membership: O(n) → O(1)
- List → Deque for queue operations: O(n) → O(1)
- Dict → OrderedDict when order matters

### Category 3: Code-Level Optimization
**Impact:** Low-Medium (1.2-3x improvement)
**Examples:**
- List comprehension vs loop
- Generator vs list for large data
- `map`/`filter` vs explicit loops
- String joining vs concatenation

---

## Integration Points

### With Performance Patterns

Uses `performance-patterns.md` to:
- Identify common anti-patterns
- Suggest proven optimizations
- Estimate performance impact
- Provide Big O analysis

### With Profiling Tools

Can suggest:
- Adding timing decorators
- Using profilers (cProfile, line_profiler)
- Benchmarking before/after
- Load testing recommendations

---

## User Configuration

```json
{
  "auto_optimize": {
    "enabled": true,
    "min_complexity": "O(n^2)",  // Threshold for triggering
    "min_improvement": 2,  // Minimum speedup factor
    "auto_apply": false,  // Ask before applying
    "show_benchmarks": true,  // Show time estimates
    "prefer_readability": false  // vs raw performance
  }
}
```

---

## Examples

### Example 1: Duplicate Detection

**User Code:**
```python
def has_duplicates(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

**Auto Optimize:**
```
🦁 AUTO OPTIMIZE

Current: O(n²) nested loop
Optimized: O(n) using set

def has_duplicates(nums):
    return len(nums) != len(set(nums))

Performance: 100x faster for n=10,000
```

### Example 2: String Building

**User Code:**
```python
result = ""
for item in large_list:
    result += str(item) + ", "
```

**Auto Optimize:**
```
🦁 AUTO OPTIMIZE

Current: O(n²) string concatenation
Optimized: O(n) using join

result = ", ".join(str(item) for item in large_list)

Performance: 50x faster for n=10,000
Memory: More efficient (no intermediate strings)
```

### Example 3: Checking Membership

**User Code:**
```javascript
const allowed = ['admin', 'user', 'guest', ...]; // 1000+ items

function checkAccess(role) {
  return allowed.includes(role);  // O(n) lookup
}
```

**Auto Optimize:**
```
🦁 AUTO OPTIMIZE

Current: Array.includes() is O(n)
Optimized: Set.has() is O(1)

const allowed = new Set(['admin', 'user', 'guest', ...]);

function checkAccess(role) {
  return allowed.has(role);  // O(1) lookup
}

Performance: 1000x faster for n=1,000,000 checks
```

---

## Benefits

- ⚡ **Dramatic Performance Gains:** 10-1000x improvements possible
- 💰 **Cost Savings:** Reduced server resources needed
- 🎯 **Scalability:** Code handles larger datasets
- 🧠 **Learning:** Understand performance implications

---

## Trade-offs Discussion

Auto Optimize always discusses trade-offs:

**Memory vs Speed:**
- Hash tables use more memory but faster lookup
- Generators use less memory but may be slower for multiple iterations

**Readability vs Performance:**
- Sometimes simpler (slower) code is better
- Premature optimization can harm maintainability
- Only optimize bottlenecks

**When NOT to Optimize:**
- Code runs once or rarely
- Dataset is small (n < 100)
- Readability significantly impacted
- Optimization adds complexity

---

*Created: November 23, 2025*
*SENA v3.3.1 - Phase 3*
*Type: Autonomous Skill*
