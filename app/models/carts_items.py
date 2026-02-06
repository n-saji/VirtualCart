import uuid

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class CartItems(Base):
    __tablename__ = "cart_items"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    cart_id = Column(ForeignKey("carts.id"), nullable=False)
    product_id = Column(ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
    price_at_time = Column(Float, nullable=False, default=0)