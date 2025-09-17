from app.db.database import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    """Database dependency for FastAPI"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
