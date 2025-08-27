from app.crud.device_commitment_crud import get_device_commitment_by_id_from_db, create_device_commitment_from_db, update_device_commitment_from_db, get_all_device_commitments_device_from_db, list_all_device_commitments_from_db
from sqlalchemy.orm import Session
from sqlalchemy import String
from app.db.models.device_commitment import DeviceCommitment
from app.db.models.devices import Devices
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty, get_all_ready_have_id,ensure_dict


string_columns = [
        col.name for col in DeviceCommitment.__table__.columns
        if isinstance(col.type, String)
    ]

def get_all_device_commitments_device_service(device_id: int, db: Session):
    return get_all_device_commitments_device_from_db(device_id, db)

def get_device_commitment_by_id(device_commitment_id: int, db: Session):
    get_object_by_id(DeviceCommitment, device_commitment_id, db)
    return get_device_commitment_by_id_from_db(device_commitment_id, db)

def create_device_commitment_service(device_commitment_data: dict, db: Session):
    return create_device_commitment_from_db(device_commitment_data, db)

def update_device_commitment_service(device_commitment_data: dict, device_commitment_id: int, db: Session):
    return update_device_commitment_from_db(device_commitment_id, device_commitment_data, db)

def list_all_device_commitments_service(db: Session):
    device_commitments = list_all_device_commitments_from_db(db)
    
    return device_commitments

