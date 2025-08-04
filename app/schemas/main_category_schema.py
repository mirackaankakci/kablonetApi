from pydantic import BaseModel

class MainCategoryResponse(BaseModel):
    id: int
    name: str
    isActive: bool

    class Config:
        from_attributes = True



class MainCategoryCreateResponse(BaseModel):
    name: str
    isActive: bool

    class Config:
        from_attributes = True


class MainCategoryUpdateResponse(BaseModel):
    id: int
    name: str
    isActive: bool
    class Config:
        from_attributes = True

