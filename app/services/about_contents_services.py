from app.crud.about_contents_crud import get_about_content_by_id_from_db, create_about_content_from_db, update_about_content_from_db, get_all_about_contents_from_db, get_all_about_contents_by_category_from_db
from sqlalchemy.orm import Session
from sqlalchemy import Integer, String
from app.db.models.about_contents import About_Contents
from app.db.models.MainCategory import MainCategory
from app.services.util import get_object_by_id, validate_required_field, validate_min_length, validate_list_not_empty, get_all_ready_have_id,ensure_dict

string_columns = [
        col.name for col in About_Contents.__table__.columns
        if isinstance(col.type, String)
    ]

def get_about_content_service(content_id: int, db: Session):
    get_object_by_id(About_Contents, content_id, db)
    return get_about_content_by_id_from_db(content_id, db)

## Get all about contents from the database
def get_all_about_contents_service(db: Session):
    about_contents = get_all_about_contents_from_db(db)
    validate_list_not_empty(about_contents)
    return about_contents

def create_about_content_service(content_data: dict, db: Session):
    content_data= ensure_dict(content_data)
    validate_list_not_empty(content_data)
    
    main_category_id=validate_required_field(content_data.get("main_category_id"))
    get_object_by_id(MainCategory, main_category_id, db)    

    for col_name in string_columns:
        value = content_data.get(col_name)
        if isinstance(value, str):  # sadece string ise kontrol et
            validate_min_length(value)    
    
    return create_about_content_from_db(content_data, db)

## Get all about contents by category from the database
def get_all_about_contents_by_category_service(main_category_id: int, db: Session):
    get_object_by_id(MainCategory, main_category_id, db)
    about_contents = get_all_about_contents_by_category_from_db(main_category_id, db)
    validate_list_not_empty(about_contents)
    return about_contents

def update_about_content_service(content_data: dict, content_id: int, db: Session):
    content_data= ensure_dict(content_data)
    validate_list_not_empty(content_data)
    
    get_object_by_id(About_Contents, main_category_id, db)
    
    main_category_id=validate_required_field(content_data.get("main_category_id"))
    get_object_by_id(MainCategory, main_category_id, db)
    
        
    for col_name in string_columns:
        if col_name in content_data and content_data.get(col_name) is not None:
            validate_min_length(content_data.get(col_name))
    
    return update_about_content_from_db(content_data, content_id, db)