from pydantic import BaseModel
from datetime import datetime as DateTime

class CampaignFeaturesSchema(BaseModel):
    id: int
    pricing_HTML: str
    detail_HTML: str
    devices: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class FeaturesSchema(BaseModel):
    id: int
    pricing_HTML: str
    detail_HTML: str | None = None
    devices: str | None = None
    is_active: bool

    class Config:
        from_attributes = True
class CampaignFeaturesResponse(BaseModel):
    pricing_HTML: str
    detail_HTML: str
    devices: str
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class CampaignFeaturesCreateSchema(BaseModel):
    pricing_HTML: str
    detail_HTML: str | None = None
    devices: str | None = None
    add_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class CampaignFeaturesUpdateSchema(BaseModel):
    pricing_HTML: str
    detail_HTML: str | None = None
    devices: str | None = None
    update_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
