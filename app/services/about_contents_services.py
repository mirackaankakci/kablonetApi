from app.crud.about_contents_crud import get_about_content_by_id_from_db, create_about_content_from_db, update_about_content_from_db

def get_about_content_service(content_id: int):
    return get_about_content_by_id_from_db(content_id)

def create_about_content_service(content_data: dict):
    return create_about_content_from_db(content_data)


    
def update_about_content_service(content_data: dict, content_id: int):
    return update_about_content_from_db(content_data, content_id)