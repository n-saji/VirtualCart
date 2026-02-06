import uuid

from sqlalchemy import Column, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    order_id = Column(ForeignKey("orders.id"), nullable=False)
    product_id = Column(ForeignKey("products.id"), nullable=False)
    seller_id = Column(ForeignKey("users.id"), nullable=False)
    
    quantity = Column(Integer, nullable=False, default = 0)
    price = Column(Float, nullable=False, default = 0.0)