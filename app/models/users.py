from sqlalchemy import  Column, String, Enum, Boolean, func, DateTime
from app.db.base import Base
import enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship,mapped_column,Mapped
from app.models.products import Products
from app.models.notifications import Notifications
from app.models.orders import Orders


class UserRole(str, enum.Enum):
    seller = "seller"
    buyer = "buyer"
    both = "both"

class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    full_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), nullable=False, default=UserRole.buyer)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    # Relationships
    products: Mapped[list["Products"]] = relationship("Products", back_populates="seller")
    orders: Mapped[list["Orders"]] = relationship("Orders", back_populates="buyer")
    notifications: Mapped[list["Notifications"]] = relationship("Notifications", back_populates="user")