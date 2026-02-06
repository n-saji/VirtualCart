from sqlalchemy import  Column, String, Enum, Boolean, func, DateTime
from app.db.base import Base
import enum
from sqlalchemy.dialects.postgresql import UUID
import uuid


class UserRole(str, enum.Enum):
    seller = "seller"
    buyer = "buyer"
    both = "both"

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    full_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.buyer)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())