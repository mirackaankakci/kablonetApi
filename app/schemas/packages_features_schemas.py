from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.packages_schemas import PackagesResponse

class PackagesFeaturesSchemas(BaseModel):
    id: int
    text: str
    
    is_active: bool
    add_time: DateTime
    update_time: DateTime
    
    packages: PackagesResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesFeaturesResponse(BaseModel):
    id: int
    text: str
    is_active: bool
    packages: PackagesResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesFeaturesCreateSchemas(BaseModel):
    text: str
    is_active: bool
    add_time: DateTime
    packages_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesFeaturesUpdateSchemas(BaseModel):
    text: str
    is_active: bool
    update_time: DateTime
    packages_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }