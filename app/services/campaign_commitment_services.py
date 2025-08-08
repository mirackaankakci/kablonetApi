from  app.crud.campaign_commitment_crud import get_campaign_commitment_by_id_from_db, create_campaign_commitment_from_db, update_campaign_commitment_from_db, get_all_campaign_commitments_from_db

def get_all_campaign_commitments_service(campaign_id: int):
    return get_all_campaign_commitments_from_db(campaign_id)

def get_campaign_commitment_by_id(commitment_id: int):
    return get_campaign_commitment_by_id_from_db(commitment_id)

def create_campaign_commitment_service(commitment_data: dict):
    return create_campaign_commitment_from_db(commitment_data)

def update_campaign_commitment_service(commitment_data: dict, commitment_id: int):
    return update_campaign_commitment_from_db(commitment_data, commitment_id)
