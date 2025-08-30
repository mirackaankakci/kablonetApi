from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

# kampanya özellikleri tablosu
class CampaignFeatures(Base):
    __tablename__ = "campaign_features"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    pricing_HTML = Column(String, index=True, nullable=False)
    detail_HTML = Column(String, nullable=True)
    devices= Column(String, nullable=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    
    campaign = relationship("Campaign", back_populates="campaign_features")
    