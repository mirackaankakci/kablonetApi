from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.channels_schemas import ChannelsResponse
from app.schemas.packages_schemas import PackagesResponse

class PackagesChannelsSchemas(BaseModel):
    id: int
    
    is_active: bool
    add_time: DateTime
    update_time: DateTime
    
    channels: ChannelsResponse
    packages: PackagesResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesChannelsSchemas(BaseModel):
    id: int
    is_active: bool
    
    channels: ChannelsResponse
    packages: PackagesResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesChannelsCreateSchemas(BaseModel):
    is_active: bool
    add_time: DateTime
    channels_id: int
    packages_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesChannelsUpdateSchemas(BaseModel):
    is_active: bool
    update_time: DateTime
    channels_id: int
    packages_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
