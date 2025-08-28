from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime


class MainCategory(Base):
    __tablename__ = "main_category"

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    campaigns = relationship("Campaign", back_populates="main_category")
    devices = relationship("Devices", back_populates="main_category")
    about_contents = relationship("About_Contents", back_populates="main_category")
    tariff_categories = relationship("TariffCategory", back_populates="main_category")###silinecek 
    packages = relationship("Packages", back_populates="main_category")