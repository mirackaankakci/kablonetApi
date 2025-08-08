from pydantic import BaseModel
from datetime import datetime as DateTime

class ChannelListResponse(BaseModel):
    id: int
    channel_no: int
    channel_name: str
    digital_frequency: str
    analog_frequency: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class ChannelListAllResponse(BaseModel):
    # id: int
    channel_no: int
    channel_name: str
    digital_frequency: str
    analog_frequency: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool

    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class ChannelListCreate(BaseModel):
    channel_no: int
    channel_name: str
    digital_frequency: str
    analog_frequency: str
    add_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class ChannelListUpdate(BaseModel):
    channel_no: int
    channel_name: str
    digital_frequency: str
    analog_frequency: str
    update_time: DateTime
    is_active: bool
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }