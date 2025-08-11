from app.crud.campaign_features_crud import get_campaign_features_by_id_from_db, create_campaign_features_from_db, update_campaign_features_in_db, list_all_campaign_features_from_db
from sqlalchemy.orm import Session

def get_campaign_features_by_id(campaign_features_id: int):
    return get_campaign_features_by_id_from_db(campaign_features_id)

def create_campaign_features_service(campaign_features_data: dict):
    return create_campaign_features_from_db(campaign_features_data)

def update_campaign_features_service(campaign_features_data: dict, campaign_features_id: int):
    return update_campaign_features_in_db(campaign_features_data, campaign_features_id)

def list_all_campaign_features_service(db: Session):
    return list_all_campaign_features_from_db(db)