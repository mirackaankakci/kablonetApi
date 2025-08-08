from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.main_category_schema import MainCategoryResponse
from app.schemas.main_category_schema import MainCategorySchema


class DeviceSchema(BaseModel):
    id: int
    device_name: str
    device_title: str
    content: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    main_category: MainCategoryResponse | None = None

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class Device(BaseModel):
    id: int
    device_name: str
    device_title: str
    content: str | None = None
    is_active: bool
    main_category: MainCategorySchema

    class Config:
        from_attributes = True
        
class DeviceCreateSchema(BaseModel):
    device_name: str
    device_title: str
    content: str | None = None
    add_time: DateTime
    is_active: bool
    main_category_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class DeviceUpdateSchema(BaseModel):
    device_name: str
    device_title: str
    content: str | None = None
    update_time: DateTime
    is_active: bool
    main_category_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }