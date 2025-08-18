from datetime import datetime
from pydantic import BaseModel, Field


class TariffValueResponse(BaseModel):
    id: int
    value: str
    is_active: bool = True
    add_date: datetime | None = None
    update_date: datetime | None = None

    class Config:
        from_attributes = True
        validate_by_name = True


class TariffValueCreateRequest(BaseModel):
    value: str
    is_active: bool = True
    add_date: datetime | None = None

    class Config:
        validate_by_name = True



class TariffValueUpdateRequest(BaseModel):
    value: str | None = None
    is_active: bool = True
    add_date: datetime | None = None
    update_date: datetime | None = None

    class Config:
        validate_by_name = True


class TariffValueDeleteRequest(BaseModel):
    id: int
    deleted: bool = True