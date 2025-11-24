# SENA v3.0 - Python Startup Hook
# Auto-loads SENA transparently

import sys
from pathlib import Path

# Add SENA to path
controller_path = Path.home() / '.claude' / 'sena_controller_v3.0'
if str(controller_path) not in sys.path:
    sys.path.insert(0, str(controller_path))

# Auto-load SENA transparent layer
try:
    from sena_transparent_layer import transparent_sena
    # Silently activate SENA
    transparent_sena.ensure_active()
except Exception:
    # Fail silently if SENA not available
    pass

