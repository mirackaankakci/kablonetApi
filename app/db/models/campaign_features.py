from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class CampaignFeatures(Base):
    __tablename__ = "campaign_features"

    id = Column(Integer, primary_key=True, index=True)
    pricing_HTML = Column(String, index=True)
    detail_HTML = Column(String, nullable=True)
    devices= Column(String, nullable=True)
    
    campaign_id = Column(Integer, ForeignKey('campaign.id'), nullable=False)
    campaign = relationship("Campaign", back_populates="features")