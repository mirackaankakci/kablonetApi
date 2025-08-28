from app.crud.campaign_crud import get_campaign_by_id_from_db, create_campaign_from_db, update_campaign_from_db, get_all_campaigns_from_db, get_all_campaigns_by_category_from_db, deactivate_campaign_from_db
from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.campaign_schema import CampaignCreateSchema
from app.db.models.campaign_features import CampaignFeatures
from app.db.models.Campaign import Campaign
from app.db.models.MainCategory import MainCategory
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict
    

# Minimum karakter sayısı (istersen her kolona özel de yapabilirsin)

string_columns = [
        col.name for col in Campaign.__table__.columns
        if isinstance(col.type, String)
    ]

# int_columns = [
#         col.name for col in Campaign.__table__.columns
#         if isinstance(col.type, Integer)
# ]


def get_campaign_by_id_service(campaign_id: int, db: Session):
    get_object_by_id(Campaign, campaign_id, db)
    return get_campaign_by_id_from_db(campaign_id,db)

def get_all_campaigns_service(db: Session):
    campaigns = get_all_campaigns_from_db(db)
    validate_list_not_empty(campaigns)
    return campaigns

def get_all_campaigns_by_category_service(main_category_id: int, db: Session):
    get_object_by_id(MainCategory, main_category_id, db)
    campaigns = get_all_campaigns_by_category_from_db(main_category_id, db)
    # Liste boşsa 404 kontrolü
    validate_list_not_empty(campaigns)
    return campaigns

def create_campaign_service(campaign_data: CampaignCreateSchema | dict, db: Session):
    # Eğer Pydantic model ise, model_dump() ile dict'e çevir
    campaign_data = ensure_dict(campaign_data)
    
    # Boş veri kontrolü
    validate_list_not_empty(campaign_data)  # Aşağıda düzelttik

    # Zorunlu alanlar: campaign_features_id
    campaign_features_id = validate_required_field(
        campaign_data.get("campaign_features_id")
    )
    get_object_by_id(CampaignFeatures, campaign_features_id, db)

    # main_category_id kontrolü
    main_category_id = validate_required_field(
        campaign_data.get("main_category_id")
    )
    get_object_by_id(MainCategory, main_category_id, db)

    # String alanlar için min uzunluk kontrolü
    for col_name in string_columns:
        value = campaign_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)

    return create_campaign_from_db(campaign_data, db)



def update_campaign_service(campaign_data: dict, campaign_id: int, db: Session):

    # Eğer Pydantic model ise, model_dump() ile dict'e çevir
    campaign_data = ensure_dict(campaign_data)

    validate_list_not_empty(campaign_data)
    get_object_by_id(Campaign, campaign_id, db)

    # campaign_features kontrolü
    campaign_features_id = validate_required_field(campaign_data.get("campaign_features_id"))
    get_object_by_id(CampaignFeatures, campaign_features_id, db)

    # main_category kontrolü
    main_category_id = validate_required_field(campaign_data.get("main_category_id"))
    get_object_by_id(MainCategory, main_category_id, db)

    # string alanlar için min length kontrolü
    for col_name in string_columns:
        if col_name in campaign_data and campaign_data.get(col_name) is not None:
            validate_min_length(campaign_data.get(col_name))

    return update_campaign_from_db(campaign_id, campaign_data,db)

def deactivate_campaign_services(campaign_id: int, db: Session):
    get_object_by_id(Campaign, campaign_id, db)
    campaigns = deactivate_campaign_from_db(campaign_id, db)
    return campaigns