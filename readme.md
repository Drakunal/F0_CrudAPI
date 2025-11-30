---

# F0 CRUD API — FastAPI + SQLite (Mac + Termux Mobile Server)

A minimal, production-minded **FastAPI + SQLite CRUD API**, designed to verify that your environment works correctly on **macOS**, and even when running your **Android phone as a server using Termux**.

This project keeps things intentionally simple and modular while demonstrating correct usage of:

* FastAPI
* SQLAlchemy (Declarative Base)
* SQLite with absolute paths
* Modern FastAPI `lifespan` event
* Pydantic v2 schemas
* Modular routers
* tmux-based persistence for mobile servers

Use this project as a starting point for testing environments or building small backend services.

---

## 🚀 Features

* `Item` CRUD API (Create, Get All, Get by ID)
* SQLite DB auto-created at: `data/items.db`
* Absolute DB path → prevents “no such table” errors
* API runs on **macOS**, **Linux**, and **Android** (via Termux)
* `tmux` support → API continues running even after closing SSH
* Includes helpful scripts:

  * `run_uvicorn.sh`
  * `start_server.sh` (runs uvicorn inside tmux auto-session)

---

## 📂 Folder Structure

```
f0_crud/
├─ app/
│  ├─ main.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ crud.py
│  ├─ session.py
│  └─ routes/
│     └─ items.py
├─ data/                  # auto-created SQLite DB
├─ requirements.txt
├─ run_uvicorn.sh
└─ start_server.sh
```

---

## 🧰 Requirements

Python 3.10+
FastAPI
SQLAlchemy
Uvicorn
Termux (optional, for running API on Android)

Install dependences:

```bash
pip install -r requirements.txt
```

---

# 🔥 Quickstart — macOS

Clone and setup:

```bash
git clone <repo-url> f0_crud
cd f0_crud

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open in browser:

```
http://127.0.0.1:8000
http://127.0.0.1:8000/docs
```

---

# 📱 Running on Android via Termux (Mobile as Server)

Your mobile can act as a real backend server.
This setup is useful for:

* portable APIs
* offline demos
* local network experiments
* running agents / IoT controllers

Termux provides a full Linux-like environment.

## 1. Install dependencies

```bash
pkg update
pkg install python git tmux -y
```

## 2. Clone project in Termux

```bash
git clone <repo-url> f0_crud
cd f0_crud

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt
```

## 3. Run server inside tmux (so it keeps running)

```bash
tmux new -s f0crud
```

Inside tmux:

```bash
cd ~/f0_crud
source env/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Detach while keeping server alive:

```
Ctrl + b  then  d
```

Reattach any time:

```bash
tmux attach -t f0crud
```

## 4. Access the API from your laptop

Find phone IP:

```bash
ip addr show wlan0
```

Open in browser:

```
http://<phone-ip>:8000
http://<phone-ip>:8000/docs
```

---

# 🗄 SQLite DB Location and Persistence

The DB file is stored at:

```
data/items.db
```

It persists across:

* tmux detach
* SSH disconnect
* Termux close
* Reboot (unless you delete the folder)

To inspect the DB:

```bash
sqlite3 data/items.db
.tables
SELECT * FROM items;
```

---

# 🧪 Testing Endpoints (Swagger & Postman)

Swagger UI:

```
http://<host>:8000/docs
```

Example Postman requests:

### Create item

POST `/items`

```json
{
  "name": "Milk",
  "description": "Cat food item"
}
```

### Get all items

GET `/items`

### Get one item

GET `/items/2`

---

# ▶️ start_server.sh (recommended script)

This script:

* activates virtualenv
* starts tmux session `f0crud`
* runs uvicorn inside it
* attaches to tmux

**Usage:**

```bash
chmod +x start_server.sh
./start_server.sh
```

Detach:

```
Ctrl + b then d
```

Reattach later:

```bash
tmux attach -t f0crud
```

---

# 🌍 Exposing API to the Internet (optional)

**Local network access works automatically** when using:

```
--host 0.0.0.0
```

For public access, you have options:

### 1. Ngrok (easiest)

```bash
ngrok http 8000
```

### 2. SSH reverse tunnel

From Termux:

```bash
ssh -R 9000:localhost:8000 user@public-server
```

### 3. Router port forwarding

(Only if you control the router.)

⚠️ Do not expose dev APIs publicly without authentication.

---

# 🛠 Troubleshooting

| Issue                         | Fix                                                                   |
| ----------------------------- | --------------------------------------------------------------------- |
| Cannot connect from laptop    | Phone & laptop must be on same network; use `ip addr`; check firewall |
| “No such table”               | DB path is absolute; ensure app created tables on startup             |
| Server stops when SSH closes  | Always run inside tmux or use start_server.sh                         |
| Phone sleeps and kills server | Use `termux-wake-lock` or enable wakelock                             |

---

# 🔐 Security Notes

* This API is **not** secured — do not expose in production.
* Add API keys or JWT for real use.
* Use HTTPS when deploying outside local network.

---

# 📄 Suggested .gitignore

```
env/
__pycache__/
*.pyc
*.db
*.sqlite3
.DS_Store
.vscode/
uvicorn.log
nohup.out
```

---

# 📜 License

MIT License — you may use this project freely for personal or commercial projects.

---