from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base


class MainCategory(Base):
    __tablename__ = "main_category"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, nullable=False, unique=True)
    isActive = Column(Boolean, unique=False, index=True, nullable=False)


