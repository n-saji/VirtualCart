import enum
import uuid

from sqlalchemy import Column, String, Enum, Boolean, DateTime, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class NotificationsType(str, enum.Enum):
    order_update = "order_update"
    message = "message"
    stock_alert = "stock_alert"


class Notifications(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    type = Column(Enum(NotificationsType), nullable=False, default=NotificationsType.order_update)
    message = Column(String(128), nullable=False)
    is_read = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
