from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Packages(Base):
    __tablename__ = "packages"
    
    id= Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    title= Column(String, nullable=False)
    content= Column(String, nullable=False)
    price=Column(Integer, nullable=False)
    detail=Column(String, nullable=False)
    
    is_active = Column(Boolean, unique=False, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    #main kategory id alınacak
    main_category_id = Column(Integer, ForeignKey('main_category.id'), nullable=False)
    main_category = relationship("MainCategory", back_populates="packages")
    
    #paket özellikleri ile ilişkisi var
    packages_features = relationship("PackagesFeatures", back_populates="packages")
    
    #paket kategori id alınacak
    packages_category_id = Column(Integer, ForeignKey("packages_category.id"), nullable=False)
    packages_category = relationship("PackagesCategory", back_populates="packages")
    
    #Paket kanal ile ilişkisi var
    packages_channels = relationship("PackagesChannels", back_populates="packages")