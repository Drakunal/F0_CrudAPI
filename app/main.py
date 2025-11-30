from fastapi import FastAPI
from contextlib import asynccontextmanager

from .session import engine
from .models import Base
from .routes import items as items_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Called when the app starts. Create tables here.
    # This ensures the DB file and tables exist before serving requests.
    Base.metadata.create_all(bind=engine)
    yield
    # (optionally) add shutdown logic here

app = FastAPI(title="F0 CRUD API", lifespan=lifespan)

app.include_router(items_router.router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "CRUD API running"}
