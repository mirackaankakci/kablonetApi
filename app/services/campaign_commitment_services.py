from  app.crud.campaign_commitment_crud import get_campaign_commitment_by_id_from_db, create_campaign_commitment_from_db, update_campaign_commitment_from_db, get_all_campaign_commitments_campaign_from_db, get_all_campaign_commitments_from_db
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from app.db.models.campaign_commitment import CampaignCommitment
from app.db.models.Campaign import Campaign
from app.db.models.commitment_period import CommitmentPeriod
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty, get_all_ready_have_id,ensure_dict


string_columns = [
        col.name for col in CampaignCommitment.__table__.columns
        if isinstance(col.type, String)
    ]

def get_all_campaign_commitments_campaign_service(campaign_id: int, db: Session):
    get_object_by_id(Campaign, campaign_id, db)
    commitments_campaign=get_all_campaign_commitments_campaign_from_db(campaign_id, db)
    validate_list_not_empty(commitments_campaign)
    return commitments_campaign

def get_campaign_commitment_by_id(commitment_id: int, db: Session):
    get_object_by_id(CampaignCommitment, commitment_id, db)
    return get_campaign_commitment_by_id_from_db(commitment_id, db)

def create_campaign_commitment_service(commitment_data: dict, db: Session):
    commitment_data= ensure_dict(commitment_data)
    validate_list_not_empty(commitment_data)
    
    commitment_period_id=validate_required_field(commitment_data.get("commitment_period_id"))
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    
    campaign_id=validate_required_field(commitment_data.get("campaign_id"))
    get_object_by_id(Campaign, campaign_id, db)
    
    for col_name in string_columns:
        value = commitment_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return create_campaign_commitment_from_db(commitment_data, db)

def update_campaign_commitment_service(commitment_data: dict, commitment_id: int, db: Session):
    commitment_data= ensure_dict(commitment_data)
    validate_list_not_empty(commitment_data)
    
    commitment_period_id=validate_required_field(commitment_data.get("commitment_period_id"))
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    
    campaign_id=validate_required_field(commitment_data.get("campaign_id"))
    get_object_by_id(Campaign, campaign_id, db)
    
    get_object_by_id(CampaignCommitment,commitment_id,db)
    
    for col_name in string_columns:
        if col_name in commitment_data and commitment_data.get(col_name) is not None:
            validate_min_length(commitment_data.get(col_name))
    
    return update_campaign_commitment_from_db(commitment_data, commitment_id, db)

def get_all_campaign_commitments_service(db: Session):
    campaign_commitments=get_all_campaign_commitments_from_db(db)
    validate_list_not_empty(campaign_commitments)
    return campaign_commitments