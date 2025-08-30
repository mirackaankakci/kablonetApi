from sqlalchemy import Column, Integer, String, DateTime,Boolean, Index
from app.db.base import Base
from datetime import datetime


class channel_list(Base):
    __tablename__ = "chanel_list"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    channel_no = Column(Integer, nullable=False)
    channel_name = Column(String, nullable=False)
    digital_frequency = Column(String, nullable=True)
    analog_frequency = Column(String, nullable=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    #sadece postgre destekliyor
    __table_args__ = (
        Index('idx_unique_active_channel_no', 'channel_no', unique=True, postgresql_where=(is_active == True)),
        Index('idx_unique_active_channel_name', 'channel_name', unique=True, postgresql_where=(is_active == True)),
    )