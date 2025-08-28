from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.main_category_schema import MainCategorySchema
from app.schemas.packages_category_schemas import PackagesCategorySchemas

class PackagesSchemas(BaseModel):
    id: int
    title: str
    content: str
    price: int
    detail:str
    
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    
    main_category: MainCategorySchema | None = None
    packages_category: PackagesCategorySchemas | None = None

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesResponse(BaseModel):
    id: int
    title: str
    content: str
    price: int
    detail:str
    is_active: bool
    
    main_category: MainCategorySchema | None = None
    packages_category: PackagesCategorySchemas | None = None
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesCreateSchemas(BaseModel):
    title: str
    content: str
    price: int
    detail:str
    add_time: DateTime
    is_active: bool
    main_category_id: int
    packages_category_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PackagesUpdateSchemas(BaseModel):
    title: str
    content: str
    price: int
    detail: str
    update_time: DateTime
    is_active: bool
    main_category_id: int
    packages_category_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        
class DeletePackagesSchemas(BaseModel):
    update_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }