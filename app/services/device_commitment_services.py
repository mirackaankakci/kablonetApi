from app.crud.device_commitment_crud import get_device_commitment_by_id_from_db, create_device_commitment_from_db, update_device_commitment_from_db, get_all_device_commitments_device_from_db, list_all_device_commitments_from_db
from sqlalchemy.orm import Session

def get_all_device_commitments_device_service(device_id: int):
    return get_all_device_commitments_device_from_db(device_id)

def get_device_commitment_by_id(device_commitment_id: int):
    return get_device_commitment_by_id_from_db(device_commitment_id)

def create_device_commitment_service(device_commitment_data: dict):
    return create_device_commitment_from_db(device_commitment_data)

def update_device_commitment_service(device_commitment_data: dict, device_commitment_id: int):
    return update_device_commitment_from_db(device_commitment_id, device_commitment_data)

def list_all_device_commitments_service(db: Session):
    return list_all_device_commitments_from_db(db)

