import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, func, Float
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class OrderStatus(str, enum.Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Orders(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    buyer_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    total_amount = Column(Float, nullable=False, default = 0.0)
    status = Column(Enum(OrderStatus), nullable=False, default=OrderStatus.active)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
