from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

#cihaz taahütname tablosu
class DeviceCommitment(Base):
    __tablename__ = "device_commitment"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    price = Column(Integer, nullable=False)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    devices_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    devices = relationship("Devices", back_populates="device_commitments")
    
    commitment_period_id = Column(Integer, ForeignKey('commitment_period.id'), nullable=False)
    commitment_period = relationship("CommitmentPeriod", back_populates="device_commitments")