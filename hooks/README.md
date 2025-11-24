# 🦁 SENA Hook System

**CLI-Only Features for Claude Code (Terminal)**

---

## Overview

The SENA hook system provides **CLI-specific enhancements** for Claude Code (terminal interface). These hooks intercept user input and Claude responses to enforce SENA rules, inject formatted output, and provide automation features.

**IMPORTANT:** Hooks only work in **Claude Code CLI** (terminal). They do NOT work in Claude Desktop (GUI).

---

## 📦 What's Included

| Hook File | Size | Purpose | Type |
|-----------|------|---------|------|
| **user-prompt-submit.sh** | 12.2KB | Pre-processes user input | Pre-Hook |
| **sena-enforcer.sh** | 4.5KB | Validates Claude output | Post-Hook |
| **post-tool-use.sh** | 1.1KB | Suppresses tool output | Post-Hook |
| **permission-request.sh** | 1.7KB | Dynamic tool permissions | Permission |
| **conversation-progress.sh** | 0.7KB | Conversation progress bars | Progress |
| **auto-progress.sh** | 0.6KB | Auto progress display | Progress |

---

## 🔧 Hook Capabilities

### 1. user-prompt-submit.sh (Pre-Processing Hook)

**Triggers BEFORE Claude sees your message**

Features:
- ✅ **Rule 0 Enforcement:** Reminds Claude to use "SENA 🦁" prefix when always-on mode active
- ✅ **Auto-Format Injection:** Automatically applies SENA formats based on keywords:
  - "why/how/explain" → Brilliant Thinking Format (Rule 2)
  - "table/tabular" → Table Format (Rule 1)
  - "is X true/fact check" → Truth Verification (Rule 3)
  - "analyze code/review" → Code Analysis (Rule 4)
- ✅ **Progress Bar Injection:** Shows initial progress bar for multi-step operations (Rule 6)
- ✅ **SENA Status Detection:** Provides correct method for checking SENA status

**Keywords Detected:**
```bash
# Brilliant Thinking
why, how, explain, what causes, what makes, how come

# Table Format
table, tabular, tabular format, in table form

# Truth Verification
is X true, fact check, verify that, confirm that

# Code Analysis
analyze code, review code, check code, examine code, refactor, debug

# Progress Injection
search, find, scan, check, analyze, all, every, multiple, files
```

**Example Output:**
```
═══════════════════════════════════════════════════════════════════
🦁🦁🦁 SENA ALWAYS-ON MODE ACTIVE 🦁🦁🦁
═══════════════════════════════════════════════════════════════════

🔴 CRITICAL SYSTEM RULE - READ THIS FIRST

BEFORE you respond, you MUST:
1. Start your ENTIRE response with exactly: **SENA 🦁**

[additional enforcement reminders...]
```

---

### 2. sena-enforcer.sh (Post-Processing Hook)

**Validates AFTER Claude generates response**

Features:
- ✅ **Always-On Mode Validation:** Blocks responses missing "SENA 🦁" prefix
- ✅ **Format Compliance:** Ensures SENA formats were used when triggered
- ✅ **Clean Output Processing:** Processes responses through 100% controller
- ✅ **Completion Progress:** Auto-injects completion progress bar (100%)

**Enforcement Rules:**
1. If always-on mode active → Response MUST start with "SENA 🦁"
2. If user asked "why/how" → Response MUST contain "SENA BRILLIANT THINKING"
3. If user asked for "table" → Response MUST contain "SENA BEAUTIFUL UI"
4. If multi-step operation → Append completion progress bar

**Violation Handling:**
```bash
⚠️  SENA ALWAYS-ON MODE VIOLATION

Always-On mode is active but response missing 'SENA 🦁' prefix.

🔴 MANDATORY REQUIREMENT:
Every response must start with: **SENA 🦁**

This is a SYSTEM-LEVEL enforcement. Response blocked.
```

---

### 3. post-tool-use.sh (Tool Output Control)

**Suppresses verbose tool output for clean display**

Features:
- ✅ Suppresses Bash tool output (no verbose command execution logs)
- ✅ Suppresses SENA tool output (only results shown)
- ✅ Uses official `suppressOutput` feature from Claude Code

**Example:**
```json
{
  "continue": true,
  "suppressOutput": true,
  "systemMessage": null
}
```

This keeps the terminal clean by hiding internal tool execution details.

---

### 4. permission-request.sh (Dynamic Tool Permissions)

**Controls which tools Claude can use at runtime**

Features:
- ✅ Allow/deny tools without restart
- ✅ Reads from `~/.claude/.sena_tool_permissions.json`
- ✅ Defaults to "allow" if not configured

**Configuration File:**
```json
{
  "tools": {
    "Bash": {
      "enabled": true,
      "reason": "Required for system operations"
    },
    "Write": {
      "enabled": false,
      "reason": "Prevent accidental file overwrites"
    }
  }
}
```

**Usage:**
```bash
# Create permissions file
cat > ~/.claude/.sena_tool_permissions.json << 'EOF'
{
  "tools": {
    "Bash": {"enabled": true},
    "Write": {"enabled": false}
  }
}
EOF

# Changes apply immediately (no restart needed)
```

---

### 5. conversation-progress.sh (Conversation Progress)

**Shows progress bar for each conversation**

Features:
- ✅ Runs `sena_live_progress.py` in background
- ✅ 5-second display timeout
- ✅ Automatic cleanup

**Note:** Requires `sena_live_progress.py` to be present in `~/.claude/`

---

### 6. auto-progress.sh (Auto Progress Display)

**Automatically shows progress for all conversations**

Features:
- ✅ Auto-starts progress bar for every conversation
- ✅ Prevents duplicate progress bars (kills existing)
- ✅ 10-second timeout
- ✅ Graceful termination

**Note:** Requires `sena_live_progress.py` to be present in `~/.claude/`

---

## 🚀 Installation

### Prerequisites

1. **Claude Code CLI** - Hooks only work in terminal (not Claude Desktop)
2. **Bash** - All hooks are Bash scripts
3. **Python 3** - Required for JSON parsing in hooks
4. **SENA MCP Server** - Already installed if you're reading this

### Installation Steps

#### Option 1: Automatic Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/Sena1996/sena-mcp-server.git
cd sena-mcp-server

# Run installer (installs both MCP server and hooks)
bash install.sh
```

The installer will:
1. Install MCP server via `uv`
2. Copy hooks to `~/.claude/hooks/`
3. Configure `~/.claude/settings.json` with hook entries
4. Set executable permissions

#### Option 2: Manual Installation

```bash
# 1. Copy hooks to Claude Code hooks directory
mkdir -p ~/.claude/hooks
cp hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 2. Add hook configuration to ~/.claude/settings.json
```

Add these entries to your `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "sena": {
      "command": "uv",
      "args": ["--directory", "/path/to/sena-mcp-server", "run", "sena-mcp-server"]
    }
  },
  "hooks": {
    "userPromptSubmit": "~/.claude/hooks/user-prompt-submit.sh",
    "assistantResponseSubmit": "~/.claude/hooks/sena-enforcer.sh",
    "postToolUse": "~/.claude/hooks/post-tool-use.sh",
    "permissionRequest": "~/.claude/hooks/permission-request.sh"
  }
}
```

**Note:** Progress hooks (conversation-progress.sh, auto-progress.sh) are optional and require additional setup.

---

## ⚙️ Configuration

### Enable SENA Always-On Mode

```bash
# Create always-on flag file
touch ~/.claude/.sena_always_on
```

**Effect:** Every Claude response will start with "SENA 🦁" prefix. This is enforced by:
1. `user-prompt-submit.sh` - Reminds Claude to add prefix
2. `sena-enforcer.sh` - Blocks responses without prefix

### Disable SENA Always-On Mode

```bash
# Remove always-on flag file
rm ~/.claude/.sena_always_on
```

### Configure Tool Permissions

```bash
# Create tool permissions file
cat > ~/.claude/.sena_tool_permissions.json << 'EOF'
{
  "tools": {
    "Bash": {"enabled": true},
    "Write": {"enabled": true},
    "Edit": {"enabled": true},
    "Read": {"enabled": true},
    "Glob": {"enabled": true},
    "Grep": {"enabled": true}
  }
}
EOF
```

---

## 🧪 Testing

### Test Hook Installation

```bash
# 1. Check hooks are installed
ls -la ~/.claude/hooks/

# Expected output:
# user-prompt-submit.sh (executable)
# sena-enforcer.sh (executable)
# post-tool-use.sh (executable)
# permission-request.sh (executable)

# 2. Check hooks are configured
cat ~/.claude/settings.json | grep -A 10 "hooks"

# Expected: Hook entries pointing to ~/.claude/hooks/*.sh

# 3. Test always-on mode
touch ~/.claude/.sena_always_on

# Start Claude Code CLI and ask any question
# Response should start with: **SENA 🦁**
```

### Test Auto-Format Triggers

```bash
# Open Claude Code CLI

# Test 1: Brilliant Thinking
"Why is the sky blue?"
# Should trigger: SENA BRILLIANT THINKING format

# Test 2: Table Format
"Give me planets info in table"
# Should trigger: Unicode table format

# Test 3: Truth Verification
"Is Python faster than C++?"
# Should trigger: SENA TRUTH VERIFICATION format

# Test 4: Code Analysis
"Analyze this code: print('hello')"
# Should trigger: SENA CODE QUALITY ANALYSIS format
```

---

## 🔍 Troubleshooting

### Hooks Not Working

**Problem:** Hooks don't seem to execute

**Solutions:**
1. **Check executable permissions:**
   ```bash
   chmod +x ~/.claude/hooks/*.sh
   ```

2. **Verify settings.json syntax:**
   ```bash
   cat ~/.claude/settings.json | python3 -m json.tool
   # Should show valid JSON, no errors
   ```

3. **Check hook paths are correct:**
   ```bash
   # In settings.json, paths should be absolute
   "userPromptSubmit": "~/.claude/hooks/user-prompt-submit.sh"
   # Or: "/Users/yourname/.claude/hooks/user-prompt-submit.sh"
   ```

4. **Test hook directly:**
   ```bash
   echo '{"prompt": "test"}' | ~/.claude/hooks/user-prompt-submit.sh
   # Should output reminders/formats
   ```

### Always-On Mode Not Working

**Problem:** Responses don't have "SENA 🦁" prefix

**Solutions:**
1. **Check flag file exists:**
   ```bash
   ls -la ~/.claude/.sena_always_on
   # Should exist
   ```

2. **Check hooks are installed:**
   ```bash
   cat ~/.claude/settings.json | grep userPromptSubmit
   cat ~/.claude/settings.json | grep assistantResponseSubmit
   # Both should point to hook files
   ```

3. **Test enforcement manually:**
   ```bash
   # Create flag file
   touch ~/.claude/.sena_always_on

   # Restart Claude Code CLI
   # Ask any question
   # Response MUST start with "SENA 🦁"
   ```

### Progress Bars Not Showing

**Problem:** No progress bars appear

**Note:** Progress hooks (conversation-progress.sh, auto-progress.sh) require `sena_live_progress.py` which is part of local SENA v3.3.1 but NOT included in this repository.

**Solutions:**
1. **Disable progress hooks if not needed:**
   - Remove from `~/.claude/settings.json`
   - Or comment out in hooks file

2. **Install full SENA v3.3.1 for progress features:**
   - Progress bars require Python progress script
   - This is CLI-specific local feature

### Python Import Errors

**Problem:** Hooks show Python import errors

**Cause:** Hooks reference local SENA v3.3.1 Python modules:
```python
sys.path.insert(0, '/Users/sena/.claude/sena_controller_v3.0')
from sena_auto_format import auto_apply_format
```

**Solutions:**
1. **For public use:** Comment out auto-format sections (lines 96-107, 119-130, etc.)
2. **For personal use:** Install full SENA v3.3.1 locally
3. **Minimal hooks:** Use only core enforcement without auto-formatting

---

## 📊 Hook Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Input                           │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  user-prompt-submit.sh (Pre-Hook)                       │
│  • Detect keywords (why/how/table/fact)                 │
│  • Inject SENA reminders                                │
│  • Auto-apply formats                                   │
│  • Add progress bars                                    │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│              Claude Processes Request                    │
│              (MCP tools available)                       │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  post-tool-use.sh (Post-Tool Hook)                      │
│  • Suppress verbose tool output                         │
│  • Clean display                                        │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  Claude Generates Response                              │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│  sena-enforcer.sh (Post-Response Hook)                  │
│  • Validate "SENA 🦁" prefix                            │
│  • Check format compliance                              │
│  • Process through 100% controller                      │
│  • Add completion progress                              │
└──────────────────┬──────────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────────┐
│                  Display to User                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Use Cases

### Use Hooks When:

1. **You use Claude Code CLI** (terminal interface)
2. **You want automatic SENA formatting** (triggered by keywords)
3. **You want enforced "SENA 🦁" branding** (always-on mode)
4. **You want clean terminal output** (no verbose tool logs)
5. **You want progress bars** for multi-step operations
6. **You want dynamic tool permissions** (runtime control)

### Don't Use Hooks When:

1. **You use Claude Desktop** (GUI) - Hooks don't work there
2. **You prefer manual control** - Hooks auto-trigger formats
3. **You want minimal setup** - MCP server alone is simpler

---

## 🆚 Hooks vs MCP

| Feature | MCP Server | Hook System | Best For |
|---------|------------|-------------|----------|
| **Environment** | Desktop + CLI | CLI only | MCP = Universal |
| **Auto-formatting** | Manual call | Auto-trigger | Hooks = Automation |
| **"SENA 🦁" Prefix** | Optional | Enforced (when enabled) | Hooks = Branding |
| **Progress Bars** | Manual | Auto-inject | Hooks = UX |
| **Tool Output** | Verbose | Suppressed | Hooks = Clean |
| **Setup Complexity** | Simple | Moderate | MCP = Easier |
| **User Control** | Full control | Automated | MCP = Flexibility |

**Recommendation:** Use both for maximum features:
- MCP provides intelligence (tools + knowledge bases)
- Hooks provide automation (triggers + enforcement)

---

## 📝 Hook Reference

### user-prompt-submit.sh

**Purpose:** Pre-process user input before Claude sees it

**Hook Type:** `userPromptSubmit`

**Environment Variables Used:**
- `HOME` - User home directory
- `SENA_IDE_MODE` - IDE mode detection
- `SENA_CLEAN_OUTPUT` - Clean output flag

**Files Checked:**
- `~/.claude/.sena_always_on` - Always-on mode flag

**JSON Input Format:**
```json
{
  "prompt": "user message here"
}
```

**Output:** Injected reminders and formats to stdout

---

### sena-enforcer.sh

**Purpose:** Validate Claude response for SENA compliance

**Hook Type:** `assistantResponseSubmit`

**JSON Input Format:**
```json
{
  "response": "Claude's response",
  "userMessage": "original user message",
  "prompt": "original user message (fallback)"
}
```

**Exit Codes:**
- `0` - Response valid, continue
- `1` - Response blocked, violation detected

---

### post-tool-use.sh

**Purpose:** Control tool output display

**Hook Type:** `postToolUse`

**JSON Input Format:**
```json
{
  "tool_name": "Bash",
  "exit_code": 0
}
```

**JSON Output Format:**
```json
{
  "continue": true,
  "suppressOutput": true,
  "systemMessage": null
}
```

---

### permission-request.sh

**Purpose:** Dynamic tool permission control

**Hook Type:** `permissionRequest`

**Files Used:**
- `~/.claude/.sena_tool_permissions.json` - Permissions config

**Output:** `allow` or `deny`

---

## 🤝 Contributing

Want to improve the hooks? Here's how:

1. **Fork the repository**
2. **Test hooks thoroughly** - They run on every interaction
3. **Document changes** - Update this README
4. **Avoid breaking changes** - Backwards compatibility matters
5. **Submit PR** - Include test cases

**Guidelines:**
- Keep hooks lightweight (fast execution)
- Use Bash best practices (error handling, quoting)
- Document all environment variables
- Test on macOS and Linux
- No external dependencies beyond Python 3

---

## 📚 Additional Resources

- [SENA MCP Server README](../README.md) - Main project documentation
- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) - System architecture
- [FEATURE_COMPATIBILITY.md](../docs/FEATURE_COMPATIBILITY.md) - MCP vs Hooks comparison
- [CLAUDE_CLI_RULES.md](../docs/CLAUDE_CLI_RULES.md) - Complete SENA rules documentation

---

## ⚠️ Important Notes

1. **CLI-Only:** Hooks DO NOT work in Claude Desktop (GUI)
2. **Requires Claude Code:** Terminal-based Claude interface only
3. **Python Dependencies:** Some hooks reference local SENA v3.3.1 Python modules
4. **Optional Feature:** You can use SENA MCP server without hooks
5. **No Restart Needed:** Most hook changes apply immediately
6. **Performance Impact:** Minimal (hooks execute in milliseconds)

---

## 🔐 Security Considerations

**Hooks run arbitrary Bash code on every interaction. Security notes:**

1. **Code Review:** Always review hook code before installation
2. **Trusted Source:** Only install hooks from trusted repositories
3. **File Permissions:** Hooks should be owned by you (`chmod 700`)
4. **No Network Access:** SENA hooks don't make network requests
5. **Local Only:** Hooks read/write local files only
6. **Open Source:** All code is visible and auditable

---

## 📄 License

MIT License - Same as SENA MCP Server

---

**SENA 🦁 Hook System - Bringing Intelligence to the Command Line**

**Version:** 1.2.0
**Last Updated:** November 24, 2025
**Compatibility:** Claude Code CLI (Terminal)
