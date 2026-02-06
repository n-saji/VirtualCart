import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class CartStatus(str, enum.Enum):
    active = "active"
    check_out = "check_out"


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    cart_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    status = Column(Enum(CartStatus), nullable=False, default=CartStatus.active)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
