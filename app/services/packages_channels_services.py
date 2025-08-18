from sqlalchemy.orm import Session
from app.crud.packages_channels_crud import get_packages_channels_by_id_from_db, create_packages_channels_from_db, update_packages_channels_from_db, list_all_packages_channels_from_db, get_packages_channels_by_packages_from_db

def get_packages_channels_services(packages_channels_id: int):
    return get_packages_channels_by_id_from_db(packages_channels_id)

def create_packages_channels_services(packages_channels_data: dict):
    return create_packages_channels_from_db(packages_channels_data)

def update_packages_channels_services(packages_channels_id: int, packages_channels_data: dict):
    return update_packages_channels_from_db(packages_channels_id, packages_channels_data)

def  list_all_packages_channels_services(db: Session):
    return list_all_packages_channels_from_db(db)

def get_packages_channels_by_packages(packages_id: int):
    return get_packages_channels_by_packages_from_db(packages_id)