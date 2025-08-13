from sqlalchemy.orm import Session
from app.crud.channels_category_crud import get_channel_category_by_id_from_db, create_channel_category_from_db, update_channel_category_in_db, list_all_channel_category_from_db

def get_channel_category_services(channel_category_id: int):
    return get_channel_category_by_id_from_db(channel_category_id)

def create_channel_category_services(channel_category_data: dict):
    return create_channel_category_from_db(channel_category_data)

def update_channel_category_services(channel_category_data: dict, channel_category_id: int):
    return update_channel_category_in_db(channel_category_data, channel_category_id)

def list_all_channel_category_services(db: Session):
    return list_all_channel_category_from_db(db)