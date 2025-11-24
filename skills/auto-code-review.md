# Auto Code Review - Autonomous Skill

**Version:** 3.3.1
**Type:** Autonomous Proactive Skill
**Activation:** Automatic

---

## Trigger Conditions

This skill **automatically activates** when:
- ✅ User writes >50 lines of code in a single operation
- ✅ User creates/modifies a programming file (.py, .js, .ts, .java, .go, etc.)
- ✅ User requests a git commit with code changes
- ✅ Confidence level >80% that code review would be helpful

**Frequency Limit:** Once per file per session (prevents spam)

---

## Analysis Framework

When triggered, perform comprehensive code review checking:

### 1. Code Quality Metrics

**Readability:**
- [ ] Clear, descriptive variable/function names
- [ ] Appropriate comments for complex logic
- [ ] Consistent formatting and style
- [ ] Logical code organization

**Maintainability:**
- [ ] Functions have single responsibility
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Appropriate abstraction levels
- [ ] Clear module/class structure

**Best Practices:**
- [ ] Follows language-specific conventions
- [ ] Uses appropriate data structures
- [ ] Error handling implemented
- [ ] Edge cases considered

### 2. Common Issues Check

**Python-Specific:**
- Mutable default arguments
- Bare except clauses
- Missing type hints (Python 3.6+)
- Inefficient list comprehensions

**JavaScript/TypeScript:**
- Missing async/await
- Callback hell
- Missing error handling in promises
- Type safety issues (TS)

**General:**
- Magic numbers/strings
- Deep nesting (>3 levels)
- Long functions (>50 lines)
- Circular dependencies

### 3. Performance Review

- Algorithm complexity (target: O(n log n) or better)
- Unnecessary loops or operations
- Inefficient data structure usage
- Memory leaks or excessive allocation

### 4. Security Check

- Input validation present
- No SQL injection risks
- No XSS vulnerabilities
- Secure random generation
- Sensitive data handling

---

## Output Format

```
🦁 AUTO CODE REVIEW

I've analyzed your recent code changes in [filename]

OVERALL SCORE: [8.5/10]

════════════════════════════════════════════════════════════════
  STRENGTHS
════════════════════════════════════════════════════════════════

✅ Well-structured with clear separation of concerns
✅ Good error handling with try-except blocks
✅ Descriptive variable names enhance readability

════════════════════════════════════════════════════════════════
  SUGGESTIONS FOR IMPROVEMENT
════════════════════════════════════════════════════════════════

💡 Consider adding type hints for better IDE support:
   def process_data(items: List[str]) -> Dict[str, int]:

⚠️  Function `calculate_metrics` is 65 lines - consider splitting:
   - Extract validation logic → validate_input()
   - Extract calculation → compute_statistics()

🔧 Replace magic number with named constant:
   TIMEOUT_SECONDS = 30  # Instead of hardcoded 30

════════════════════════════════════════════════════════════════
  SECURITY & PERFORMANCE
════════════════════════════════════════════════════════════════

✅ No security issues detected
✅ Performance: O(n) complexity - optimal for this use case

════════════════════════════════════════════════════════════════
  RECOMMENDATION
════════════════════════════════════════════════════════════════

Code is production-ready with minor improvements suggested above.
Would you like me to apply any of these refactorings?
```

---

## Decision Logic

**When to trigger:**
```
IF (code_written > 50 lines OR significant_changes_detected)
   AND programming_language_detected
   AND NOT already_reviewed_this_file_this_session
   AND user_not_explicitly_disabled
THEN
   trigger_auto_review()
```

**Confidence Calculation:**
- File extension matches programming language: +30%
- Significant code changes detected: +30%
- No review in this session yet: +20%
- Code complexity warrants review: +20%
- **Total >= 80%:** Trigger

---

## Integration Points

### With SENA Memory System

Uses knowledge from:
- `security-patterns.md` for security checks
- `performance-patterns.md` for optimization suggestions
- `architecture-patterns.md` for design recommendations

### With Existing Tools

- Can trigger after `Write` tool usage
- Can integrate with git `commit` operations
- Can provide context for `Edit` suggestions

---

## User Configuration

Users can customize in `~/.claude/sena_skills.json`:

```json
{
  "auto_code_review": {
    "enabled": true,
    "min_lines": 50,
    "trigger_on": ["write", "commit"],
    "frequency": "once_per_file_per_session",
    "strictness": "balanced",  // "lenient" | "balanced" | "strict"
    "focus_areas": ["all"],  // or ["security", "performance", "quality"]
  }
}
```

---

## Examples

### Example 1: Python Function

**User writes:**
```python
def process_users(users):
    result = []
    for user in users:
        if user['age'] > 18:
            result.append(user)
    return result
```

**Auto Review Triggers:**
```
🦁 AUTO CODE REVIEW

Quick suggestions for `process_users`:

💡 Add type hints:
   def process_users(users: List[Dict]) -> List[Dict]:

💡 Use list comprehension for better performance:
   return [user for user in users if user['age'] > 18]

✅ Consider defensive programming:
   return [user for user in users if user.get('age', 0) > 18]
```

### Example 2: JavaScript Async

**User writes:**
```javascript
function fetchData(url) {
  return fetch(url)
    .then(res => res.json())
    .then(data => processData(data))
    .catch(err => console.log(err));
}
```

**Auto Review Triggers:**
```
🦁 AUTO CODE REVIEW

Modernization suggestion for `fetchData`:

💡 Use async/await for better readability:
   async function fetchData(url) {
     try {
       const res = await fetch(url);
       const data = await res.json();
       return processData(data);
     } catch (err) {
       console.error('Error fetching data:', err);
       throw err; // Re-throw for caller to handle
     }
   }
```

---

## Benefits

- ⚡ **Faster Development:** Catch issues immediately
- 🎯 **Higher Quality:** Automatic best practice enforcement
- 🧠 **Learning:** See suggestions and improve over time
- 🛡️ **Fewer Bugs:** Issues caught before they reach production

---

*Created: November 23, 2025*
*SENA v3.3.1 - Phase 3*
*Type: Autonomous Skill*
