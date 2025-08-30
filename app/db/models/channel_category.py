from sqlalchemy import Column, Integer, String, Boolean, DateTime, Index
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class ChannelCategory(Base):
    __tablename__ = "channel_category"

    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    
    is_active = Column(Boolean, index=True, nullable=False, default=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    
    
    #kanallar ile ilişkisi var
    channels= relationship("Channels", back_populates="channel_category")
    
    __table_args__ = (
        Index('idx_unique_active_channel_category_name', 'name', unique=True, postgresql_where=(is_active == True)),
    )