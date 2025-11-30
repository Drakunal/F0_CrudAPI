#!/usr/bin/env bash
# small helper script to run uvicorn (make executable: chmod +x run_uvicorn.sh)
# On Mac (localhost):
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
# For Termux (use 0.0.0.0 if you want external network access):
# uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
