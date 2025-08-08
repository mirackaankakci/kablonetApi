from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base


class MainCategory(Base):
    __tablename__ = "main_category"

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    isActive = Column(Boolean, unique=False, index=True, nullable=False, default=True)
    
    campaigns = relationship("Campaign", back_populates="main_category")
    tariff_categories = relationship("TariffCategory", back_populates="main_category")


