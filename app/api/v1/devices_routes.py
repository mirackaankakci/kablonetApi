from fastapi import APIRouter, Depends, HTTPException
from app.schemas.devices_schemas import DeviceSchema, DeviceCreateSchema, DeviceUpdateSchema
from app.services.devices_services import get_device_by_id, create_device_service, update_device_service, list_all_devices_service
from app.db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/device", tags=["Devices"])

@router.get("/", response_model=list[DeviceSchema])
def list_all_devices(db: Session = Depends(get_db)):
    devices = list_all_devices_service(db)
    if not devices:
        raise HTTPException(status_code=404, detail="No devices found")
    return devices

@router.get("/{device_id}", response_model=DeviceSchema)
def get_device(device_id: int):
    device= get_device_by_id(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device

@router.post("/new-device", response_model=DeviceCreateSchema)
def add_device(device_data: DeviceCreateSchema):
    try:
        created_device = create_device_service(device_data)
        return created_device
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{device_id}", response_model=DeviceUpdateSchema)
def update_device(device_id: int, device_data: DeviceUpdateSchema):
    try:
        updated_device = update_device_service(device_data, device_id)
        if not updated_device:
            raise HTTPException(status_code=404, detail="Device not found")
        return updated_device
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))