from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.channel_list_service import get_channel_list_by_id_from_db, create_channel_list_service, update_channel_list_service, get_all_channel_list_service
from app.schemas.channel_list_schema import ChannelListAllResponse, ChannelListCreate, ChannelListUpdate, ChannelListResponse

router = APIRouter(prefix="/channel-list", tags=["Channel-List"])

@router.get("/channels", response_model=list[ChannelListAllResponse])
def list_all_channels(db: Session = Depends(get_db)):
    return get_all_channel_list_service(db)

@router.get("/{channel_id}", response_model=ChannelListResponse)
def get_channel(channel_id: int, db: Session = Depends(get_db)):
    channel = get_channel_list_by_id_from_db(channel_id, db)
    return channel

@router.post("/new-channel", response_model=ChannelListCreate)
def add_channel(channel_data: ChannelListCreate, db: Session = Depends(get_db)):
    created_channel = create_channel_list_service(channel_data, db)
    return created_channel

@router.put("/{channel_id}", response_model=ChannelListUpdate)
def update_channel(channel_id: int, channel_data: ChannelListUpdate, db: Session = Depends(get_db)):
    updated_channel = update_channel_list_service(channel_data, channel_id, db)
    return updated_channel