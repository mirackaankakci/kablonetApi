from app.crud.tariff_value_crud import (
    get_all_tariff_values,
    get_tariff_value_by_id,
    create_tariff_value,
    update_tariff_value,
    delete_tariff_value
)


def get_tariff_values_service():
    return get_all_tariff_values()


def get_tariff_value_by_id_service(tariff_value_id: int):
    return get_tariff_value_by_id(tariff_value_id)


def create_tariff_value_service(tariff_value_data):
    return create_tariff_value(tariff_value_data)


def update_tariff_value_service(tariff_value_id: int, tariff_value_data):
    return update_tariff_value(tariff_value_id, tariff_value_data)


def delete_tariff_value_service(tariff_value_id: int):
    return delete_tariff_value(tariff_value_id)
