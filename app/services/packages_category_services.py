from sqlalchemy.orm import Session
from sqlalchemy import String
from app.schemas.packages_category_schemas import PackagesCategoryCreateResponse
from app.crud.packages_category_crud import get_packages_category_by_id_from_db,create_packages_category_from_db, update_packages_category_in_db, list_all_packages_category_from_db, deactivate_packages_category_from_db 
from app.db.models.packages_category import PackagesCategory
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty ,ensure_dict, validate_non_negative_fields, validate_required_keys

string_columns = [
        col.name for col in PackagesCategory.__table__.columns
        if isinstance(col.type, String)
    ]

def get_packages_category_services(packages_category_id: int, db: Session):
    get_object_by_id(PackagesCategory, packages_category_id, db)
    return get_packages_category_by_id_from_db(packages_category_id, db)

def create_packages_category_services(packages_category_data: PackagesCategoryCreateResponse | dict, db: Session):
    packages_category_data = ensure_dict(packages_category_data)
    validate_list_not_empty(packages_category_data)
    
    validate_non_negative_fields(PackagesCategory, packages_category_data)
    validate_required_keys(PackagesCategory, packages_category_data)
    # validate_datetime_fields(PackagesCategory, packages_category_data, allow_none=True)
    # validate_unique_field(model=PackagesCategory, data=packages_category_data, db=db)
    
    for col_name in string_columns:
        value = packages_category_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    
    return create_packages_category_from_db(packages_category_data, db)

def update_packages_category_services(packages_category_data: dict, packages_category_id: int, db: Session):
    packages_category_data = ensure_dict(packages_category_data)
    validate_list_not_empty(packages_category_data)
    get_object_by_id(PackagesCategory, packages_category_id, db)
    
    validate_non_negative_fields(PackagesCategory, packages_category_data)
    validate_required_keys(PackagesCategory, packages_category_data)
    # validate_datetime_fields(PackagesCategory, packages_category_data, allow_none=True)
    # validate_unique_field(model=PackagesCategory, data=packages_category_data, exclude_id=packages_category_id ,db=db)
    
    for col_name in string_columns:
        value = packages_category_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)
    return update_packages_category_in_db(packages_category_data, packages_category_id, db)

def list_all_packages_category_services(db: Session):
    packages_category = list_all_packages_category_from_db(db)
    validate_list_not_empty(packages_category)
    return packages_category

def deactivate_packages_category_services(packages_category_id: int, db: Session):
    get_object_by_id(PackagesCategory, packages_category_id, db)
    packages_category = deactivate_packages_category_from_db(packages_category_id, db)
    return packages_category