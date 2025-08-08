from app.crud.tariff_category_crud import get_main_tariff_category_by_id_from_db, create_tariff_category_in_db, get_tarfiff_categories_from_db


def get_tariff_categories_service():
    return get_tarfiff_categories_from_db()


def get_main_tariff_category_by_id(tariff_category_id: int):
    return get_main_tariff_category_by_id_from_db(tariff_category_id)

def create_tariff_category_service(tariff_category_data: dict):
    return create_tariff_category_in_db(tariff_category_data)