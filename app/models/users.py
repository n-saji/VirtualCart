from sqlalchemy import UUID, Column, TIMESTAMP, String, Enum, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class roles(Enum):
    SELLER = 1
    USER = 2
    BOTH = 3

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID, primary_key=True, nullable=False)
    full_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(Enum(roles), nullable=False, default=roles.USER)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f"<User(full_name='{self.full_name}', email='{self.email}')>"