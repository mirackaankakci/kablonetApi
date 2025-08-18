from app.crud.tariff_category_column_crud import (
    get_tariff_category_column_from_db,
    get_category_column_by_id_from_db,
    create_category_column_from_db,
    update_category_column_from_db,
    delete_category_column_from_db,
)


def get_tariff_category_columns_services():
    return get_tariff_category_column_from_db()


def get_category_column_by_id_services(category_column_id: int):
    return get_category_column_by_id_from_db(category_column_id)


def create_category_column_services(payload):
    return create_category_column_from_db(payload)


def update_category_column_services(category_column_id: int, payload):
    return update_category_column_from_db(payload, category_column_id)


def delete_category_column_services(category_column_id: int):
    return delete_category_column_from_db(category_column_id)