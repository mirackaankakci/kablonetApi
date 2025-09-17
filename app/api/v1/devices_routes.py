from fastapi import APIRouter, Depends, HTTPException
from app.schemas.devices_schemas import DeviceSchema, DeviceCreateSchema, DeviceUpdateSchema, DeleteDeviceSchema
from app.services.devices_services import get_device_by_id, create_device_service, update_device_service, list_all_devices_service, deactivate_devices_services, get_device_by_category_services
from app.db.database import get_db
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator
from sqlalchemy.orm import Session

router = APIRouter(prefix="/device", tags=["Devices"])

@router.get("/", response_model=list[DeviceSchema], summary="Get All Devices (Public)")
def list_all_devices(db: Session = Depends(get_db)):
    devices = list_all_devices_service(db)
    return devices

@router.get("/{device_id}", response_model=DeviceSchema, summary="Get Device by ID (Public)")
def get_device(device_id: int, db: Session = Depends(get_db)):
    device= get_device_by_id(device_id, db)
    return device

@router.get("/category/{main_category_id}", response_model=list[DeviceSchema], summary="Get Devices by Category (Public)")
def get_device_by_category(main_category_id: int, db: Session = Depends(get_db)):
    device_category= get_device_by_category_services(main_category_id, db)
    return device_category

@router.post("/new-device", response_model=DeviceCreateSchema, summary="Create New Device (Admin Only)")
def add_device(
    device_data: DeviceCreateSchema, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    created_device = create_device_service(device_data, db)
    return created_device

@router.put("/{device_id}", response_model=DeviceUpdateSchema, summary="Update Device (Admin Only)")
def update_device(
    device_id: int, 
    device_data: DeviceUpdateSchema, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_device = update_device_service(device_data, device_id, db)
    return updated_device

@router.delete("/{device_id}", response_model=DeleteDeviceSchema, summary="Delete Device (Admin Only)")
def deactivate_devices(
    device_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_devices_services(device_id, db)
    return deactivate

