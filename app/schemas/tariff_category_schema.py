from datetime import datetime
from pydantic import BaseModel
from app.schemas.main_category_schema import MainCategoryResponse


class TariffCategoryResponse(BaseModel):
    id: int
    name: str
    is_active: bool = True
    add_date: str | None = None
    update_date: str | None = None
    important_information: str | None = None
    main_category: MainCategoryResponse | None = None

    class Config:
        from_attributes = True


class TariffCategoryCreatedResponse(BaseModel):
    name: str
    is_active: bool = True
    add_date: datetime = datetime.now()
    important_information: str | None = None
    main_category_id: int | None = None

    class Config:
        from_attributes = True


class TariffCategoryUpdateResponse(BaseModel):
    name: str
    update_date: datetime = datetime.now()
    class Config:
        from_attributes = True