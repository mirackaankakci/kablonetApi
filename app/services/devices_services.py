from app.crud.devices_crud import get_device_by_id_from_db, create_device_from_db, update_device_from_db, list_all_devices_from_db
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from app.db.models.devices import Devices
from app.db.models.MainCategory import MainCategory
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty, get_all_ready_have_id,ensure_dict

string_columns = [
        col.name for col in Devices.__table__.columns
        if isinstance(col.type, String)
    ]

def get_device_by_id(device_id: int, db: Session):
    get_object_by_id(Devices, device_id, db)
    return get_device_by_id_from_db(device_id, db)

def create_device_service(device_data: dict, db: Session):
    device_data = ensure_dict(device_data)
    validate_list_not_empty(device_data)
    
    main_category_id = validate_required_field(device_data.get("main_category_id"))
    get_object_by_id(MainCategory, main_category_id, db)
    
    for col_name in string_columns:
        value = device_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return create_device_from_db(device_data, db)

def update_device_service(device_data: dict, device_id: int, db: Session):
    device_data = ensure_dict(device_data)
    validate_list_not_empty(device_data)
    get_object_by_id(Devices, device_id, db)
    
    main_category_id = validate_required_field(device_data.get("main_category_id"))
    get_object_by_id(MainCategory, main_category_id, db)    
    
    for col_name in string_columns:
        value = device_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return update_device_from_db(device_id, device_data, db)

def list_all_devices_service(db: Session):
    devices = list_all_devices_from_db(db)
    validate_list_not_empty(devices)
    return devices
    