from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.devices_schemas import Device
from app.schemas.commitment_period_schemas import PeriodSchema

class DeviceCommitmentSchema(BaseModel):
    id: int
    price: int
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    devices: Device
    commitment_period: PeriodSchema

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class DeviceCommitmentCreateSchema(BaseModel):
    price: int
    add_time: DateTime
    is_active: bool
    devices_id: int
    commitment_period_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class DeviceCommitmentUpdateSchema(BaseModel):
    price: int
    update_time: DateTime
    is_active: bool
    devices_id: int
    commitment_period_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        