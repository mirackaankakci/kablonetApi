from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.packages_features_schemas import PackagesFeaturesCreateSchemas
from app.db.models.packages_features import PackagesFeatures
from app.db.models.packages import Packages
from app.crud.packages_features_crud import get_packages_features_by_id_from_db, create_packages_features_from_db, update_packages_features_from_db, list_all_packages_features_from_db, get_packages_features_by_packages_from_db, deactivate_packages_features_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict

string_columns = [
        col.name for col in PackagesFeatures.__table__.columns
        if isinstance(col.type, String)
    ]

def get_packages_features_services(packages_features_id: int, db: Session):
    get_object_by_id(PackagesFeatures, packages_features_id, db)
    packages_features = get_packages_features_by_id_from_db(packages_features_id, db)
    return packages_features

def create_packages_features_services(packages_features_data: PackagesFeaturesCreateSchemas | dict, db: Session):
    packages_features_data = ensure_dict(packages_features_data)
    validate_list_not_empty(packages_features_data)
    
    packages_id = validate_required_field(
        packages_features_data.get("packages_id")
    )
    get_object_by_id(Packages, packages_id, db)
    
    # String alanlar için min uzunluk kontrolü
    for col_name in string_columns:
        value = packages_features_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)    
    
    return create_packages_features_from_db(packages_features_data, db)

def update_packages_features_services(packages_features_id: int, packages_features_data: dict, db: Session):
    packages_features_data = ensure_dict(packages_features_data)
    validate_list_not_empty(packages_features_data)
    get_object_by_id(PackagesFeatures, packages_features_id, db)
    
    packages_id = validate_required_field(
        packages_features_data.get("packages_id")
    )
    get_object_by_id(Packages, packages_id, db)
    
    # String alanlar için min uzunluk kontrolü
    for col_name in string_columns:
        value = packages_features_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)  
    return update_packages_features_from_db(packages_features_id, packages_features_data, db)

def list_all_packages_features_services(db: Session):
    packages_features = list_all_packages_features_from_db(db)
    validate_list_not_empty(packages_features)
    return packages_features

def get_packages_features_by_packages_services(packages_id: int, db: Session):
    get_object_by_id(Packages, packages_id, db)
    packages_features = get_packages_features_by_packages_from_db(packages_id, db)
    validate_list_not_empty(packages_features)
    return packages_features

def deactivate_packages_features_services(packages_features_id: int, db: Session):
    get_object_by_id(PackagesFeatures, packages_features_id, db)
    packages_features = deactivate_packages_features_from_db(packages_features_id, db)
    return packages_features