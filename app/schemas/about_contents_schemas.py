from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.main_category_schema import MainCategoryResponse

class AboutContentsSchema(BaseModel):
    id: int
    title: str
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
        
class AboutContentsResponse(BaseModel):
    title: str
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
        
class AboutContentsCreateSchema(BaseModel):
    title: str
    content: str
    add_time: DateTime
    is_active: bool
    main_category_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class AboutContentsUpdateSchema(BaseModel):
    title: str
    content: str
    update_time: DateTime
    main_category_id: int

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class DeleteAboutContentsSchema(BaseModel):
    update_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }