from fastapi import APIRouter, Depends, HTTPException
from app.api.v1.users import router as users_router

router = APIRouter(prefix="/v1")
router.include_router(users_router)