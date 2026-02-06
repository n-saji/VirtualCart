import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class CartStatus(str, enum.Enum):
    active = "active"
    check_out = "check_out"


class Carts(Base):
    __tablename__ = "carts"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    status = Column(Enum(CartStatus), nullable=False, default=CartStatus.active)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
