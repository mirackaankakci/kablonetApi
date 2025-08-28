from app.crud.commitment_period_crud import get_commitment_period_by_id_from_db, create_commitment_period_from_db, update_commitment_period_in_db, list_all_commitment_period_from_db, deactivate_commitment_period_from_db
from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.commitment_period_schemas import CommitmentPeriodCreateSchema
from app.db.models.commitment_period import CommitmentPeriod
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict

string_columns = [
        col.name for col in CommitmentPeriod.__table__.columns
        if isinstance(col.type, String)
    ]

def get_commitment_period_by_id(commitment_period_id: int, db: Session):
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    return get_commitment_period_by_id_from_db(commitment_period_id, db)

def create_commitment_period_service(commitment_period_data: CommitmentPeriodCreateSchema | dict, db: Session):
    commitment_period_data = ensure_dict(commitment_period_data)
    validate_list_not_empty(commitment_period_data)
    
    for col_name in string_columns:
        value = commitment_period_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value) 
    
    return create_commitment_period_from_db(commitment_period_data, db)

def update_commitment_period_service(commitment_period_data: dict, commitment_period_id: int, db: Session):
    commitment_period_data = ensure_dict(commitment_period_data)
    validate_list_not_empty(commitment_period_data)
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    
    for col_name in string_columns:
        value = commitment_period_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value) 
    
    
    return update_commitment_period_in_db(commitment_period_data, commitment_period_id, db)

def list_all_commitment_period_service(db: Session):
    commitment_period = list_all_commitment_period_from_db(db)
    validate_list_not_empty(commitment_period)
    return commitment_period

def deactivate_commitment_period_services(commitment_period_id: int, db: Session):
    get_object_by_id(CommitmentPeriod, commitment_period_id, db)
    commitment_period = deactivate_commitment_period_from_db(commitment_period_id, db)
    return commitment_period