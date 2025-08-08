from app.crud.channel_list import create_channel_list, get_channel_list_by_id, update_channel_list, get_all_channel_list                                                                                                        
from app.schemas.channel_list_schema import ChannelListCreate, ChannelListUpdate, ChannelListResponse, ChannelListAllResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_channel_list_by_id_from_db(channel_id: int):
    return get_channel_list_by_id(channel_id)

def create_channel_list_service(channel_data: ChannelListCreate):
    return create_channel_list(channel_data)

def update_channel_list_service(channel_id: int, channel_data: ChannelListUpdate):
    updated_channel = update_channel_list(channel_id, channel_data)
    if not updated_channel:
        raise HTTPException(status_code=404, detail="channel bulunamadı")
    return updated_channel

def get_all_channel_list_service(db: Session):
    channel_list = get_all_channel_list(db)
    if not channel_list:
        raise HTTPException(status_code=404, detail="channel listesi bulunamadı")
    return [ChannelListAllResponse.from_orm(channel) for channel in channel_list]
    