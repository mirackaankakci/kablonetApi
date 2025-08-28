from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Channels(Base):
    __tablename__ = "channels"
    
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    image= Column(String, nullable=False)
    
    is_active = Column(Boolean, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    #kanal kategori id si gelecek
    channel_category_id = Column(Integer, ForeignKey('channel_category.id'), nullable=True)
    channel_category = relationship("ChannelCategory", back_populates="channels")
    
    #paket kanal ile ilişkisi var
    packages_channels = relationship("PackagesChannels", back_populates="channels")