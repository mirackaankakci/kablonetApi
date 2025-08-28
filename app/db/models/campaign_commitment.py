from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

# taahütname tablosu
class CampaignCommitment(Base):
    __tablename__ = "campaign_commitment"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    price = Column(Integer, nullable=False)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=False)
    campaign = relationship("Campaign", back_populates="campaign_commitments")
    
    commitment_period_id = Column(Integer, ForeignKey('commitment_period.id'), nullable=False)
    commitment_period = relationship("CommitmentPeriod", back_populates="campaign_commitments")
    
    # kampanya ve taahütname süresi arasındaki ilişki