from sqlalchemy.orm import Session
from app.crud.packages_features_crud import get_packages_features_by_id_from_db, create_packages_features_from_db, update_packages_features_from_db, list_all_packages_features_from_db

def get_packages_features_services(packages_features_id: int):
    return get_packages_features_by_id_from_db(packages_features_id)

def create_packages_features_services(packages_features_data: dict):
    return create_packages_features_from_db(packages_features_data)

def update_packages_features_services(packages_features_id: int, packages_features_data: dict):
    return update_packages_features_from_db(packages_features_id, packages_features_data)

def list_all_packages_features_services(db: Session):
    return list_all_packages_features_from_db(db)

