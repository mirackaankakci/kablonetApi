from pydantic import BaseModel
from datetime import datetime as DateTime

class ChannelCategorySchemas(BaseModel):
    id: int
    name: str
    
    is_active: bool
    add_time: DateTime
    update_time: DateTime
        
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }


class ChannelCategoryResponse(BaseModel):
    id: int
    name: str
    is_active: bool

        
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class ChannelCategoryCreateSchemas(BaseModel):
    name: str
    
    is_active: bool
    add_time: DateTime
        
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class ChannelCategoryUpdateSchemas(BaseModel):
    name: str
    
    is_active: bool
    update_time: DateTime
        
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }