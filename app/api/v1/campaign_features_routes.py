from fastapi import APIRouter, Depends, HTTPException
from app.schemas.campaign_features_schemas import CampaignFeaturesSchema, CampaignFeaturesCreateSchema, CampaignFeaturesUpdateSchema, CampaignFeaturesResponse
from app.services.campaign_features_services import get_campaign_features_by_id, create_campaign_features_service, update_campaign_features_service

router = APIRouter(prefix="/campaigns-features", tags=["Campaign Features"])

@router.get("/{campaign_id}/features", response_model=CampaignFeaturesResponse)
def get_campaign_features(campaign_id: int):
    campaign_features = get_campaign_features_by_id(campaign_id)
    if not campaign_features:
        raise HTTPException(status_code=404, detail="Campaign features not found")
    return campaign_features

@router.post("/new-features", response_model=CampaignFeaturesCreateSchema)
def add_campaign_features(campaign_features_data: CampaignFeaturesCreateSchema):
    try:
        created_campaign_features = create_campaign_features_service(campaign_features_data)
        return created_campaign_features
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{campaign_id}", response_model=CampaignFeaturesUpdateSchema)
def update_campaign_features(campaign_id: int, features_data: CampaignFeaturesUpdateSchema):
    try:
        updated_campaign_features = update_campaign_features_service(features_data, campaign_id)
        if not updated_campaign_features:
            raise HTTPException(status_code=404, detail="Campaign features not found")
        return updated_campaign_features
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))