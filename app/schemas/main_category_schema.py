from pydantic import BaseModel

class MainCategoryResponse(BaseModel):
    id: int
    name: str
    isActive: bool

    class Config:
        orm_mode = True


class MainCategoryCreateResponse(BaseModel):
    name: str
    isActive: bool

    class Config:
        orm_mode = True

class MainCategoryUpdateResponse(BaseModel):
    id: int
    name: str
    isActive: bool

    class Config:
        orm_mode = True
