import uuid
from sqlalchemy import (
    Column, String, Text, Boolean, Integer, Float,
    DateTime, func, UniqueConstraint
)
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    seller_id = Column(UUID(as_uuid=True), nullable=False, index=True)
    category_id = Column(UUID(as_uuid=True), nullable=False, index=True)

    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)

    price = Column(Float, nullable=False)
    quantity_available = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, nullable=False, default=True)

    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

