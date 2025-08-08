from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.campaign_commitment_schemas import CampaignCommitmentCreateSchema, CampaignCommitmentUpdateSchema, CampaignCommitmentSchema
from app.services.campaign_commitment_services import get_campaign_commitment_by_id, create_campaign_commitment_service, update_campaign_commitment_service, get_all_campaign_commitments_service

router = APIRouter(prefix="/campaign-commitments", tags=["Campaign Commitments"])

@router.get("/campaign-commitments", response_model=list[CampaignCommitmentSchema])
def list_all_campaign_commitments(campaign_id: int, db: Session = Depends(get_db)):
    commitments = get_all_campaign_commitments_service(campaign_id)
    if not commitments:
        raise HTTPException(status_code=404, detail="No Campaign Commitments found for this campaign")
    return commitments

@router.get("/{commitment_id}", response_model=CampaignCommitmentSchema)
def get_campaign_commitment(commitment_id: int):
    commitment = get_campaign_commitment_by_id(commitment_id)
    if not commitment:
        raise HTTPException(status_code=404, detail="Campaign Commitment not found")
    return commitment

@router.post("/new-commitment", response_model=CampaignCommitmentCreateSchema)
def add_campaign_commitment(commitment_data: CampaignCommitmentCreateSchema):
    try:
        created_commitment = create_campaign_commitment_service(commitment_data)
        return created_commitment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{commitment_id}", response_model=CampaignCommitmentUpdateSchema)
def update_campaign_commitment(commitment_id: int, commitment_data: CampaignCommitmentUpdateSchema):
    try:
        updated_commitment = update_campaign_commitment_service(commitment_id, commitment_data)
        if not updated_commitment:
            raise HTTPException(status_code=404, detail="Campaign Commitment not found")
        return updated_commitment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))