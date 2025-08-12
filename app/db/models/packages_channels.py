from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class PackagesChannels(Base):
    __tablename__ = "packages_channels"
    
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    #kannal-id alınacak
    channels_id = Column(Integer, ForeignKey('channels.id'), nullable=True)
    channels = relationship("Channels", back_populates="packages_channels")
    
    #paketler-id alınacak
    packages_id = Column(Integer, ForeignKey('packages.id'), nullable=True)
    packages = relationship("Packages", back_populates="packages_channels")
    