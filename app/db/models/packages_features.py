from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class PackagesFeatures(Base):
    __tablename__ = "packages_features"
    
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    text = Column(String, nullable=False)
    
    is_active = Column(Boolean, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    packages_id = Column(Integer, ForeignKey("packages.id"), nullable=False)
    packages = relationship("Packages", back_populates="packages_features")
    #paket id alınacak