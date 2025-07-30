from app.crud.main_category_crud import get_main_category_by_id_from_db, create_main_category_from_db

def get_main_category_by_id(main_category_id: int):
    return get_main_category_by_id_from_db(main_category_id)

def create_main_category_service(main_category_data: dict):
    return create_main_category_from_db(main_category_data)
