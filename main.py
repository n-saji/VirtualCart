from fastapi import FastAPI
from app.db.init_db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Virtual Cart API",lifespan=lifespan)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Virtual Cart API!"}


# run: uvicorn main:app --reload