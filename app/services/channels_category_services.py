from sqlalchemy.orm import Session
from sqlalchemy import String
from app.db.models.channel_category import ChannelCategory
from app.schemas.channels_category_schemas import ChannelCategoryCreateSchemas
from app.crud.channels_category_crud import get_channel_category_by_id_from_db, create_channel_category_from_db, update_channel_category_in_db, list_all_channel_category_from_db, deactivate_channel_category_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict

string_columns = [
        col.name for col in ChannelCategory.__table__.columns
        if isinstance(col.type, String)
    ]

def get_channel_category_services(channel_category_id: int, db: Session):
    get_object_by_id(ChannelCategory, channel_category_id, db)
    return get_channel_category_by_id_from_db(channel_category_id, db)

def create_channel_category_services(channel_category_data: ChannelCategoryCreateSchemas | dict, db: Session):
    channel_category_data = ensure_dict(channel_category_data)
    validate_list_not_empty(channel_category_data)
    
    for col_name in string_columns:
        value = channel_category_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return create_channel_category_from_db(channel_category_data, db)

def update_channel_category_services(channel_category_data: dict, channel_category_id: int, db: Session):
    channel_category_data = ensure_dict(channel_category_data)
    validate_list_not_empty(channel_category_data)
    get_object_by_id(ChannelCategory, channel_category_id, db)
    
    for col_name in string_columns:
        value = channel_category_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    return update_channel_category_in_db(channel_category_data, channel_category_id, db)

def list_all_channel_category_services(db: Session):
    channel_category = list_all_channel_category_from_db(db)
    validate_list_not_empty(channel_category)
    return channel_category

def deactivate_channel_category_services(channel_category_id: int, db: Session):
    get_object_by_id(ChannelCategory, channel_category_id, db)
    about_content = deactivate_channel_category_from_db(channel_category_id, db)
    return about_content