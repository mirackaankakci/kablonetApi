from sqlalchemy.orm import Session
from app.crud.packages_crud import get_packages_by_id_from_db,create_packages_from_db,update_packages_from_db,list_all_packages_from_db, get_packages_by_category_id_from_db

def get_packages_services(packages_id: int):
    return get_packages_by_id_from_db(packages_id)

def create_packages_services(packages_data: dict):
    return create_packages_from_db(packages_data)

def update_packages_services(packages_id: int ,packages_data: dict):
    return update_packages_from_db(packages_id,packages_data)

def list_all_packages_services(db: Session):
    return list_all_packages_from_db(db)

def get_packages_by_category_services(packages_category_id: int):
    return get_packages_by_category_id_from_db(packages_category_id)