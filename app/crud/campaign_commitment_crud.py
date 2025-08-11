from app.db.database import get_db
from app.db.models.campaign_commitment import CampaignCommitment
from app.db.models.Campaign import Campaign
from app.db.models.campaign_commitment import CampaignCommitment
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_campaign_commitment_by_id_from_db(commitment_id: int):
    commitment = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).filter(CampaignCommitment.id == commitment_id).first()
    db.close()
    return commitment

def get_all_campaign_commitments_from_db(db: Session):
    commitment = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).order_by(CampaignCommitment.id).all()
    db.close()
    return commitment

def create_campaign_commitment_from_db(commitment_data):
    new_commitment = CampaignCommitment(**commitment_data.dict())
    db.add(new_commitment)
    db.commit()
    db.refresh(new_commitment)
    db.close()
    return new_commitment

def update_campaign_commitment_from_db(commitment_id: int, commitment_data):
    commitment = db.query(CampaignCommitment).filter(CampaignCommitment.id == commitment_id).first()
    if not commitment:
        db.close()
        return None
    for key, value in commitment_data.dict().items():
        setattr(commitment, key, value)
    db.commit()
    db.refresh(commitment)
    db.close()
    return commitment

def get_all_campaign_commitments_campaign_from_db(campaign_id: int):
    commitments = db.query(CampaignCommitment).options(
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.main_category),
        joinedload(CampaignCommitment.campaign)
            .joinedload(Campaign.campaign_features),
        joinedload(CampaignCommitment.commitment_period)
    ).filter(CampaignCommitment.campaign_id == campaign_id).order_by(CampaignCommitment.id).all()
    db.close()
    return commitments