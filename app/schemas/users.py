from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
from enum import Enum
from datetime import datetime

class UserRole(str, Enum):
    seller = "seller"
    buyer = "buyer"
    both = "both"

class UserCreate(BaseModel):
    full_name: str = Field(..., max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: UserRole = UserRole.buyer

class UserResponse(BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True