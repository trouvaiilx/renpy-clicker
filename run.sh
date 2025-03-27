#!/bin/bash
VENV_PATH="$HOME/venv"
PYTHON="$VENV_PATH/bin/python"
SCRIPT_PATH="$(dirname "$0")/shift_clicker.py"

if [ ! -f "$PYTHON" ]; then
    echo "Error: Python interpreter not found in $PYTHON"
    exit 1
fi

if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $SCRIPT_PATH"
    exit 1
fi

"$PYTHON" "$SCRIPT_PATH"
