from app.db.database import get_db
from app.db.models.campaign_commitment import CampaignCommitment
from app.db.models.Campaign import Campaign
from app.db.models.campaign_commitment import CampaignCommitment
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_campaign_commitment_by_id_from_db(commitment_id: int, db: Session):
    commitment = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).filter(CampaignCommitment.id == commitment_id,
            CampaignCommitment.is_active == True).first()
    #
    return commitment

def get_all_campaign_commitments_from_db(db: Session):
    commitment = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).filter(CampaignCommitment.is_active == True).order_by(CampaignCommitment.id).all()
    #
    return commitment

def create_campaign_commitment_from_db(commitment_data, db: Session):
    new_commitment = CampaignCommitment(**commitment_data)
    db.add(new_commitment)
    db.commit()
    db.refresh(new_commitment)
    #
    return new_commitment

def update_campaign_commitment_from_db(commitment_id: int, commitment_data, db: Session):
    commitment = db.query(CampaignCommitment).filter(CampaignCommitment.id == commitment_id).first()
    if not commitment:
        #
        return None
    for key, value in commitment_data.items():
        setattr(commitment, key, value)
    db.commit()
    db.refresh(commitment)
    #
    return commitment

def get_all_campaign_commitments_campaign_from_db(campaign_id: int, db: Session):
    commitments = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).filter(CampaignCommitment.campaign_id == campaign_id,
            CampaignCommitment.is_active == True).order_by(CampaignCommitment.id).all()
    #
    return commitments

def deactivate_campaign_commitments_from_db(commitment_id: int, db: Session):
    commitment = db.query(CampaignCommitment).filter(CampaignCommitment.id == commitment_id,
                                                    CampaignCommitment.is_active == True).first()
    if not commitment:
        #
        return None
    
    if not commitment.is_active:
        return commitment 
    
    commitment.is_active = False
    
    db.commit()
    db.refresh(commitment)
    #
    return commitment