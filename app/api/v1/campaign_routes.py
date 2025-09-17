from fastapi import APIRouter, Depends, HTTPException
from app.services.campaign_service import get_campaign_by_id_service, create_campaign_service, update_campaign_service, get_all_campaigns_service, get_all_campaigns_by_category_service, deactivate_campaign_services
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.campaign_schema import CampaignSchema, CampaignCreateSchema, CampaignUpdateSchema, CampaignUpdateResponse,DeleteCampaignSchema
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])



@router.get("/", response_model=list[CampaignSchema])
def list_all_campaigns(db: Session = Depends(get_db)):
    return get_all_campaigns_service(db)

@router.get("/category", response_model=list[CampaignSchema])
def list_all_campaigns_by_category(main_category_id: int, db: Session = Depends(get_db)):
    campaigns = get_all_campaigns_by_category_service(main_category_id, db)
    return campaigns

@router.get("/{campaign_id}", response_model=CampaignSchema)
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):
    campaign = get_campaign_by_id_service(campaign_id, db)
    return campaign

@router.post("/new-campaign", response_model=CampaignCreateSchema, summary="Create New Campaign (Admin Only)")
def add_campaign(
    campaign_data: CampaignCreateSchema, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    created_campaign = create_campaign_service(campaign_data, db)
    return created_campaign
    
@router.put("/{campaign_id}", response_model=CampaignUpdateResponse, summary="Update Campaign (Admin Only)")
def update_campaign(
    campaign_id: int, 
    campaign_data: CampaignUpdateResponse, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_campaign = update_campaign_service(campaign_data, campaign_id, db)
    return updated_campaign

@router.delete("/{campaign_id}", response_model= DeleteCampaignSchema, summary="Delete Campaign (Admin Only)")
def deactivate_campaign(
    campaign_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_campaign_services(campaign_id, db)
    return deactivate