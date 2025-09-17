from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.channels_services import get_channels_services, create_channels_services, update_channels_services, list_all_channels_services, get_channels_by_category_services, deactivate_channels_services
from app.schemas.channels_schemas import ChannelsSchemas, ChannelsResponse, ChannelsCreateSchemas, ChannelsUpdateSchemas, DeleteChannelsSchemas
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator

router = APIRouter(prefix="/channels", tags=["Channels"])

@router.get("/", response_model=list[ChannelsSchemas])
def list_all_channels(db: Session = Depends(get_db)):
    channels = list_all_channels_services(db)
    return channels

@router.get("/channels", response_model=list[ChannelsSchemas])
def list_all_channels_by_category(channel_category_id: int, db: Session = Depends(get_db)):
    channel_category = get_channels_by_category_services(channel_category_id, db)
    return channel_category

@router.get("/{channels_id}", response_model=ChannelsSchemas)
def get_channels(channels_id: int, db: Session = Depends(get_db)):
    channels= get_channels_services(channels_id, db)
    return channels

@router.post("/new-channels", response_model=ChannelsCreateSchemas, summary="Create New Channel (Admin Only)")
def add_channels(
    channels_data: ChannelsCreateSchemas, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    created_channels = create_channels_services(channels_data, db)
    return created_channels
    
@router.put("/{channels_id}", response_model=ChannelsUpdateSchemas, summary="Update Channel (Admin Only)")
def update_channels(
    channels_id: int, 
    channels_data: ChannelsUpdateSchemas, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_channels = update_channels_services(channels_id, channels_data, db)
    return updated_channels

@router.delete("/{channels_id}", response_model= DeleteChannelsSchemas, summary="Delete Channel (Admin Only)")
def deactivate_channels(
    channels_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_channels_services(channels_id, db)
    return deactivate