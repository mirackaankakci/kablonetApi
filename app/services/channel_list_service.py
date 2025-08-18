from app.crud.channel_list import create_channel_list, get_channel_list_by_id, update_channel_list, get_all_channel_list
from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_channel_list_by_id_from_db(channel_id: int):
    return get_channel_list_by_id(channel_id)

def create_channel_list_service(channel_data: dict):
    return create_channel_list(channel_data)

def update_channel_list_service(channel_data: dict ,channel_id: int):
    updated_channel = update_channel_list(channel_data, channel_id)
    if not updated_channel:
        raise HTTPException(status_code=404, detail="channel bulunamadı")
    return updated_channel

def get_all_channel_list_service(db: Session):
    channel = get_all_channel_list(db)
    if not channel:
        raise HTTPException(status_code=404, detail="channel listesi bulunamadı")
    return channel
    