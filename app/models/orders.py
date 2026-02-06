import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, func, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from sqlalchemy.orm import Mapped, relationship


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    buyer_id = Column(ForeignKey("users.id"), nullable=False)
    total_amount = Column(Float, nullable=False, default = 0.0)
    status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.pending)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    buyer: Mapped["User"] = relationship("User", back_populates="orders")
