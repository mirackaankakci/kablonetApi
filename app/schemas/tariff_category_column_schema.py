from datetime import datetime
from pydantic import BaseModel

from app.schemas.tariff_category_schema import TariffCategoryResponse
from app.schemas.tariff_column_schema import TariffColumnResponse


class TariffCategoryColumnResponse(BaseModel):
    id: int
    tariff_category: TariffCategoryResponse | None = None
    tariff_column: TariffColumnResponse | None = None
    is_active: bool
    add_date: datetime | None = None
    update_date: datetime | None = None

    class Config:
        from_attributes = True


class TariffCategoryColumnCreateRequest(BaseModel):
    # Incoming IDs following existing naming style; category_id in model maps from tariff_category_id here
    tariff_category_id: int
    tariff_column_id: int
    is_active: bool = True
    add_date: datetime = datetime.now()

    class Config:
        from_attributes = True


class TariffCategoryColumnUpdateRequest(BaseModel):
    tariff_category_id: int | None = None
    tariff_column_id: int | None = None
    is_active: bool | None = None
    update_date: datetime = datetime.now()

    class Config:
        from_attributes = True


class TariffCategoryColumnDeleteRequest(BaseModel):
    id: int
    deleted: bool = True