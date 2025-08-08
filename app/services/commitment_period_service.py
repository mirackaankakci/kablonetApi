from app.crud.commitment_period_crud import get_commitment_period_by_id_from_db, create_commitment_period_from_db, update_commitment_period_in_db

def get_commitment_period_by_id(commitment_period_id: int):
    return get_commitment_period_by_id_from_db(commitment_period_id)

def create_commitment_period_service(commitment_period_data: dict):
    return create_commitment_period_from_db(commitment_period_data)

def update_commitment_period_service(commitment_period_data: dict, commitment_period_id: int):
    return update_commitment_period_in_db(commitment_period_data, commitment_period_id)