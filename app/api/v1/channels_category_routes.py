from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.channels_category_services import get_channel_category_services, create_channel_category_services, update_channel_category_services, list_all_channel_category_services, deactivate_channel_category_services
from app.schemas.channels_category_schemas import ChannelCategorySchemas, ChannelCategoryResponse, ChannelCategoryCreateSchemas, ChannelCategoryUpdateSchemas, DeleteChannelCategorySchemas
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator

router = APIRouter(prefix="/channels-category", tags=["Channels Category"])

@router.get("/", response_model=list[ChannelCategorySchemas])
def list_all_channels_category(db: Session = Depends(get_db)):
    channels_category = list_all_channel_category_services(db)
    return channels_category

@router.get("/{channel_category_id}", response_model=ChannelCategorySchemas)
def get_channels_category(channel_category_id: int, db: Session = Depends(get_db)):
    channels_category= get_channel_category_services(channel_category_id, db)
    return channels_category

@router.post("/new-channels-category", response_model=ChannelCategoryCreateSchemas, summary="Create New Channel Category (Admin Only)")
def add_channels_category(
    channel_category_data: ChannelCategoryCreateSchemas, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    created_channels_category = create_channel_category_services(channel_category_data, db)
    return created_channels_category

@router.put("/{channel_category_id}", response_model=ChannelCategoryUpdateSchemas, summary="Update Channel Category (Admin Only)")
def update_channels_category(
    channel_category_id: int, 
    channel_category_data: ChannelCategoryUpdateSchemas, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_channels_category = update_channel_category_services(channel_category_data, channel_category_id, db)
    return updated_channels_category


@router.delete("/{channel_category_id}", response_model= DeleteChannelCategorySchemas, summary="Delete Channel Category (Admin Only)")
def deactivate_channel_category(
    channel_category_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_channel_category_services(channel_category_id, db)
    return deactivate