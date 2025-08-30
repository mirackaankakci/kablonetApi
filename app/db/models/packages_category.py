from sqlalchemy import Column, Integer, String, Boolean, DateTime, Index
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class PackagesCategory(Base):
    __tablename__ = "packages_category"
    
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    
    is_active = Column(Boolean, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    packages = relationship("Packages", back_populates="packages_category")
    #paketler ile ilişkisi var
    
    __table_args__ = (
        Index('idx_unique_active_packages_category_name', 'name', unique=True, postgresql_where=(is_active == True)),
        )