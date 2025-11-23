# SENA CLI Rules System

**Purpose:** Enhance Claude Code CLI with automatic formatting, enforcement, and intelligence
**Environment:** Claude Code CLI only (Terminal)
**Version:** 3.3.1

---

## Overview

The SENA CLI Rules System is a comprehensive set of 8 mandatory rules that extend Claude Code's behavior in the terminal environment. These rules work in conjunction with enforcement hooks to provide automatic formatting, keyword detection, and quality assurance.

**Key Concept:**
- **Rules** = Instructions in `~/.claude/CLAUDE.md` that Claude follows
- **Hooks** = Bash scripts in `~/.claude/hooks/` that enforce these rules
- **Integration** = Rules + Hooks working together for consistent behavior

---

## Rule System Architecture

```
User Input
    ↓
[user-prompt-submit.sh]
    ├─ Check always-on mode → Add SENA 🦁 prefix
    ├─ Detect keywords (table, why, explain)
    └─ Inject enforcement reminders
    ↓
Claude Processing
    ├─ Follow CLAUDE.md rules
    ├─ Use MCP tools
    └─ Generate response
    ↓
[sena-enforcer.sh]
    ├─ Validate SENA markers present
    ├─ Check format compliance
    └─ Allow/Block response
    ↓
[post-tool-use.sh]
    └─ Clean up tool invocation details
    ↓
User sees clean, formatted output
```

---

## The 8 Mandatory Rules

### Rule 0: SENA Always-On Mode Prefix

**Trigger:** When `~/.claude/.sena_always_on` file exists

**Behavior:**
```
EVERY response MUST start with: SENA 🦁

No exceptions - applies to ALL responses:
- Simple questions → Start with "SENA 🦁"
- Complex questions → Start with "SENA 🦁"
- Table requests → Start with "SENA 🦁"
- Code analysis → Start with "SENA 🦁"
```

**Example:**
```
User: "give me moon info in table"
Assistant: SENA 🦁

╔══════════════════════════════════════╗
║        📊 MOON INFORMATION           ║
╚══════════════════════════════════════╝
[table follows]
```

**Implementation:**
- Hook: `user-prompt-submit.sh` checks for flag file
- Adds reminder to prompt if file exists
- Enforcer validates prefix present

---

### Rule 1: Tabular Data (MANDATORY)

**Triggers:** Keywords "table", "tabular", "tabular format", "in table form"

**Behavior:**
```
Generate formatted table DIRECTLY using Unicode box-drawing characters.

FORBIDDEN:
- Markdown tables (| header |)
- Using Bash tool
- Using Python execution
- Any code execution
```

**Format:**
```
┌────────────────────────────────────┐
│ Header 1  │ Header 2  │ Header 3  │
├────────────────────────────────────┤
│ Data 1    │ Data 2    │ Data 3    │
│ Data 4    │ Data 5    │ Data 6    │
└────────────────────────────────────┘
```

**Optional Title Box:**
```
╔════════════════════════════════════╗
║     📊 TABLE TITLE HERE            ║
╚════════════════════════════════════╝
```

**Why This Method:**
- Clean, instant display
- No Bash tool visibility
- No output collapse
- Professional appearance

---

### Rule 2: Complex Questions (MANDATORY)

**Triggers:** Keywords "why", "how", "explain"

**Behavior:**
```
Generate SENA Brilliant Thinking analysis DIRECTLY.

DO NOT use tools (Bash, Python).
JUST output formatted thinking analysis.
```

**Format:**
```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║         SENA 🦁 BRILLIANT THINKING                   ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════
  QUESTION ANALYSIS
════════════════════════════════════════════════════════

[Restate the question clearly]

════════════════════════════════════════════════════════
  FIRST PRINCIPLES BREAKDOWN
════════════════════════════════════════════════════════

1. [Core concept 1]
2. [Core concept 2]
3. [Core concept 3]

════════════════════════════════════════════════════════
  STRUCTURED ANALYSIS
════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────┐
│ Aspect       │ Analysis                            │
├────────────────────────────────────────────────────┤
│ [Aspect 1]   │ [Detailed analysis]                 │
│ [Aspect 2]   │ [Detailed analysis]                 │
└────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════
  CONCLUSION
════════════════════════════════════════════════════════

[Clear, concise conclusion with key takeaways]
```

**Enforcement:**
- Hook validates "SENA BRILLIANT THINKING" marker present
- Blocks response if plain text explanation without formatting

---

### Rule 3: Truth Verification (MANDATORY)

**Triggers:** "is X true", "fact check", "verify"

**Behavior:**
```
Generate SENA Truth Verification analysis DIRECTLY.
```

**Format:**
```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║       SENA 🦁 TRUTH VERIFICATION SYSTEM              ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════
  CLAIM BEING VERIFIED
════════════════════════════════════════════════════════

"[Statement to verify]"

════════════════════════════════════════════════════════
  VERIFICATION ANALYSIS
════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────┐
│ Verdict      │ [TRUE/FALSE/PARTIALLY TRUE/UNCLEAR] │
│ Confidence   │ [High/Medium/Low]                   │
│ Evidence     │ [Strong/Moderate/Weak]              │
└────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════
  EVIDENCE
════════════════════════════════════════════════════════

✅ Supporting Evidence:
  • [Evidence point 1]
  • [Evidence point 2]

❌ Contradicting Evidence:
  • [Evidence point 1]
  • [Evidence point 2]

════════════════════════════════════════════════════════
  FINAL VERDICT
════════════════════════════════════════════════════════

[Clear statement of truth/falsehood with nuance]
```

---

### Rule 4: Code Analysis (MANDATORY)

**Triggers:** "analyze code", "code review", "code quality"

**Behavior:**
```
Generate SENA Code Analysis DIRECTLY.
```

**Format:**
```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║         SENA 🦁 CODE QUALITY ANALYSIS                ║
║                                                      ║
╚══════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════
  CODE OVERVIEW
════════════════════════════════════════════════════════

[Brief description of what the code does]

════════════════════════════════════════════════════════
  QUALITY METRICS
════════════════════════════════════════════════════════

┌────────────────────────────────────────────────────┐
│ Metric           │ Score    │ Status              │
├────────────────────────────────────────────────────┤
│ Code Clarity     │ [Score]  │ [Status]            │
│ Performance      │ [Score]  │ [Status]            │
│ Security         │ [Score]  │ [Status]            │
│ Maintainability  │ [Score]  │ [Status]            │
└────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════
  ISSUES & RECOMMENDATIONS
════════════════════════════════════════════════════════

🔴 Critical Issues:
  • [Issue 1]

⚠️  Warnings:
  • [Warning 1]

✅ Strengths:
  • [Strength 1]
```

---

### Rule 5: Output Display (MANDATORY - 100% ENFORCEMENT)

**Purpose:** Clean, professional output without tool invocation details

**Requirements:**
```
NEVER SHOW IN OUTPUT:
- Bash command calls (MUST be silent)
- Tool invocation details
- "Searching...", "Looking for...", "Let me..." phrases
- Any technical implementation details

ALWAYS SHOW:
- Clean, formatted results only
- Direct answers without preamble
- Beautiful Unicode tables and boxes
- Progress bars for multi-step operations
```

**Correct Example:**
```
User: "give me Mars info in table"
Assistant: SENA 🦁

╔════════════════════════════════════╗
║     📊 MARS INFORMATION            ║
╚════════════════════════════════════╝

┌────────────────────────────────────┐
│ Property    │ Value                │
├────────────────────────────────────┤
│ Diameter    │ 6,779 km             │
│ Distance    │ 227.9M km            │
└────────────────────────────────────┘
```

**Wrong Example:**
```
Assistant: Let me search for Mars information...
*Uses Bash tool: grep "Mars" data.txt*
Here's what I found:
[plain text response]
```

---

### Rule 6: Progress Display (MANDATORY - 100% AUTOMATIC)

**Triggers:**
- Searching files (2+ operations)
- Reading multiple files
- Multi-step analysis
- Any operation with 2+ tool calls

**Format:**
```
Single Progress Bar:
[████████████████🦁████░░░░░░░░░░░░] 75% - Processing data...

Multiple Tasks:
┌──────────────────────────────────────────────────────┐
│ Task 1: Loading   [██████🦁███░░░░░░░░░░] 50%       │
│ Task 2: Process   [███████████🦁███████] 100% ✅     │
│ Task 3: Saving    [███🦁░░░░░░░░░░░░░░░] 20%        │
└──────────────────────────────────────────────────────┘

With Title Box:
╔══════════════════════════════════════════════════════╗
║             SENA 🦁 TASK PROGRESS                    ║
╚══════════════════════════════════════════════════════╝

┌──────────────────────────────────────────────────────┐
│ Stage 1: Init    [████████████🦁████████] 100% ✅    │
│ Stage 2: Execute [████████🦁███░░░░░░░░] 60%        │
│ Stage 3: Finalize[🦁░░░░░░░░░░░░░░░░░░] 0%         │
└──────────────────────────────────────────────────────┘
```

**Elements:**
- Filled: █████
- Empty: ░░░░░
- SENA emoji: 🦁 (at progress point)
- Complete: ✅
- Error: ❌
- Warning: ⚠️

**Implementation:**
- Display progress DIRECTLY in response text
- NO Python scripts needed
- NO background processes
- Static snapshots, not animated

**Note:** Old progress bar scripts (v1.0, v2.0) are DEPRECATED.

---

### Rule 7: Automatic System Integration (100% MANDATORY)

**Purpose:** Automatic keyword detection and format application

**Keyword Triggers:**

| User Says | You MUST Apply |
|-----------|----------------|
| "why" / "how" / "explain" | → BRILLIANT THINKING FORMAT |
| "table" / "tabular" | → TABLE FORMAT |
| "is X true" / "fact" / "verify" | → TRUTH VERIFICATION |
| "analyze code" / "review" | → CODE ANALYSIS |
| Multiple file operations | → PROGRESS BARS |

**Enforcement Checklist:**
- [ ] Did user say "why/how"? → Use Brilliant Thinking
- [ ] Did user say "table"? → Use Table Format
- [ ] Did user say "true/fact"? → Use Truth Verification
- [ ] Did user say "analyze code"? → Use Code Analysis
- [ ] Are you doing 2+ operations? → Show Progress Bars

**Implementation:**
- Hook: `user-prompt-submit.sh` scans for keywords
- Injects format reminders into prompt
- Claude applies appropriate format automatically

---

### Rule 8: GitHub Commits - NO Claude Credits (MANDATORY)

**Purpose:** Clean, professional commit messages

**Requirements:**
```
DO NOT add Claude Code credits to commit messages.

FORBIDDEN:
🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>

INSTEAD:
- Write clean, professional commit messages
- Follow repository's existing commit style
- Do NOT add any Claude/AI attribution
- Keep commits focused on changes made
```

**Enforcement:**
- When user requests git commit → Write WITHOUT credits
- When user requests git push → No attribution
- Keep commits professional and clean

---

## Hook Integration

### Hook Files

| Hook | File | Purpose |
|------|------|---------|
| **UserPromptSubmit** | `user-prompt-submit.sh` | Pre-validation: keyword detection, enforcement injection |
| **AssistantResponseSubmit** | `sena-enforcer.sh` | Post-validation: format checking, response blocking |
| **PostToolUse** | `post-tool-use.sh` | Output cleanup: remove tool details |
| **PermissionRequest** | `permission-request.sh` | Tool permission handling |
| **ConversationProgress** | `conversation-progress.sh` | Session progress tracking |
| **AutoProgress** | `auto-progress.sh` | Automatic progress detection |

### How Hooks Enforce Rules

**user-prompt-submit.sh:**
```bash
# Check always-on mode (Rule 0)
if [ -f ~/.claude/.sena_always_on ]; then
    # Add SENA 🦁 prefix reminder
fi

# Detect keywords (Rule 7)
if echo "$message" | grep -qi "table\|tabular"; then
    # Inject Rule 1 (Table Format) reminder
fi

if echo "$message" | grep -qi "why\|how\|explain"; then
    # Inject Rule 2 (Brilliant Thinking) reminder
fi
```

**sena-enforcer.sh:**
```bash
# Validate SENA markers present
if ! echo "$response" | grep -q "SENA.*BRILLIANT THINKING"; then
    if echo "$prompt" | grep -qi "why\|how\|explain"; then
        # Block response - Rule 2 violated
        echo "ERROR: SENA Brilliant Thinking format required"
        exit 1
    fi
fi

# Validate tables have Unicode formatting
if echo "$prompt" | grep -qi "table"; then
    if ! echo "$response" | grep -q "┌\|╔"; then
        # Block response - Rule 1 violated
        echo "ERROR: Unicode table format required"
        exit 1
    fi
fi
```

**post-tool-use.sh:**
```bash
# Remove tool invocation details (Rule 5)
# Clean up "Bash(command)" patterns
# Remove "Searching..." phrases
```

---

## Installation

### Automatic (Recommended)

```bash
# Clone SENA MCP server
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server

# Run installer
bash install.sh

# Installer will:
# 1. Copy CLAUDE.md to ~/.claude/
# 2. Copy hooks to ~/.claude/hooks/
# 3. Update ~/.claude/settings.json
# 4. Set executable permissions
```

### Manual

```bash
# 1. Copy CLAUDE.md
cp CLAUDE.md ~/.claude/

# 2. Copy hooks
cp hooks/* ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 3. Update settings.json
# Add hooks configuration to ~/.claude/settings.json

# 4. Enable always-on mode (optional)
touch ~/.claude/.sena_always_on
```

---

## Configuration

### Enable Always-On Mode (SENA 🦁 Prefix)

```bash
# Enable
touch ~/.claude/.sena_always_on

# Disable
rm ~/.claude/.sena_always_on
```

### Disable Specific Rules

Edit `~/.claude/CLAUDE.md` and comment out unwanted rules:

```markdown
<!-- ## RULE 1: Tabular Data (DISABLED)
... rule content ...
-->
```

### Disable All Hooks

Edit `~/.claude/settings.json`:

```json
{
  "hooks": {
    // "userPromptSubmit": "~/.claude/hooks/user-prompt-submit.sh",
    // "assistantResponseSubmit": "~/.claude/hooks/sena-enforcer.sh"
  }
}
```

---

## Testing

### Test Individual Rules

```bash
# Test Rule 0 (SENA prefix)
echo "test message" | claude

# Test Rule 1 (Tables)
echo "give me planet data in table" | claude

# Test Rule 2 (Brilliant Thinking)
echo "why is the sky blue?" | claude

# Test Rule 3 (Truth Verification)
echo "is the earth flat?" | claude

# Test Rule 4 (Code Analysis)
echo "analyze this code: function test() { return 42; }" | claude
```

### Test Hooks

```bash
# Test pre-hook
bash ~/.claude/hooks/user-prompt-submit.sh "give me table"

# Test enforcer
# (Requires actual Claude response to validate)

# Test post-hook
bash ~/.claude/hooks/post-tool-use.sh
```

---

## Troubleshooting

### Rules Not Being Followed

1. **Check CLAUDE.md exists:** `ls ~/.claude/CLAUDE.md`
2. **Verify hooks configured:** Check `~/.claude/settings.json`
3. **Test hooks directly:** Run hook scripts manually
4. **Check always-on flag:** `ls ~/.claude/.sena_always_on`

### Hooks Not Executing

1. **Verify executable:** `ls -l ~/.claude/hooks/*.sh` (should show `x` permissions)
2. **Fix permissions:** `chmod +x ~/.claude/hooks/*.sh`
3. **Check bash available:** `which bash` (should return path)
4. **Test in terminal:** Run hook script directly

### False Positives (Blocked Responses)

1. **Check enforcer logic:** `cat ~/.claude/hooks/sena-enforcer.sh`
2. **Temporarily disable:** Comment out hook in settings.json
3. **Debug mode:** Add `set -x` to hook scripts for verbose output

---

## Unicode Reference

### Box-Drawing Characters

```
Double borders: ╔═╗║╚╝
Single borders: ┌─┐│└┘
Connectors: ├┤┬┴┼
Section separators: ════════
```

### Status Emojis

```
✅ Success / Enabled / Good
❌ Error / Disabled / Bad
⚠️  Warning / Caution
🔴 Critical / Error level
ℹ️  Info level
📊 Data / Tables / Stats
🦁 SENA branding
🧠 Thinking
🔍 Verification
💡 Ideas
🎯 Goals
```

---

## Performance Impact

| Metric | Without Hooks | With Hooks | Difference |
|--------|---------------|------------|------------|
| **Startup Time** | ~2s | ~3s | +1s |
| **Response Latency** | <100ms | <150ms | +50ms |
| **Memory Usage** | ~150MB | ~170MB | +20MB |
| **CPU (idle)** | <1% | <2% | +1% |

**Conclusion:** Minimal performance impact for significant quality improvement.

---

## Security

### What Hooks Can Access

- ✅ User's prompt text (read-only)
- ✅ Claude's response text (read-only)
- ✅ Config files (~/.claude/)
- ❌ No network access
- ❌ No sudo/root required
- ❌ No data collection

### Privacy

- **No analytics** - Hooks don't send any data externally
- **Local execution** - Everything runs on your machine
- **Open source** - All code is visible and auditable
- **No telemetry** - SENA doesn't track usage

---

## FAQ

**Q: Do these rules work in Claude Desktop (GUI)?**
A: No, rules are CLI-specific. Desktop uses MCP tools only.

**Q: Can I customize the rules?**
A: Yes, edit `~/.claude/CLAUDE.md` to modify rules.

**Q: Do hooks slow down Claude?**
A: Minimal impact (~50ms per response).

**Q: Can I disable specific rules?**
A: Yes, comment out rules in CLAUDE.md or hooks in settings.json.

**Q: Are hooks required for MCP tools?**
A: No, MCP tools work without hooks. Hooks add enforcement.

**Q: Can hooks break Claude?**
A: No, worst case they block a response (can be disabled).

---

## Related Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture overview
- [FEATURE_COMPATIBILITY.md](FEATURE_COMPATIBILITY.md) - MCP vs Hooks comparison
- [README.md](../README.md) - Main project documentation

---

**SENA 🦁 - Systematic Enhanced Natural Analysis**
