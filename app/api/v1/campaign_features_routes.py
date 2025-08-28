from fastapi import APIRouter, Depends, HTTPException
from app.schemas.campaign_features_schemas import CampaignFeaturesSchema, CampaignFeaturesCreateSchema, CampaignFeaturesUpdateSchema, CampaignFeaturesResponse, CampaignFeaturesAllResponse, DeleteCampaignFeaturesSchema
from app.services.campaign_features_services import get_campaign_features_by_id, create_campaign_features_service, update_campaign_features_service, list_all_campaign_features_service, deactivate_campaign_features_services
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(prefix="/campaigns-features", tags=["Campaign Features"])

@router.get("/features", response_model=list[CampaignFeaturesAllResponse])
def list_all_campaign_features(db: Session = Depends(get_db)):
    return list_all_campaign_features_service(db)

@router.get("/{campaign_id}/features", response_model=CampaignFeaturesResponse)
def get_campaign_features(campaign_id: int, db: Session = Depends(get_db)):
    campaign_features = get_campaign_features_by_id(campaign_id,db)
    return campaign_features

@router.post("/new-features", response_model=CampaignFeaturesCreateSchema)
def add_campaign_features(campaign_features_data: CampaignFeaturesCreateSchema, db: Session = Depends(get_db)):
    created_campaign_features = create_campaign_features_service(campaign_features_data,db)
    return created_campaign_features

@router.put("/{campaign_id}", response_model=CampaignFeaturesUpdateSchema)
def update_campaign_features(campaign_id: int, features_data: CampaignFeaturesUpdateSchema, db: Session = Depends(get_db)):
    updated_campaign_features = update_campaign_features_service(features_data, campaign_id,db)
    return updated_campaign_features

@router.delete("/{campaign_features_id}", response_model= DeleteCampaignFeaturesSchema)
def deactivate_campaign_features(campaign_features_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_campaign_features_services(campaign_features_id, db)
    return deactivate