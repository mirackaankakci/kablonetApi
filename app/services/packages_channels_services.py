from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.packages_channels_schemas import PackagesChannelsCreateSchemas
from app.db.models.packages_channels import PackagesChannels
from app.db.models.channels import Channels
from app.db.models.packages import Packages
from app.crud.packages_channels_crud import get_packages_channels_by_id_from_db, create_packages_channels_from_db, update_packages_channels_from_db, list_all_packages_channels_from_db, get_packages_channels_by_packages_from_db, deactivate_packages_channels_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict, validate_non_negative_fields, validate_required_keys

string_columns = [
        col.name for col in PackagesChannels.__table__.columns
        if isinstance(col.type, String)
    ]

def get_packages_channels_services(packages_channels_id: int, db: Session):
    get_object_by_id(PackagesChannels, packages_channels_id, db)
    return get_packages_channels_by_id_from_db(packages_channels_id, db)

def create_packages_channels_services(packages_channels_data: PackagesChannelsCreateSchemas | dict, db: Session):
    packages_channels_data = ensure_dict(packages_channels_data)
    validate_list_not_empty(packages_channels_data)
    
    validate_non_negative_fields(PackagesChannels, packages_channels_data)
    validate_required_keys(PackagesChannels, packages_channels_data)
    # validate_datetime_fields(PackagesChannels, packages_channels_data, allow_none=True)
    
    channels_id = validate_required_field(
        packages_channels_data.get("channels_id")
    )
    get_object_by_id(Channels, channels_id, db)
    
    packages_id = validate_required_field(
        packages_channels_data.get("packages_id")
    )
    get_object_by_id(Packages, packages_id, db)
    
    for col_name in string_columns:
        value = packages_channels_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)    
    
    return create_packages_channels_from_db(packages_channels_data, db)

def update_packages_channels_services(packages_channels_id: int, packages_channels_data: dict, db: Session):
    packages_channels_data = ensure_dict(packages_channels_data)
    validate_list_not_empty(packages_channels_data)
    get_object_by_id(PackagesChannels, packages_channels_id, db)
    
    validate_non_negative_fields(PackagesChannels, packages_channels_data)
    validate_required_keys(PackagesChannels, packages_channels_data)
    # validate_datetime_fields(PackagesChannels, packages_channels_data, allow_none=True)
    
    channels_id = validate_required_field(
        packages_channels_data.get("channels_id")
    )
    get_object_by_id(Channels, channels_id, db)
    
    packages_id = validate_required_field(
        packages_channels_data.get("packages_id")
    )
    get_object_by_id(Packages, packages_id, db)
    
    for col_name in string_columns:
        value = packages_channels_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value) 
    
    return update_packages_channels_from_db(packages_channels_id, packages_channels_data, db)

def  list_all_packages_channels_services(db: Session):
    packages_channels = list_all_packages_channels_from_db(db)
    validate_list_not_empty(packages_channels)
    return packages_channels

def get_packages_channels_by_packages(packages_id: int, db: Session):
    get_object_by_id(Packages, packages_id, db)
    packages_channels = get_packages_channels_by_packages_from_db(packages_id, db)
    validate_list_not_empty(packages_channels)
    return packages_channels

def deactivate_packages_channels_services(packages_channels_id: int, db: Session):
    get_object_by_id(PackagesChannels, packages_channels_id, db)
    packages_channels = deactivate_packages_channels_from_db(packages_channels_id, db)
    return packages_channels