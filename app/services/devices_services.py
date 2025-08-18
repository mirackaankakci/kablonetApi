from app.crud.devices_crud import get_device_by_id_from_db, create_device_from_db, update_device_from_db, list_all_devices_from_db
from sqlalchemy.orm import Session

def get_device_by_id(device_id: int):
    return get_device_by_id_from_db(device_id)

def create_device_service(device_data: dict):
    return create_device_from_db(device_data)

def update_device_service(device_data: dict, device_id: int):
    return update_device_from_db(device_id, device_data)

def list_all_devices_service(db: Session):
    return list_all_devices_from_db(db)
    