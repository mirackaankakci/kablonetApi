from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.channels_schemas import ChannelsCreateSchemas
from app.db.models.channels import Channels
from app.db.models.channel_category import ChannelCategory
from app.crud.channels_crud import get_channels_by_id_from_db, create_channels_from_db, update_channels_from_db, list_all_channels_from_db, get_channels_by_category_id_from_db, deactivate_channels_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict

string_columns = [
        col.name for col in Channels.__table__.columns
        if isinstance(col.type, String)
    ]

def get_channels_services(channels_id: int, db: Session):
    get_object_by_id(Channels, channels_id,db)
    return get_channels_by_id_from_db(channels_id, db)

def create_channels_services(channels_data: ChannelsCreateSchemas | dict, db: Session):
    channels_data = ensure_dict(channels_data)
    validate_list_not_empty(channels_data)
    
    channel_category_id = validate_required_field(
        channels_data.get("channel_category_id")
    )
    get_object_by_id(ChannelCategory, channel_category_id, db)
    
    for col_name in string_columns:
        value = channels_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)    
    
    return create_channels_from_db(channels_data, db)

def update_channels_services(channels_id: int, channels_data: dict, db: Session):
    channels_data = ensure_dict(channels_data)
    validate_list_not_empty(channels_data)
    get_object_by_id(Channels, channels_id,db)
    
    channel_category_id = validate_required_field(
        channels_data.get("channel_category_id"))
    get_object_by_id(ChannelCategory, channel_category_id, db)
    
    for col_name in string_columns:
        value = channels_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return update_channels_from_db(channels_id, channels_data, db)

def list_all_channels_services(db: Session):
    all_channels = list_all_channels_from_db(db)
    validate_list_not_empty(all_channels)
    return all_channels

def get_channels_by_category_services(channel_category_id: int, db: Session):
    get_object_by_id(ChannelCategory, channel_category_id, db)
    channels = get_channels_by_category_id_from_db(channel_category_id, db)
    validate_list_not_empty(channels)
    return channels

def deactivate_channels_services(channels_id: int, db: Session):
    get_object_by_id(Channels, channels_id, db)
    channels = deactivate_channels_from_db(channels_id, db)
    return channels