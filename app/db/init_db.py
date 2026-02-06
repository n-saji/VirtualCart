from app.db.base import Base
from app.db.session import engine

from app.models.users import User
from app.models.products import Product

# Add other model imports here

def init_db():
    Base.metadata.create_all(bind=engine)

