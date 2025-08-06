from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Campaign(Base):
    __tablename__ = "campaign"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    feature_table = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    subheading = Column(String, nullable=True)
    start_date = Column(String)
    campaign_notes = Column(String, nullable=True)

    main_category_id = Column(Integer, ForeignKey('main_category.id'), nullable=False)
    main_category = relationship("MainCategory", back_populates="campaigns")