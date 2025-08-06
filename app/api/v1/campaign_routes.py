from fastapi import APIRouter, Depends, HTTPException
from app.services.campaign_service import get_campaign_by_id, create_campaign_service, update_campaign_service
from app.schemas.campaign_schema import CampaignSchema, CampaignCreateSchema, CampaignUpdateSchema, CampaignUpdateResponse

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])

@router.get("/{campaign_id}", response_model=CampaignSchema)
def get_campaign(campaign_id: int):
    campaign = get_campaign_by_id(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

@router.post("/new-campaign", response_model=CampaignCreateSchema)
def add_campaign(campaign_data: CampaignCreateSchema):
    try:
        created_campaign = create_campaign_service(campaign_data)
        return created_campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{campaign_id}", response_model=CampaignUpdateResponse)
def update_campaign(campaign_id: int, campaign_data: CampaignUpdateResponse):
    try:
        updated_campaign = update_campaign_service(campaign_data, campaign_id)
        if not updated_campaign:
            raise HTTPException(status_code=404, detail="Campaign not found")
        return updated_campaign
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))