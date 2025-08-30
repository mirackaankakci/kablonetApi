from sqlalchemy import Column, Integer, String, Boolean, ForeignKey,DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.db.models.MainCategory import MainCategory
from app.db.models.campaign_features import CampaignFeatures


class Campaign(Base):
    __tablename__ = "campaign"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True)
    feature_table = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    subheading = Column(String, nullable=True)
    add_time = Column(DateTime, default=datetime.now, nullable=True)
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    campaign_notes = Column(String, nullable=True)
    
    main_category_id = Column(Integer, ForeignKey('main_category.id'), nullable=False)
    main_category = relationship("MainCategory", back_populates="campaigns")
    
    # özellik id gelmesi gerekiyor
    campaign_features_id = Column(Integer, ForeignKey('campaign_features.id'), nullable=True)
    campaign_features = relationship("CampaignFeatures", back_populates="campaign")
    
    campaign_commitments = relationship("CampaignCommitment", back_populates="campaign") #, cascade="all, delete-orphan"