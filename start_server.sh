#!/usr/bin/env bash

# ---------------------------------------------
# Start FastAPI inside a tmux session (f0crud)
# Works on Mac + Termux
# ---------------------------------------------

SESSION="f0crud"

# Navigate to project root (where this script is)
cd "$(dirname "$0")"

# Activate virtual environment
if [ -d "env" ]; then
    source env/bin/activate
else
    echo "❌ Virtual environment not found. Run:"
    echo "python3 -m venv env && source env/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Check if tmux session already exists
tmux has-session -t $SESSION 2>/dev/null

if [ $? != 0 ]; then
    echo "🟢 Creating new tmux session: $SESSION"
    # Create session and run uvicorn inside it
    tmux new-session -d -s $SESSION "uvicorn app.main:app --host 0.0.0.0 --port 8000"
    echo "🚀 FastAPI started in tmux session: $SESSION"
else
    echo "🔄 Tmux session already exists. Attaching..."
fi

# Attach to the session
tmux attach -t $SESSION
