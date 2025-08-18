from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.packages_channels_services import get_packages_channels_services, create_packages_channels_services, update_packages_channels_services, list_all_packages_channels_services, get_packages_channels_by_packages
from app.schemas.packages_channels_schemas import PackagesChannelsSchemas, PackagesChannelsCreateSchemas, PackagesChannelsUpdateSchemas

router = APIRouter(prefix="/packages-channels", tags=["Packages Channels"])

@router.get("/", response_model=list[PackagesChannelsSchemas])
def list_all_packages_channels(db: Session = Depends(get_db)):
    packages_channels = list_all_packages_channels_services(db)
    if not packages_channels:
        raise HTTPException(status_code=404, detail="No packages channels found")
    return packages_channels

@router.get("/packages", response_model=list[PackagesChannelsSchemas])
def list_all_channels_by_category(packages_id: int):
    channel_packages = get_packages_channels_by_packages(packages_id)
    if not channel_packages:
        raise HTTPException(status_code=404, detail="No Packages Channels found for this Packages")
    return channel_packages

@router.get("/{packages_channels_id}", response_model=PackagesChannelsSchemas)
def get_packages_channels(packages_channels_id: int):
    packages_channels = get_packages_channels_services(packages_channels_id)
    if not packages_channels:
        raise HTTPException(status_code=404, detail="packages channels not found")
    return packages_channels

@router.post("/new-packages-channels", response_model=PackagesChannelsCreateSchemas)
def add_packages_channels(packages_channels_data: PackagesChannelsCreateSchemas):
    try:
        created_packages_channels = create_packages_channels_services(packages_channels_data)
        return created_packages_channels
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{packages_channels_id}", response_model=PackagesChannelsUpdateSchemas)
def update_packages_channels(packages_channels_id: int, packages_channels_data: PackagesChannelsUpdateSchemas):
    try:
        updated_packages_channels = update_packages_channels_services(packages_channels_id, packages_channels_data)
        if not updated_packages_channels:
            raise HTTPException(status_code=404, detail="Packages channels not found")
        return updated_packages_channels
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))