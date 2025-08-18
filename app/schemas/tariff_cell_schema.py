from datetime import datetime
from pydantic import BaseModel
from app.schemas.tariff_category_schema import TariffCategoryResponse
from app.schemas.tariff_line_schema import TariffLineResponse
from app.schemas.tariff_column_schema import TariffColumnResponse
from app.schemas.tariff_value_schema import TariffValueResponse



class TariffCellResponse(BaseModel):
    id: int
    tariff_line: TariffLineResponse | None = None
    tariff_column: TariffColumnResponse | None = None
    tariff_value: TariffValueResponse | None = None
    tariff_line_id: int
    tariff_column_id: int
    tariff_value_id: int
    is_active: bool
    add_date: datetime | None = None
    update_date: datetime | None = None

    class Config:
        from_attributes = True




class TariffCellCreate(BaseModel):
    tariff_line_id: int
    tariff_column_id: int
    tariff_value_id: int
    is_active: bool = True
    add_date: datetime | None = None


class TariffCellUpdate(BaseModel):
    tariff_line_id: int | None = None
    tariff_column_id: int | None = None
    tariff_value_id: int | None = None
    is_active: bool | None = None
    update_date: datetime | None = None


class TariffCellDelete(BaseModel):
    id: int
    deletede: bool = True