#!/bin/bash
# SENA v3.5.0 - Universal Python Executor Hook
# Executes Python modules SILENTLY with NO terminal output
# Returns ONLY the result for internal hook processing

MODULE="$1"
FUNCTION="$2"
shift 2
ARGS="$@"

# Exit if no module specified
if [ -z "$MODULE" ]; then
    exit 0
fi

# Determine Python module path
CONTROLLER_PATH="$HOME/.claude/sena_controller_v3.0"

# Execute Python silently, capture only return value
RESULT=$(python3 <<EOF 2>/dev/null
import sys
import os
sys.path.insert(0, '$CONTROLLER_PATH')

try:
    # Import module dynamically
    module = __import__('$MODULE')

    # Get function if specified
    if '$FUNCTION':
        if hasattr(module, '$FUNCTION'):
            func = getattr(module, '$FUNCTION')

            # Execute function with args
            if '$ARGS':
                result = func('$ARGS')
            else:
                result = func()

            # Print result (captured by RESULT variable)
            if result:
                print(result)
        else:
            # Function not found, try main()
            if hasattr(module, 'main'):
                result = module.main()
                if result:
                    print(result)
    else:
        # No function specified, try main()
        if hasattr(module, 'main'):
            result = module.main()
            if result:
                print(result)

except Exception as e:
    # Silent failure - return nothing
    pass
EOF
)

# Return result to hook system (internal only)
# NO output to user terminal
echo "$RESULT"
