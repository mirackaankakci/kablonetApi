from app.db.database import get_db
from app.db.models.Campaign import Campaign
from app.db.models.MainCategory import MainCategory
from app.db.models.campaign_features import CampaignFeatures
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal


db:Session = SessionLocal()

def get_campaign_by_id_from_db(campaign_id: int):
    campaign = db.query(Campaign).options(
        joinedload(Campaign.main_category),
        joinedload(Campaign.campaign_features)
        ).filter(Campaign.id == campaign_id).first()
    db.close()
    return campaign


def create_campaign_from_db(campaign_data):
    new_campaign = Campaign(**campaign_data.dict())
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    db.close()
    return new_campaign


def update_campaign_from_db(campaign_id: int, campaign_data):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        db.close()
        return None
    for key, value in campaign_data.dict().items():
        setattr(campaign, key, value)
    db.commit()
    db.refresh(campaign)
    db.close()
    return campaign