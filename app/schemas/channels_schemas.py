from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.channels_category_schemas import ChannelCategoryResponse

class ChannelsSchemas(BaseModel):
    id: int
    name: str
    image: str
    
    is_active: bool
    add_time: DateTime
    update_time: DateTime
    
    channel_category: ChannelCategoryResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class ChannelsResponse(BaseModel):
    id: int
    name: str
    image: str 
    is_active: bool
    
    channel_category: ChannelCategoryResponse
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        
class ChannelsCreateSchemas(BaseModel):
    name: str
    image: str
    is_active: bool
    add_time: DateTime    
    channel_category: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class ChannelsUpdateSchemas(BaseModel):
    name: str
    image: str
    is_active: bool
    update_time: DateTime
    channel_category: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        