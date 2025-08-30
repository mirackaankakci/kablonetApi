from app.crud.devices_crud import get_device_by_id_from_db, create_device_from_db, update_device_from_db, list_all_devices_from_db, deactivate_devices_from_db, get_device_by_category_from_db
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from app.schemas.devices_schemas import DeviceCreateSchema
from app.db.models.devices import Devices
from app.db.models.MainCategory import MainCategory
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict, validate_non_negative_fields, validate_required_keys

string_columns = [
        col.name for col in Devices.__table__.columns
        if isinstance(col.type, String)
    ]

def get_device_by_category_services(main_category_id: int, db: Session):
    get_object_by_id(MainCategory, main_category_id, db)
    device_category = get_device_by_category_from_db(main_category_id, db)
    validate_list_not_empty(device_category)
    return device_category

def get_device_by_id(device_id: int, db: Session):
    get_object_by_id(Devices, device_id, db)
    return get_device_by_id_from_db(device_id, db)

def create_device_service(device_data: DeviceCreateSchema | dict, db: Session):
    device_data = ensure_dict(device_data)
    validate_list_not_empty(device_data)
    
    validate_non_negative_fields(Devices, device_data)
    validate_required_keys(Devices, device_data)
    # validate_datetime_fields(Devices, device_data, allow_none=True)
    
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
    
    validate_non_negative_fields(Devices, device_data)
    validate_required_keys(Devices, device_data)
    # validate_datetime_fields(Devices, device_data, allow_none=True)
    
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
    

    
def deactivate_devices_services(device_id: int, db: Session):
    get_object_by_id(Devices, device_id, db)
    devices = deactivate_devices_from_db(device_id, db)
    return devices