from pydantic import BaseModel

class KanalListesiResponse(BaseModel):
    # id: int
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True

class KanalListesiAllResponse(BaseModel):
    id: int
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True
        
class KanalListesiCreate(BaseModel):
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True


class KanalListesiUpdate(BaseModel):
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True