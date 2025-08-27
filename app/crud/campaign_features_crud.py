from app.db.database import get_db
from app.db.models.campaign_features import CampaignFeatures
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_campaign_features_by_id_from_db(campaign_features_id: int, db: Session):
    db: Session = SessionLocal()
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.id == campaign_features_id).first()
    db.close()
    return campaign_features

def list_all_campaign_features_from_db(db: Session):
    campaign_features = db.query(CampaignFeatures).order_by(CampaignFeatures.id).all()
    db.close()
    return campaign_features

def create_campaign_features_from_db(campaign_features_data, db: Session):
    db: Session = SessionLocal()
    new_campaign_features = CampaignFeatures(**campaign_features_data)
    db.add(new_campaign_features)
    db.commit()
    db.refresh(new_campaign_features)
    db.close()
    return new_campaign_features

def update_campaign_features_in_db(campaign_features_data, campaign_features_id: int, db: Session):
    db: Session = SessionLocal()
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.id == campaign_features_id).first()
    if not campaign_features:
        db.close()
        return None
    for key, value in campaign_features_data.items():
        setattr(campaign_features, key, value)
    db.commit()
    db.refresh(campaign_features)
    db.close()
    return campaign_features