# SENA Autonomous Skills Framework

**Version:** 3.3.1
**Phase:** 3 - Autonomous Capabilities
**Purpose:** Proactive intelligent assistance

---

## Overview

This directory contains **autonomous skills** that trigger automatically based on context, without explicit user requests.

## How It Works

1. **Detection:** SENA monitors code/context for specific patterns
2. **Trigger:** When conditions match, skill activates automatically
3. **Execution:** Skill runs and provides assistance
4. **Feedback:** User can accept/reject/configure

## Available Skills

### 1. Auto Code Review (`auto-code-review.md`)
**Triggers:** After writing significant code (>50 lines)
**Purpose:** Automatic code quality analysis
**Actions:**
- Check code quality
- Verify best practices
- Suggest improvements
- Identify common issues

### 2. Auto Optimize (`auto-optimize.md`)
**Triggers:** O(n²) or worse complexity detected
**Purpose:** Performance optimization suggestions
**Actions:**
- Identify bottlenecks
- Suggest optimizations
- Show complexity improvements
- Provide optimized code

### 3. Auto Security Scan (`auto-security-scan.md`)
**Triggers:** User input, SQL, file ops, auth code
**Purpose:** Security vulnerability detection
**Actions:**
- Scan for OWASP Top 10
- Check input validation
- Verify SQL safety
- Suggest security fixes

## Skill Activation

Skills activate automatically when:
- **Confidence:** >80% that skill is relevant
- **Context:** Appropriate situation detected
- **Frequency:** Within configured limits

## Configuration

Edit `~/.claude/sena_skills.json` to:
- Enable/disable skills
- Adjust trigger thresholds
- Set frequency limits
- Configure preferences

## Creating New Skills

Skills are markdown files with:
1. **Trigger Conditions** - When to activate
2. **Analysis Logic** - What to check
3. **Recommendations** - What to suggest
4. **Examples** - Usage demonstrations

## Best Practices

- ✅ Skills should be helpful, not annoying
- ✅ High confidence threshold for auto-trigger
- ✅ Clear, actionable recommendations
- ✅ Respect user preferences and frequency limits

---

*Updated: November 23, 2025*
*SENA v3.3.1 - Phase 3*
