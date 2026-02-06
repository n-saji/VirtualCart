from app.db.base import Base
from app.db.session import engine
import app.models


# Add other model imports here

def init_db():
    Base.metadata.create_all(bind=engine)

