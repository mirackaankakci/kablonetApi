from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.services.channels_category_services import get_channel_category_services, create_channel_category_services, update_channel_category_services, list_all_channel_category_services
from app.schemas.channels_category_schemas import ChannelCategorySchemas, ChannelCategoryResponse, ChannelCategoryCreateSchemas, ChannelCategoryUpdateSchemas

router = APIRouter(prefix="/channels-category", tags=["Channels Category"])

@router.get("/", response_model=list[ChannelCategorySchemas])
def list_all_channels_category(db: Session = Depends(get_db)):
    channels_category = list_all_channel_category_services(db)
    if not channels_category:
        raise HTTPException(status_code=404, detail="No channels category found")
    return channels_category

@router.get("/{channel_category_id}", response_model=ChannelCategorySchemas)
def get_channels_category(channel_category_id: int):
    channels_category= get_channel_category_services(channel_category_id)
    if not channels_category:
        raise HTTPException(status_code=404, detail="channels category not found")
    return channels_category

@router.post("/new-channels-category", response_model=ChannelCategoryCreateSchemas)
def add_channels_category(channel_category_data: ChannelCategoryCreateSchemas):
    try:
        created_channels_category = create_channel_category_services(channel_category_data)
        return created_channels_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{channel_category_id}", response_model=ChannelCategoryUpdateSchemas)
def update_channels_category(channel_category_id: int, channel_category_data: ChannelCategoryUpdateSchemas):
    try:
        updated_channels_category = update_channel_category_services(channel_category_data, channel_category_id)
        if not updated_channels_category:
            raise HTTPException(status_code=404, detail="channels category not found")
        return updated_channels_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))