from fastapi import APIRouter, Depends, HTTPException
from app.services.campaign_service import get_campaign_by_id, create_campaign_service, update_campaign_service, get_all_campaigns_service, get_all_campaigns_by_category_service
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.campaign_schema import CampaignSchema, CampaignCreateSchema, CampaignUpdateSchema, CampaignUpdateResponse

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])

@router.get("/", response_model=list[CampaignSchema])
def list_all_campaigns(db: Session = Depends(get_db)):
    return get_all_campaigns_service(db)

@router.get("/category", response_model=list[CampaignSchema])
def list_all_campaigns_by_category(main_category_id: int, db: Session = Depends(get_db)):
    campaigns = get_all_campaigns_by_category_service(main_category_id)
    if not campaigns:
        raise HTTPException(status_code=404, detail="No campaigns found for this category")
    return campaigns

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