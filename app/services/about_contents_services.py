from app.crud.about_contents_crud import get_about_content_by_id_from_db, create_about_content_from_db, update_about_content_from_db, get_all_about_contents_from_db, get_all_about_contents_by_category_from_db
from sqlalchemy.orm import Session

def get_about_content_service(content_id: int):
    return get_about_content_by_id_from_db(content_id)

def create_about_content_service(content_data: dict):
    return create_about_content_from_db(content_data)

## Get all about contents from the database
def get_all_about_contents_service(db: Session):
    return get_all_about_contents_from_db(db)

## Get all about contents by category from the database
def get_all_about_contents_by_category_service(main_category_id: int):
    return get_all_about_contents_by_category_from_db(main_category_id)

def update_about_content_service(content_data: dict, content_id: int):
    return update_about_content_from_db(content_data, content_id)