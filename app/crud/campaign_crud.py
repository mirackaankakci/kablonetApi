from app.db.database import get_db
from app.db.models.Campaign import Campaign
from app.db.models.MainCategory import MainCategory
from app.db.models.campaign_features import CampaignFeatures
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal


db:Session = SessionLocal()

def get_campaign_by_id_from_db(campaign_id: int ,db: Session):
    campaign = db.query(Campaign).options(
        joinedload(Campaign.main_category),
        joinedload(Campaign.campaign_features)
        ).filter(Campaign.id == campaign_id,
                Campaign.is_active == True).first()
    #
    return campaign

#kategoriye gore kampanya getir
def get_all_campaigns_by_category_from_db(main_category_id: int, db: Session):
    campaigns = db.query(Campaign).options(
        joinedload(Campaign.main_category),
        joinedload(Campaign.campaign_features)
    ).filter(Campaign.main_category_id == main_category_id,
            Campaign.is_active == True).order_by(Campaign.id).all()
    #
    return campaigns


# bütün kampanyaları getir
def get_all_campaigns_from_db(db: Session):
    campaigns = db.query(Campaign).options(
        joinedload(Campaign.main_category),
        joinedload(Campaign.campaign_features)
    ).filter(Campaign.is_active == True).order_by(Campaign.id).all()
    #
    return campaigns


def create_campaign_from_db(campaign_data, db: Session):
    new_campaign = Campaign(**campaign_data)
    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)
    #
    return new_campaign


def update_campaign_from_db(campaign_id: int, campaign_data, db: Session):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id).first()
    if not campaign:
        #
        return None
    for key, value in campaign_data.items():
        setattr(campaign, key, value)
    db.commit()
    db.refresh(campaign)
    #
    return campaign

def deactivate_campaign_from_db(campaign_id: int, db: Session):
    campaign = db.query(Campaign).filter(Campaign.id == campaign_id,
                                                    Campaign.is_active == True).first()
    if not campaign:
        #
        return None
    
    if not campaign.is_active:
        return campaign 
    
    campaign.is_active = False
    
    db.commit()
    db.refresh(campaign)
    #
    return campaign