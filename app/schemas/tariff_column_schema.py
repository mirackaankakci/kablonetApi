from datetime import datetime
from pydantic import BaseModel



class TariffColumnResponse(BaseModel):
    id: int
    name: str
    number: int
    add_date: datetime = datetime.now()
    is_active: bool = True

    class Config:
        from_attributes = True




class TariffColumnCreateRequest(BaseModel):
    name: str
    number: int
    add_date: datetime = datetime.now()
    is_active: bool = True




class TariffColumnUpdateRequest(BaseModel):
    name: str | None = None
    number: int | None = None
    update_date: datetime = datetime.now()
    is_active: bool = True


class TariffColumnDeleteRequest(BaseModel):
    id: int
    deleted: bool = True