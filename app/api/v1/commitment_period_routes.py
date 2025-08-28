from fastapi import APIRouter, Depends, HTTPException
from app.schemas.commitment_period_schemas import CommitmentPeriodSchema, CommitmentPeriodCreateSchema, CommitmentPeriodUpdateSchema, CommitmentPeriodResponse,DeleteCommitmentPeriodSchema
from app.services.commitment_period_service import get_commitment_period_by_id, create_commitment_period_service, update_commitment_period_service,list_all_commitment_period_service,deactivate_commitment_period_services
from sqlalchemy.orm import Session
from app.db.database import get_db


router = APIRouter(prefix="/commitment-period", tags=["Commitment Periods"])

@router.get("/periods", response_model=list[CommitmentPeriodSchema])
def list_all_commitment_periods(db: Session = Depends(get_db)):
    list_commitment_period = list_all_commitment_period_service(db)
    return list_commitment_period

@router.get("/{commitment_period_id}", response_model=CommitmentPeriodResponse)
def get_commitment_period(commitment_period_id: int, db: Session = Depends(get_db)):
    commitment_period = get_commitment_period_by_id(commitment_period_id,db)
    return commitment_period

@router.post("/new-period", response_model=CommitmentPeriodCreateSchema)
def add_commitment_period(commitment_period_data: CommitmentPeriodCreateSchema, db: Session = Depends(get_db)):
    created_commitment_period = create_commitment_period_service(commitment_period_data,db)
    return created_commitment_period

@router.put("/{commitment_period_id}", response_model=CommitmentPeriodUpdateSchema)
def update_commitment_period(commitment_period_id: int, commitment_period_data: CommitmentPeriodUpdateSchema, db: Session = Depends(get_db)):
    updated_commitment_period = update_commitment_period_service(commitment_period_data, commitment_period_id,db)
    return updated_commitment_period

@router.delete("/{commitment_period_id}", response_model= DeleteCommitmentPeriodSchema)
def deactivate_commitment_period(commitment_period_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_commitment_period_services(commitment_period_id, db)
    return deactivate
