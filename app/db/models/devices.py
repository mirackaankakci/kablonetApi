from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Devices(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    device_name = Column(String, nullable=False)
    device_title = Column(String, nullable=False)  # e.g., 'router', 'modem'
    content = Column(String, nullable=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    device_commitments = relationship("DeviceCommitment", back_populates="devices")
    
    main_category_id = Column(Integer, ForeignKey('main_category.id'), nullable=False)
    main_category = relationship("MainCategory", back_populates="devices")