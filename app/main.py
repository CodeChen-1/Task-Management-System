from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

from app.config import settings
from app.database import Base, engine
from app.routes import auth, tasks

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task Management System", lifespan=lifespan)
app.include_router(auth.router)
app.include_router(tasks.router)

app.mount("/", StaticFiles(directory="static", html=True, name="static"))

@app.get("/")
def root():
    return {"message":" Task Management System API"}