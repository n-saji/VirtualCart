import enum
import uuid

from sqlalchemy import Column, Float, Integer
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    order_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    seller_id = Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    quantity = Column(Integer, nullable=False, default = 0)
    price = Column(Float, nullable=False, default = 0.0)