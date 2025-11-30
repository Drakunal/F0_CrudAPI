from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Absolute DB path (project root / data / items.db)
# This prevents "no such table" when running from different working directories.
BASE_DIR = Path(__file__).resolve().parent.parent  # project root (f0_crud/)
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_FILE = DATA_DIR / "items.db"
# For SQLAlchemy: sqlite:///relative and sqlite:////absolute. Using f"sqlite:///{DB_FILE}" yields sqlite:////abs/path
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

# echo=False for production-like silent behavior; set True for debugging
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # required for SQLite + threads
    echo=False,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
