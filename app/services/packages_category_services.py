from sqlalchemy.orm import Session
from app.crud.packages_category_crud import get_packages_category_by_id_from_db,create_packages_category_from_db, update_packages_category_in_db, list_all_packages_category_from_db 

def get_packages_category_services(packages_category_id: int):
    return get_packages_category_by_id_from_db(packages_category_id)

def create_packages_category_services(packages_category_data: dict):
    return create_packages_category_from_db(packages_category_data)

def update_packages_category_services(packages_category_data: dict, packages_category_id: int):
    return update_packages_category_in_db(packages_category_data, packages_category_id)

def list_all_packages_category_services(db: Session):
    return list_all_packages_category_from_db(db)