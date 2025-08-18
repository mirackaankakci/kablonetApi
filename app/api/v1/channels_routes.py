from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.channels_services import get_channels_services, create_channels_services, update_channels_services, list_all_channels_services, get_channels_by_category_services
from app.schemas.channels_schemas import ChannelsSchemas, ChannelsResponse, ChannelsCreateSchemas, ChannelsUpdateSchemas

router = APIRouter(prefix="/channels", tags=["Channels"])

@router.get("/", response_model=list[ChannelsSchemas])
def list_all_channels(db: Session = Depends(get_db)):
    channels = list_all_channels_services(db)
    if not channels:
        raise HTTPException(status_code=404, detail="No channels found")
    return channels

@router.get("/channels", response_model=list[ChannelsSchemas])
def list_all_channels_by_category(channel_category_id: int, db: Session = Depends(get_db)):
    channel_category = get_channels_by_category_services(channel_category_id)
    if not channel_category:
        raise HTTPException(status_code=404, detail="No Channels found for this category")
    return channel_category

@router.get("/{channels_id}", response_model=ChannelsSchemas)
def get_channels(channels_id: int):
    channels= get_channels_services(channels_id)
    if not channels:
        raise HTTPException(status_code=404, detail="Channels not found")
    return channels

@router.post("/new-channels", response_model=ChannelsCreateSchemas)
def add_channels(channels_data: ChannelsCreateSchemas):
    try:
        created_channels = create_channels_services(channels_data)
        return created_channels
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.put("/{channels_id}", response_model=ChannelsUpdateSchemas)
def update_channels(channels_id: int, channels_data: ChannelsUpdateSchemas):
    try:
        updated_channels = update_channels_services(channels_id, channels_data)
        if not updated_channels:
            raise HTTPException(status_code=404, detail="Channels not found")
        return updated_channels
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))