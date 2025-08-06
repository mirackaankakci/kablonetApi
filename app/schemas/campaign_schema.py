from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.main_category_schema import MainCategoryResponse



class CampaignSchema(BaseModel):
    id: int
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    add_time: DateTime
    update_time: DateTime
    campaign_notes: str | None = None
    main_category: MainCategoryResponse | None = None
    

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
class CampaignCreateSchema(BaseModel):
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    campaign_notes: str | None = None
    main_category_id: int
    add_time: DateTime
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }


class CampaignUpdateSchema(BaseModel):
    id: int
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    update_time: DateTime
    campaign_notes: str | None = None
    main_category_id: int
    class Config:
        from_attributes = True

class CampaignUpdateResponse(BaseModel):
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    update_time: DateTime
    campaign_notes: str | None = None
    main_category_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }