from pydantic import BaseModel
from app.schemas.main_category_schema import MainCategoryResponse



class CampaignSchema(BaseModel):
    id: int
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    start_date: str
    campaign_notes: str | None = None
    main_category: MainCategoryResponse | None = None
    

    class Config:
        from_attributes = True

class CampaignCreateSchema(BaseModel):
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    start_date: str
    campaign_notes: str | None = None
    main_category_id: int


class CampaignUpdateSchema(BaseModel):
    name: str
    feature_table: str | None = None
    image_url: str | None = None
    is_active: bool = True
    subheading: str | None = None
    start_date: str
    campaign_notes: str | None = None
    main_category_id: int