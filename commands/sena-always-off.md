# Disable SENA Always-On Mode

Deactivating SENA Always-On Mode - returning to keyword-triggered SENA mode.

**Execute this command:**

```bash
rm -f ~/.claude/.sena_always_on
```

**What this does:**
- Removes the always-on flag file
- SENA will only activate on specific keywords (why, how, table, etc.)
- Responses will not have "SENA 🦁" prefix
- Manual activation with `/activate-sena` will still work

**To re-enable:** Use `/sena-always-on` command

SENA Always-On Mode has been disabled. SENA will now activate only on triggers.
