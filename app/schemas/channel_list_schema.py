from pydantic import BaseModel

class ChannelListResponse(BaseModel):
    # id: int
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True

class ChannelListAllResponse(BaseModel):
    id: int
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True
        
class ChannelListCreate(BaseModel):
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True


class ChannelListUpdate(BaseModel):
    kanal_no: int
    kanal_adi: str
    dijital_frekans: str
    analog_frekans: str

    class Config:
        from_attributes = True