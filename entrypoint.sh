#!/bin/bash
set -e

if [ "$MODE" = "script" ]; then
    if [ "$DEBUG" = "true" ]; then
        echo "Running $SCRIPT_PATH in DEBUG mode..."
        exec python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m "$SCRIPT_PATH"
    else
        echo "Running $SCRIPT_PATH in normal mode..."
        exec python -m "$SCRIPT_PATH"
    fi

elif [ "$MODE" = "test" ]; then
    export PYTHONPATH=/app:$PYTHONPATH
    if [ "$DEBUG" = "true" ]; then
        echo "Running tests in DEBUG mode on $TEST_PATH..."
        exec python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m pytest -v "$TEST_PATH"
    else
        echo "Running tests on $TEST_PATH..."
        exec pytest -v "$TEST_PATH"
    fi

else
    echo "Unknown MODE: $MODE (expected 'script' or 'test')"
    exit 1
fi
