from app.crud.channel_list import create_channel_list, get_channel_list_by_id, update_channel_list, get_all_channel_list, deactivate_channel_list_from_db
from fastapi import HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy import Integer, String
from app.db.models import channel_list
from app.schemas.channel_list_schema import ChannelListCreate
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict,validate_non_negative_fields, validate_required_keys

string_columns = [
    col.name for col in channel_list.__table__.columns
    if isinstance(col.type, String)
]


def get_channel_list_by_id_from_db(channel_id: int, db: Session):
    get_object_by_id(channel_list, channel_id, db)
    return get_channel_list_by_id(channel_id, db)

def get_all_channel_list_service(db: Session):
    channel = get_all_channel_list(db)

    validate_list_not_empty(channel)

    return channel

def create_channel_list_service(channel_data: ChannelListCreate | dict, db: Session):
    # BaseModel ise dict'e çevir
    channel_data = ensure_dict(channel_data)
    validate_list_not_empty(channel_data)
    
    validate_non_negative_fields(channel_list, channel_data)
    validate_required_keys(channel_list, channel_data)
    # validate_datetime_fields(channel_list, channel_data, allow_none=True)
    # validate_unique_field(model=channel_list, data=channel_data ,db=db)

    for col_name in string_columns:
        value = channel_data.get(col_name)
        if isinstance(value, str):
            validate_min_length(value)

    return create_channel_list(channel_data, db)  # CRUD fonksiyonuna data (dict) gönder

def update_channel_list_service(channel_data: dict ,channel_id: int, db: Session):
        # dict'e çevir
    channel_data = ensure_dict(channel_data)  # Pydantic objesini dict’e çevir
    validate_list_not_empty(channel_data)
    
    validate_non_negative_fields(channel_list, channel_data)
    validate_required_keys(channel_list, channel_data)
    # validate_datetime_fields(channel_list, channel_data, allow_none=True)
    
    get_object_by_id(channel_list, channel_id, db)
    
    for col_name in string_columns:
        if col_name in channel_data and channel_data.get(col_name) is not None:
            validate_min_length(channel_data.get(col_name))
    
    updated_channel = update_channel_list(channel_data, channel_id,db)
    return updated_channel

def deactivate_channel_list_services(channel_id: int, db: Session):
    get_object_by_id(channel_list, channel_id, db)
    channel = deactivate_channel_list_from_db(channel_id, db)
    return channel