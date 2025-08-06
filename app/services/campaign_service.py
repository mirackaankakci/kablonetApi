from app.crud.campaign_crud import get_campaign_by_id_from_db, create_campaign_from_db, update_campaign_from_db



def get_campaign_by_id(campaign_id: int):
    return get_campaign_by_id_from_db(campaign_id)


def create_campaign_service(campaign_data: dict):
    return create_campaign_from_db(campaign_data)

def update_campaign_service(campaign_data: dict, campaign_id: int):
    return update_campaign_from_db(campaign_id, campaign_data)