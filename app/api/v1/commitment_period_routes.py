from fastapi import APIRouter, Depends, HTTPException
from app.schemas.commitment_period_schemas import CommitmentPeriodSchema, CommitmentPeriodCreateSchema, CommitmentPeriodUpdateSchema, CommitmentPeriodResponse
from app.services.commitment_period_service import get_commitment_period_by_id, create_commitment_period_service, update_commitment_period_service

router = APIRouter(prefix="/commitment-period", tags=["Commitment Periods"])

@router.get("/{commitment_period_id}", response_model=CommitmentPeriodResponse)
def get_commitment_period(commitment_period_id: int):
    commitment_period = get_commitment_period_by_id(commitment_period_id)
    if not commitment_period:
        raise HTTPException(status_code=404, detail="Commitment period not found")
    return commitment_period

@router.post("/new-period", response_model=CommitmentPeriodCreateSchema)
def add_commitment_period(commitment_period_data: CommitmentPeriodCreateSchema):
    try:
        created_commitment_period = create_commitment_period_service(commitment_period_data)
        return created_commitment_period
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{commitment_period_id}", response_model=CommitmentPeriodUpdateSchema)
def update_commitment_period(commitment_period_id: int, commitment_period_data: CommitmentPeriodUpdateSchema):
    try:
        updated_commitment_period = update_commitment_period_service(commitment_period_data, commitment_period_id)
        if not updated_commitment_period:
            raise HTTPException(status_code=404, detail="Commitment period not found")
        return updated_commitment_period
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
