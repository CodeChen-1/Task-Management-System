from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.config import settings
from app.database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task Management System", lifespan=lifespan)

@app.get("/")
def root():
    return {"message":" Task Management System API"}