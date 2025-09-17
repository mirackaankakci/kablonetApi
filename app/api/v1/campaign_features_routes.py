from fastapi import APIRouter, Depends, HTTPException
from app.schemas.campaign_features_schemas import CampaignFeaturesSchema, CampaignFeaturesCreateSchema, CampaignFeaturesUpdateSchema, CampaignFeaturesResponse, CampaignFeaturesAllResponse, DeleteCampaignFeaturesSchema
from app.services.campaign_features_services import get_campaign_features_by_id, create_campaign_features_service, update_campaign_features_service, list_all_campaign_features_service, deactivate_campaign_features_services
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator

router = APIRouter(prefix="/campaigns-features", tags=["Campaign Features"])

@router.get("/features", response_model=list[CampaignFeaturesAllResponse])
def list_all_campaign_features(db: Session = Depends(get_db)):
    return list_all_campaign_features_service(db)

@router.get("/{campaign_id}/features", response_model=CampaignFeaturesResponse)
def get_campaign_features(campaign_id: int, db: Session = Depends(get_db)):
    campaign_features = get_campaign_features_by_id(campaign_id,db)
    return campaign_features

@router.post("/new-features", response_model=CampaignFeaturesCreateSchema, summary="Create New Campaign Features (Admin Only)")
def add_campaign_features(
    campaign_features_data: CampaignFeaturesCreateSchema, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    created_campaign_features = create_campaign_features_service(campaign_features_data,db)
    return created_campaign_features

@router.put("/{campaign_id}", response_model=CampaignFeaturesUpdateSchema, summary="Update Campaign Features (Admin Only)")
def update_campaign_features(
    campaign_id: int, 
    features_data: CampaignFeaturesUpdateSchema, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_campaign_features = update_campaign_features_service(features_data, campaign_id,db)
    return updated_campaign_features

@router.delete("/{campaign_features_id}", response_model= DeleteCampaignFeaturesSchema, summary="Delete Campaign Features (Admin Only)")
def deactivate_campaign_features(
    campaign_features_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_campaign_features_services(campaign_features_id, db)
    return deactivate