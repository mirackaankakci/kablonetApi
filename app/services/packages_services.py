from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.packages_schemas import PackagesCreateSchemas
from app.db.models.packages import Packages
from app.db.models.MainCategory import MainCategory
from app.db.models.packages_category import PackagesCategory
from app.crud.packages_crud import get_packages_by_id_from_db,create_packages_from_db,update_packages_from_db,list_all_packages_from_db, get_packages_by_category_id_from_db, deactivate_packages_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict

string_columns = [
        col.name for col in Packages.__table__.columns
        if isinstance(col.type, String)
    ]

def get_packages_services(packages_id: int, db: Session):
    get_object_by_id(Packages, packages_id, db)
    packages = get_packages_by_id_from_db(packages_id, db)
    return packages

def create_packages_services(packages_data: PackagesCreateSchemas | dict, db: Session):
    packages_data = ensure_dict(packages_data)
    validate_list_not_empty(packages_data)
    
    main_category_id = validate_required_field(
        packages_data.get("main_category_id")
    )
    get_object_by_id(MainCategory, main_category_id, db)
    
    packages_category_id = validate_required_field(
        packages_data.get("packages_category_id")
    )
    get_object_by_id(PackagesCategory, packages_category_id, db)
    
    for col_name in string_columns:
        value = packages_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return create_packages_from_db(packages_data, db)

def update_packages_services(packages_id: int ,packages_data: dict, db: Session):
    packages_data = ensure_dict(packages_data)
    validate_list_not_empty(packages_data)
    get_object_by_id(Packages, packages_id, db)
    
    main_category_id = validate_required_field(
        packages_data.get("main_category_id")
    )
    get_object_by_id(MainCategory, main_category_id, db)
    
    packages_category_id = validate_required_field(
        packages_data.get("packages_category_id")
    )
    get_object_by_id(PackagesCategory, packages_category_id, db)
    
    for col_name in string_columns:
        value = packages_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
            
    return update_packages_from_db(packages_id,packages_data, db)

def list_all_packages_services(db: Session):
    packages = list_all_packages_from_db(db)
    validate_list_not_empty(packages)
    return packages

def get_packages_by_category_services(packages_category_id: int, db: Session):
    get_object_by_id(PackagesCategory, packages_category_id, db)
    packages = get_packages_by_category_id_from_db(packages_category_id, db)
    validate_list_not_empty(packages)
    return packages

def deactivate_packages_services(packages_id: int, db: Session):
    get_object_by_id(Packages, packages_id, db)
    packages = deactivate_packages_from_db(packages_id, db)
    return packages