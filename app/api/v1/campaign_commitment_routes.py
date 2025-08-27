from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.campaign_commitment_schemas import CampaignCommitmentCreateSchema, CampaignCommitmentUpdateSchema, CampaignCommitmentSchema
from app.services.campaign_commitment_services import get_campaign_commitment_by_id, create_campaign_commitment_service, update_campaign_commitment_service, get_all_campaign_commitments_campaign_service, get_all_campaign_commitments_service

router = APIRouter(prefix="/campaign-commitments", tags=["Campaign Commitments"])

@router.get("/campaign-commitments-device", response_model=list[CampaignCommitmentSchema])
def list_all_campaign_commitments_campaign(campaign_id: int, db: Session = Depends(get_db)):
    commitments = get_all_campaign_commitments_campaign_service(campaign_id, db)
    return commitments

@router.get("/campaign-commitments", response_model=list[CampaignCommitmentSchema])
def list_all_campaign_commitments(db: Session= Depends(get_db)):
    commitments = get_all_campaign_commitments_service(db)
    return commitments

@router.get("/{commitment_id}", response_model=CampaignCommitmentSchema)
def get_campaign_commitment(commitment_id: int, db: Session = Depends(get_db)):
    commitment = get_campaign_commitment_by_id(commitment_id, db)
    return commitment

@router.post("/new-commitment", response_model=CampaignCommitmentCreateSchema)
def add_campaign_commitment(commitment_data: CampaignCommitmentCreateSchema, db: Session = Depends(get_db)):
    created_commitment = create_campaign_commitment_service(commitment_data, db)
    return created_commitment

@router.put("/{commitment_id}", response_model=CampaignCommitmentUpdateSchema)
def update_campaign_commitment(commitment_id: int, commitment_data: CampaignCommitmentUpdateSchema, db: Session = Depends(get_db)):
    updated_commitment = update_campaign_commitment_service(commitment_id, commitment_data, db)
    return updated_commitment