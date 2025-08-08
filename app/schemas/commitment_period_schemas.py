from pydantic import BaseModel
from datetime import datetime as DateTime

class CommitmentPeriodSchema(BaseModel):
    id: int
    period: str  # taahüt süresi (örneğin: "12 months")
    add_time: DateTime
    update_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class PeriodSchema(BaseModel):
    id: int
    period: str  # taahüt süresi (örneğin: "12 months")
    is_active: bool

    class Config:
        from_attributes = True
        
class CommitmentPeriodResponse(BaseModel):
    period: str  # taahüt süresi (örneğin: "12 months")
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class CommitmentPeriodCreateSchema(BaseModel):
    period: str  # taahüt süresi (örneğin: "12 months")
    add_time: DateTime
    is_active: bool = True  # Varsayılan değer

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class CommitmentPeriodUpdateSchema(BaseModel):
    period: str  # taahüt süresi (örneğin: "12 months")
    update_time: DateTime
    is_active: bool

    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }