# Enable SENA Always-On Mode

Activating SENA Always-On Mode - SENA will be your default operating mode for ALL responses.

**Execute this command:**

```bash
touch ~/.claude/.sena_always_on && echo "enabled" > ~/.claude/.sena_always_on
```

**What this does:**
- Creates the always-on flag file
- Every response will start with "SENA 🦁"
- SENA Smart UI will be used automatically for all tables and data
- SENA functions will be available in every response
- No need to manually activate SENA with keywords

**To disable:** Use `/sena-always-off` command

SENA 🦁 mode is now your default. Enjoy consistent, powerful AI responses!
