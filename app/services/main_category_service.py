from app.crud.main_category_crud import get_main_category_by_id_from_db, create_main_category_from_db, update_main_category_in_db

def get_main_category_by_id(main_category_id: int):
    return get_main_category_by_id_from_db(main_category_id)

def create_main_category_service(main_category_data: dict):
    return create_main_category_from_db(main_category_data)


def update_main_category_service(main_category_data: dict, main_category_id: int):
    updated_category = update_main_category_in_db(main_category_data, main_category_id)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Ana kategori bulunamadı")
    return updated_category