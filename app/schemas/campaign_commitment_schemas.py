from pydantic import BaseModel
from datetime import datetime as DateTime
from app.schemas.commitment_period_schemas import PeriodSchema
from app.schemas.campaign_schema import CampaignInfoSchema

class CampaignCommitmentSchema(BaseModel):
    id: int
    price: int
    add_time: DateTime
    update_time: DateTime
    is_active: bool
    campaign: CampaignInfoSchema
    commitment_period: PeriodSchema
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }

class CampaignCommitmentCreateSchema(BaseModel):
    price: int
    add_time: DateTime
    is_active: bool = True  # Varsayılan değer
    campaign_id: int
    commitment_period_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
class CampaignCommitmentUpdateSchema(BaseModel):
    price: int
    update_time: DateTime
    is_active: bool
    campaign_id: int
    commitment_period_id: int
    
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        
class DeleteCampaignCommitmentSchema(BaseModel):
    update_time: DateTime
    is_active: bool
    class Config:
        from_attributes = True
        json_encoders = {
            DateTime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        