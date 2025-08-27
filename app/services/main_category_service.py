from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from app.db.models.MainCategory import MainCategory
from app.crud.main_category_crud import get_main_category_by_id_from_db, create_main_category_from_db, update_main_category_in_db, get_all_main_categories_from_db
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty, get_all_ready_have_id,ensure_dict

string_columns = [
        col.name for col in MainCategory.__table__.columns
        if isinstance(col.type, String)
    ]

def get_main_category_by_id(main_category_id: int, db: Session):
    get_object_by_id(MainCategory, main_category_id, db)
    return get_main_category_by_id_from_db(main_category_id, db)

def create_main_category_service(main_category_data: dict, db: Session):
    main_category_data= ensure_dict(main_category_data)
    validate_list_not_empty(main_category_data)
    
    for col_name in string_columns:
        value = main_category_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)

    return create_main_category_from_db(main_category_data, db)


def update_main_category_service(main_category_data: dict, main_category_id: int, db: Session):
    main_category_data= ensure_dict(main_category_data)
    validate_list_not_empty(main_category_data)
    get_object_by_id(MainCategory, main_category_id, db)
    
    for col_name in string_columns:
        if col_name in main_category_data and main_category_data.get(col_name) is not None:
            validate_min_length(main_category_data.get(col_name))
    
    updated_category = update_main_category_in_db(main_category_data, main_category_id, db)
    return updated_category

def get_all_main_categories_service(db: Session):
    main_categories = get_all_main_categories_from_db(db)
    validate_list_not_empty(main_categories)
    return main_categories
    