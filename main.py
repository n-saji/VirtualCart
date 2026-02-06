from fastapi import FastAPI
from app.db.init_db import init_db
from contextlib import asynccontextmanager
from app.api.v1 import router as api_v1_router
from fastapi.middleware.cors import CORSMiddleware
# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Virtual Cart API",lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Virtual Cart API!"}
# Include API v1 routes
app.include_router(api_v1_router)




# run: uvicorn main:app --reload