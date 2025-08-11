from pydantic import BaseModel
from datetime import datetime as DateTime

class MainCategoryResponse(BaseModel):
    id: int
    name: str
    isActive: bool
    add_time: DateTime
    update_time: DateTime

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class MainCategorySchema(BaseModel):
    id: int
    name: str
    isActive: bool = True  # Varsayılan değer
    class Config:
        from_attributes = True


class MainCategoryCreateResponse(BaseModel):
    name: str
    isActive: bool = True  # Varsayılan değer
    add_time: DateTime

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }


class MainCategoryUpdateResponse(BaseModel):
    # id: int
    name: str
    isActive: bool
    update_time: DateTime
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class MainCategoryUpdate(BaseModel):
    name: str
    isActive: bool
    update_time: DateTime

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

