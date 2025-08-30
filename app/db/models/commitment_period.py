from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

# taahüt süresi tablosu
class CommitmentPeriod(Base):
    __tablename__ = "commitment_period"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    period= Column(String, nullable=False)  # taahüt süresi (örneğin: "12 months")
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    campaign_commitments = relationship("CampaignCommitment", back_populates="commitment_period")
    device_commitments = relationship("DeviceCommitment", back_populates="commitment_period")
