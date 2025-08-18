from pydantic import BaseModel
from datetime import datetime as DateTime

class PackagesCategorySchemas(BaseModel):
    id: int
    name: str
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
    
class PackagesCategoryResponse(BaseModel):
    id: int
    name: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }


class PackagesCategoryCreateResponse(BaseModel):
    # id: int
    name: str
    add_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class PackagesCategoryUpdateResponse(BaseModel):
    # id: int
    name: str
    update_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }