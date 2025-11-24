# Auto Security Scan - Autonomous Skill

**Version:** 3.3.1
**Type:** Autonomous Proactive Skill
**Activation:** Automatic

---

## Trigger Conditions

This skill **automatically activates** when:
- ✅ User input handling detected
- ✅ Database queries (SQL, NoSQL)
- ✅ File operations or system commands
- ✅ Authentication or authorization code
- ✅ Cryptographic operations
- ✅ API endpoints or network operations
- ✅ Confidence level >90% that security check is warranted

**Frequency Limit:** Every occurrence (security is critical)

---

## Security Categories

### 1. OWASP Top 10 Coverage

1. **Injection** (SQL, NoSQL, Command, LDAP)
2. **Broken Authentication**
3. **Sensitive Data Exposure**
4. **XML External Entities (XXE)**
5. **Broken Access Control**
6. **Security Misconfiguration**
7. **Cross-Site Scripting (XSS)**
8. **Insecure Deserialization**
9. **Using Components with Known Vulnerabilities**
10. **Insufficient Logging & Monitoring**

### 2. Common Vulnerabilities

- SQL Injection
- XSS (Cross-Site Scripting)
- CSRF (Cross-Site Request Forgery)
- Path Traversal
- Command Injection
- Insecure Randomness
- Hardcoded Secrets
- Weak Cryptography

---

## Detection Patterns

### Pattern 1: SQL Injection

**Vulnerable:**
```python
# ❌ String concatenation
query = f"SELECT * FROM users WHERE email = '{email}'"
cursor.execute(query)

# ❌ String formatting
query = "SELECT * FROM users WHERE email = '%s'" % email
cursor.execute(query)
```

**Secure:**
```python
# ✅ Parameterized query
query = "SELECT * FROM users WHERE email = ?"
cursor.execute(query, (email,))

# ✅ ORM (automatically safe)
user = User.query.filter_by(email=email).first()
```

### Pattern 2: XSS

**Vulnerable:**
```javascript
// ❌ Direct HTML injection
element.innerHTML = userInput;

// ❌ eval() with user data
eval(userData);
```

**Secure:**
```javascript
// ✅ Text content (auto-escaped)
element.textContent = userInput;

// ✅ Sanitization library
element.innerHTML = DOMPurify.sanitize(userInput);
```

### Pattern 3: Command Injection

**Vulnerable:**
```python
# ❌ Shell execution with user input
os.system(f"convert {user_file} output.png")

# ❌ Unvalidated shell command
subprocess.run(f"ping {user_host}", shell=True)
```

**Secure:**
```python
# ✅ No shell, array arguments
subprocess.run(["convert", user_file, "output.png"])

# ✅ Input validation
if re.match(r'^[a-zA-Z0-9.-]+$', user_host):
    subprocess.run(["ping", "-c", "1", user_host])
```

### Pattern 4: Path Traversal

**Vulnerable:**
```python
# ❌ Direct file access with user input
file_path = f"/uploads/{user_filename}"
with open(file_path) as f:
    ...
```

**Secure:**
```python
# ✅ Path validation
from pathlib import Path

base_dir = Path("/uploads")
file_path = (base_dir / user_filename).resolve()

# Ensure path is within base directory
if not file_path.is_relative_to(base_dir):
    raise ValueError("Invalid file path")
```

### Pattern 5: Weak Cryptography

**Vulnerable:**
```python
# ❌ MD5 for passwords
import hashlib
password_hash = hashlib.md5(password.encode()).hexdigest()

# ❌ Math.random() for security
token = str(random.random())
```

**Secure:**
```python
# ✅ bcrypt/argon2 for passwords
import bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# ✅ Cryptographically secure random
import secrets
token = secrets.token_urlsafe(32)
```

---

## Output Format

```
🦁 AUTO SECURITY SCAN

🔴 SECURITY VULNERABILITY DETECTED in [filename:line]

════════════════════════════════════════════════════════════════
  VULNERABILITY
════════════════════════════════════════════════════════════════

Type: SQL Injection (OWASP #1)
Severity: CRITICAL
Risk: Remote Code Execution, Data Breach

Vulnerable code:
   query = f"SELECT * FROM users WHERE id = {user_id}"
   db.execute(query)

════════════════════════════════════════════════════════════════
  ATTACK SCENARIO
════════════════════════════════════════════════════════════════

An attacker could inject:
   user_id = "1 OR 1=1; DROP TABLE users; --"

Resulting query:
   SELECT * FROM users WHERE id = 1 OR 1=1; DROP TABLE users; --

Impact: Complete database compromise

════════════════════════════════════════════════════════════════
  SECURE FIX
════════════════════════════════════════════════════════════════

Use parameterized queries:
   query = "SELECT * FROM users WHERE id = ?"
   db.execute(query, (user_id,))

Why this works:
- Database treats user_id as DATA, not CODE
- Special characters are escaped automatically
- Prevents all SQL injection attacks

════════════════════════════════════════════════════════════════
  RECOMMENDATION
════════════════════════════════════════════════════════════════

🚨 IMMEDIATE ACTION REQUIRED

This is a critical security vulnerability that could lead to:
- Complete database access
- Data theft
- Data deletion
- Remote code execution

Apply fix immediately before deployment.

[Apply Fix] Automatically fix with parameterized query
[Learn More] Show detailed SQL injection tutorial
[Ignore] (Not recommended for critical issues)
```

---

## Security Levels

### 🔴 CRITICAL (Immediate Action Required)
- SQL Injection
- Command Injection
- Authentication bypass
- Remote Code Execution
- Hardcoded credentials

### ⚠️ HIGH (Fix Before Production)
- XSS vulnerabilities
- Broken access control
- Sensitive data exposure
- Insecure deserialization
- Weak cryptography

### ⚡ MEDIUM (Should Fix)
- Missing input validation
- Insufficient logging
- Security misconfiguration
- Using components with vulnerabilities

### ℹ️  LOW (Best Practice)
- Missing CSRF tokens
- Weak password requirements
- Missing security headers
- Verbose error messages

---

## Detection Logic

**Trigger Decision Tree:**
```
1. Code contains user input?
   → Check for validation/sanitization

2. Code builds SQL/commands?
   → Check for parameterization

3. Code handles authentication?
   → Check for secure practices

4. Code uses crypto?
   → Check for strong algorithms

5. Code handles files?
   → Check for path validation

IF vulnerability_detected:
   severity = assess_severity()
   IF severity >= MEDIUM:
      trigger_auto_security_scan()
```

---

## Integration Points

### With Security Patterns

Uses `security-patterns.md` for:
- OWASP Top 10 checks
- Secure coding examples
- Best practices validation
- Framework-specific guidance

### With MCP Servers

Can integrate with:
- GitHub for security scanning in repos
- Database for checking production code
- Web search for CVE lookups

---

## User Configuration

```json
{
  "auto_security_scan": {
    "enabled": true,
    "min_severity": "medium",  // "low" | "medium" | "high" | "critical"
    "categories": [
      "injection",
      "xss",
      "auth",
      "crypto",
      "access_control"
    ],
    "auto_fix": false,  // Ask before applying fixes
    "show_examples": true,  // Show attack scenarios
    "owasp_version": "2021"  // OWASP Top 10 version
  }
}
```

---

## Examples

### Example 1: SQL Injection

**User Code:**
```python
def get_user(email):
    query = f"SELECT * FROM users WHERE email = '{email}'"
    return db.execute(query).fetchone()
```

**Auto Security Scan:**
```
🦁 AUTO SECURITY SCAN

🔴 SQL INJECTION DETECTED

Current code allows injection via email parameter.

Secure fix:
   query = "SELECT * FROM users WHERE email = ?"
   return db.execute(query, (email,)).fetchone()

Apply fix? [Yes/No/Explain]
```

### Example 2: XSS

**User Code:**
```javascript
function showMessage(msg) {
  document.getElementById('output').innerHTML = msg;
}
```

**Auto Security Scan:**
```
🦁 AUTO SECURITY SCAN

⚠️  XSS VULNERABILITY DETECTED

innerHTML with unsanitized input allows script injection.

Secure options:
1. Use textContent (safest):
   element.textContent = msg;

2. Sanitize with DOMPurify:
   element.innerHTML = DOMPurify.sanitize(msg);

Apply option 1? [Yes/No/Show Both]
```

### Example 3: Weak Password Hashing

**User Code:**
```python
import hashlib

password_hash = hashlib.sha256(password.encode()).hexdigest()
```

**Auto Security Scan:**
```
🦁 AUTO SECURITY SCAN

⚠️  WEAK PASSWORD HASHING DETECTED

SHA-256 is not suitable for passwords (too fast, enables brute force).

Secure alternatives:
1. bcrypt (recommended):
   import bcrypt
   hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

2. Argon2 (best, won Password Hashing Competition):
   import argon2
   hasher = argon2.PasswordHasher()
   hash = hasher.hash(password)

Apply bcrypt? [Yes/No/Learn More]
```

### Example 4: Command Injection

**User Code:**
```python
import os

os.system(f"ping -c 1 {user_host}")
```

**Auto Security Scan:**
```
🦁 AUTO SECURITY SCAN

🔴 COMMAND INJECTION DETECTED

Attacker could inject: user_host = "8.8.8.8; rm -rf /"

Secure fix:
   import subprocess
   subprocess.run(["ping", "-c", "1", user_host])

Apply fix? [Yes/No/Explain]
```

---

## Benefits

- 🛡️ **Prevents Security Breaches:** Catch vulnerabilities before deployment
- 💰 **Saves Costs:** Fixing vulnerabilities in development is 100x cheaper
- 📚 **Educational:** Learn secure coding practices
- ✅ **Compliance:** Meet security standards (OWASP, PCI DSS, etc.)
- 🚀 **Faster Security Reviews:** Automated checks accelerate process

---

## Best Practices Enforced

### Input Validation
- ✅ Validate all user input
- ✅ Use allowlists, not denylists
- ✅ Validate type, length, format, range

### Authentication & Authorization
- ✅ Use proven libraries (OAuth, JWT)
- ✅ Multi-factor authentication
- ✅ Secure session management
- ✅ Proper password hashing

### Data Protection
- ✅ Encrypt sensitive data
- ✅ Use HTTPS for all communication
- ✅ Secure key management
- ✅ Proper error handling (no info leakage)

### Code Security
- ✅ Parameterized queries
- ✅ Output encoding
- ✅ Secure random generation
- ✅ Regular dependency updates

---

*Created: November 23, 2025*
*SENA v3.3.1 - Phase 3*
*Type: Autonomous Skill*
