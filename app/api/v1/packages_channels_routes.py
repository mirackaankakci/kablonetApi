from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.packages_channels_services import get_packages_channels_services, create_packages_channels_services, update_packages_channels_services, list_all_packages_channels_services, get_packages_channels_by_packages, deactivate_packages_channels_services
from app.schemas.packages_channels_schemas import PackagesChannelsSchemas, PackagesChannelsCreateSchemas, PackagesChannelsUpdateSchemas, DeletePackagesChannelsSchemas

router = APIRouter(prefix="/packages-channels", tags=["Packages Channels"])

@router.get("/", response_model=list[PackagesChannelsSchemas])
def list_all_packages_channels(db: Session = Depends(get_db)):
    packages_channels = list_all_packages_channels_services(db)
    return packages_channels

@router.get("/packages", response_model=list[PackagesChannelsSchemas])
def list_all_channels_by_packages(packages_id: int, db: Session = Depends(get_db)):
    channel_packages = get_packages_channels_by_packages(packages_id, db)
    return channel_packages

@router.get("/{packages_channels_id}", response_model=PackagesChannelsSchemas)
def get_packages_channels(packages_channels_id: int, db: Session = Depends(get_db)):
    packages_channels = get_packages_channels_services(packages_channels_id, db)
    return packages_channels

@router.post("/new-packages-channels", response_model=PackagesChannelsCreateSchemas)
def add_packages_channels(packages_channels_data: PackagesChannelsCreateSchemas, db: Session = Depends(get_db)):
    created_packages_channels = create_packages_channels_services(packages_channels_data, db)
    return created_packages_channels

@router.put("/{packages_channels_id}", response_model=PackagesChannelsUpdateSchemas)
def update_packages_channels(packages_channels_id: int, packages_channels_data: PackagesChannelsUpdateSchemas, db: Session = Depends(get_db)):
    updated_packages_channels = update_packages_channels_services(packages_channels_id, packages_channels_data, db)
    return updated_packages_channels

@router.delete("/{packages_channels_id}", response_model= DeletePackagesChannelsSchemas)
def deactivate_packages_channels(packages_channels_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_packages_channels_services(packages_channels_id, db)
    return deactivate