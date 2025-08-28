from app.crud.device_commitment_crud import get_device_commitment_by_id_from_db, create_device_commitment_from_db, update_device_commitment_from_db, get_all_device_commitments_device_from_db, list_all_device_commitments_from_db, deactivate_device_commitments_from_db
from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.device_commitment_schemas import DeviceCommitmentCreateSchema
from app.db.models.device_commitment import DeviceCommitment
from app.db.models.devices import Devices
from app.db.models.commitment_period import CommitmentPeriod
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict


string_columns = [
        col.name for col in DeviceCommitment.__table__.columns
        if isinstance(col.type, String)
    ]

def get_all_device_commitments_device_service(device_id: int, db: Session):
    get_object_by_id(Devices, device_id, db)
    commitments_device = get_all_device_commitments_device_from_db(device_id, db)
    validate_list_not_empty(commitments_device)
    return commitments_device

def get_device_commitment_by_id(device_commitment_id: int, db: Session):
    get_object_by_id(DeviceCommitment, device_commitment_id, db)
    return get_device_commitment_by_id_from_db(device_commitment_id, db)

def create_device_commitment_service(device_commitment_data: DeviceCommitmentCreateSchema | dict, db: Session):
    device_commitment_data = ensure_dict(device_commitment_data)
    validate_list_not_empty(device_commitment_data)
    
    commitment_period_id = validate_required_field(
        device_commitment_data.get("commitment_period_id"))
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    
    devices_id = validate_required_field(
        device_commitment_data.get("devices_id"))
    get_object_by_id(Devices, devices_id, db)
    
    for col_name in string_columns:
        value = device_commitment_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)

    return create_device_commitment_from_db(device_commitment_data, db)

def update_device_commitment_service(device_commitment_data: dict, device_commitment_id: int, db: Session):
    device_commitment_data = ensure_dict(device_commitment_data)
    get_object_by_id(DeviceCommitment, device_commitment_id, db)
    validate_list_not_empty(device_commitment_data)
    
    commitment_period_id = validate_required_field(
        device_commitment_data.get("commitment_period_id"))
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    
    devices_id = validate_required_field(
        device_commitment_data.get("devices_id"))
    get_object_by_id(Devices, devices_id, db)
    
    for col_name in string_columns:
        value = device_commitment_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return update_device_commitment_from_db(device_commitment_id, device_commitment_data, db)

def list_all_device_commitments_service(db: Session):
    device_commitments = list_all_device_commitments_from_db(db)
    validate_list_not_empty(device_commitments)
    return device_commitments

def deactivate_device_commitments_services(device_commitment_id: int, db: Session):
    get_object_by_id(DeviceCommitment, device_commitment_id, db)
    device_commitments = deactivate_device_commitments_from_db(device_commitment_id, db)
    return device_commitments