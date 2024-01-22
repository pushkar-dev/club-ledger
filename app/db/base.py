from .session import Base, SessionLocal, engine
from sqlalchemy.orm import Session



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
