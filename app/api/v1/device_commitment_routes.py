from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.device_commitment_schemas import DeviceCommitmentSchema, DeviceCommitmentCreateSchema, DeviceCommitmentUpdateSchema,DeleteDeviceCommitmentSchema
from app.services.device_commitment_services import get_device_commitment_by_id, create_device_commitment_service, update_device_commitment_service, get_all_device_commitments_device_service, list_all_device_commitments_service, deactivate_device_commitments_services

router = APIRouter(prefix="/device-commitments", tags=["Device Commitments"])

@router.get("/", response_model=list[DeviceCommitmentSchema])
def list_all_device_commitments(db: Session = Depends(get_db)):
    device_commitments = list_all_device_commitments_service(db)
    return device_commitments

@router.get("/device", response_model=list[DeviceCommitmentSchema])
def list_all_device_commitments_device(device_id: int, db: Session = Depends(get_db)):
    device_commitments = get_all_device_commitments_device_service(device_id, db)
    return device_commitments

@router.get("/{device_commitment_id}", response_model=DeviceCommitmentSchema)
def get_device_commitment(device_commitment_id: int, db: Session = Depends(get_db)):
    device_commitment = get_device_commitment_by_id(device_commitment_id, db)
    return device_commitment

@router.post("/new-device-commitment", response_model=DeviceCommitmentCreateSchema)
def add_device_commitment(device_commitment_data: DeviceCommitmentCreateSchema, db: Session = Depends(get_db)):
    created_device_commitment = create_device_commitment_service(device_commitment_data, db)
    return created_device_commitment

@router.put("/{device_commitment_id}", response_model=DeviceCommitmentUpdateSchema)
def update_device_commitment(device_commitment_id: int, device_commitment_data: DeviceCommitmentUpdateSchema, db: Session = Depends(get_db)):
    updated_device_commitment = update_device_commitment_service(device_commitment_data, device_commitment_id, db)
    return updated_device_commitment
    
@router.delete("/{device_commitment_id}", response_model= DeleteDeviceCommitmentSchema)
def deactivate_device_commitments(device_commitment_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_device_commitments_services(device_commitment_id, db)
    return deactivate