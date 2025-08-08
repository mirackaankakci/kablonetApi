from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.channel_list_service import get_channel_list_by_id_from_db, create_channel_list_service, update_channel_list_service, get_all_channel_list_service
from app.schemas.channel_list_schema import ChannelListAllResponse, ChannelListCreate, ChannelListUpdate, ChannelListResponse

router = APIRouter(prefix="/channel-list", tags=["channel List"])

@router.get("/channels", response_model=list[ChannelListAllResponse])
def list_all_channels(db: Session = Depends(get_db)):
    return get_all_channel_list_service(db)

@router.get("/{channel_id}", response_model=ChannelListResponse)
def get_channel(channel_id: int):
    channel = get_channel_list_by_id_from_db(channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="channel bulunamadı")
    return channel

@router.post("/new-channel", response_model=ChannelListCreate)
def add_channel(channel_data: ChannelListCreate):
    created_channel = create_channel_list_service(channel_data.dict())
    if not created_channel:
        raise HTTPException(status_code=400, detail="channel oluşturulamadı")
    return created_channel

@router.put("/{channel_id}", response_model=ChannelListUpdate)
def update_channel(channel_id: int, channel_data: ChannelListUpdate):
    updated_channel = update_channel_list_service(channel_id, channel_data.dict())
    if not updated_channel:
        raise HTTPException(status_code=404, detail="channel bulunamadı")
    return updated_channel

