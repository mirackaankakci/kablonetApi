from datetime import datetime
from pydantic import BaseModel
from app.schemas.tariff_category_schema import TariffCategoryResponse



class TariffLineResponse(BaseModel):
    id: int
    tariff_category: TariffCategoryResponse | None = None
    tariff_category_id: int | None = None
    is_active: bool = True

    class Config:
        from_attributes = True

class TariffLineCreateRequest(BaseModel):
    tariff_category_id: int
    is_active: bool = True

class TariffLineUpdateRequest(BaseModel):
    tariff_category_id: int | None = None
    is_active: bool | None = None

class TariffLineDeleteRequest(BaseModel):
    id: int
    deleted: bool = True
