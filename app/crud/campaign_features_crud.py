from app.db.database import get_db
from app.db.models.campaign_features import CampaignFeatures
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_campaign_features_by_id_from_db(campaign_features_id: int, db: Session):
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.id == campaign_features_id,
                                                        CampaignFeatures.is_active == True).first()
    #
    return campaign_features

def list_all_campaign_features_from_db(db: Session):
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.is_active == True).order_by(CampaignFeatures.id).all()
    #
    return campaign_features

def create_campaign_features_from_db(campaign_features_data, db: Session):
    new_campaign_features = CampaignFeatures(**campaign_features_data)
    db.add(new_campaign_features)
    db.commit()
    db.refresh(new_campaign_features)
    #
    return new_campaign_features

def update_campaign_features_in_db(campaign_features_data, campaign_features_id: int, db: Session):
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.id == campaign_features_id).first()
    if not campaign_features:
        #
        return None
    for key, value in campaign_features_data.items():
        setattr(campaign_features, key, value)
    db.commit()
    db.refresh(campaign_features)
    #
    return campaign_features

def deactivate_campaign_features_from_db(campaign_features_id: int, db: Session):
    campaign_features = db.query(CampaignFeatures).filter(CampaignFeatures.id == campaign_features_id,
                                                    CampaignFeatures.is_active == True).first()
    if not campaign_features:
        #
        return None
    
    if not campaign_features.is_active:
        return campaign_features 
    
    campaign_features.is_active = False
    
    db.commit()
    db.refresh(campaign_features)
    #
    return campaign_features