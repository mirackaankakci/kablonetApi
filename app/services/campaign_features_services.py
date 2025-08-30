from app.crud.campaign_features_crud import get_campaign_features_by_id_from_db, create_campaign_features_from_db, update_campaign_features_in_db, list_all_campaign_features_from_db, deactivate_campaign_features_from_db
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from fastapi import APIRouter, Depends, HTTPException
from app.db.models.campaign_features import CampaignFeatures
from app.schemas.campaign_features_schemas import CampaignFeaturesSchema, CampaignFeaturesCreateSchema
from app.services.util import get_object_by_id, validate_required_field,validate_datetime_fields, validate_min_length, validate_list_not_empty ,ensure_dict, validate_non_negative_fields, validate_required_keys

string_columns = [
        col.name for col in CampaignFeatures.__table__.columns
        if isinstance(col.type, String)
    ]


def get_campaign_features_by_id(campaign_features_id: int, db: Session):
    get_object_by_id(CampaignFeatures, campaign_features_id, db)
    return get_campaign_features_by_id_from_db(campaign_features_id, db)



def create_campaign_features_service(campaign_features_data: CampaignFeaturesCreateSchema | dict, db: Session):
    campaign_features_data= ensure_dict(campaign_features_data)
    validate_list_not_empty(campaign_features_data)
    
    validate_non_negative_fields(CampaignFeatures, campaign_features_data)
    validate_required_keys(CampaignFeatures, campaign_features_data)
    # validate_datetime_fields(CampaignFeatures, campaign_features_data, allow_none=True)
    
    for col_name in string_columns:
        value = campaign_features_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)

    return create_campaign_features_from_db(campaign_features_data, db)

def update_campaign_features_service(campaign_features_data: dict, campaign_features_id: int, db: Session):
    campaign_features_data= ensure_dict(campaign_features_data)
    validate_list_not_empty(campaign_features_data)
    
    validate_non_negative_fields(CampaignFeatures, campaign_features_data)
    validate_required_keys(CampaignFeatures, campaign_features_data)
    # validate_datetime_fields(CampaignFeatures, campaign_features_data, allow_none=True)
    
    get_object_by_id(CampaignFeatures, campaign_features_id, db)
    
    for col_name in string_columns:
        value = campaign_features_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    
    return update_campaign_features_in_db(campaign_features_data, campaign_features_id, db)



def list_all_campaign_features_service(db: Session):
    
    campaign_features=list_all_campaign_features_from_db(db)
    
    validate_list_not_empty(campaign_features)
    
    return campaign_features

def deactivate_campaign_features_services(campaign_features_id: int, db: Session):
    get_object_by_id(CampaignFeatures, campaign_features_id, db)
    campaign_features = deactivate_campaign_features_from_db(campaign_features_id, db)
    return campaign_features