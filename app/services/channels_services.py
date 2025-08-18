from sqlalchemy.orm import Session
from app.crud.channels_crud import get_channels_by_id_from_db, create_channels_from_db, update_channels_from_db, list_all_channels_from_db, get_channels_by_category_id_from_db


def get_channels_services(channels_id: int):
    return get_channels_by_id_from_db(channels_id)

def create_channels_services(channels_data: dict):
    return create_channels_from_db(channels_data)

def update_channels_services(channels_id: int, channels_data: dict):
    return update_channels_from_db(channels_id, channels_data)

def list_all_channels_services(db: Session):
    return list_all_channels_from_db(db)

def get_channels_by_category_services(channel_category_id: int):
    return get_channels_by_category_id_from_db(channel_category_id)