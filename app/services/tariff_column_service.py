from app.crud.tariff_column_crud import (
    get_all_tariff_columns_crud,
    get_tariff_column_by_id_crud,
    create_tariff_column_crud,
    update_tariff_column_crud,
    delete_tariff_column_crud
)

def get_tariff_columns_service():
    return get_all_tariff_columns_crud()



def get_tariff_column_by_id_service(tariff_column_id: int):
    return get_tariff_column_by_id_crud(tariff_column_id)



def create_tariff_column_service(tariff_column_data):
    return create_tariff_column_crud(tariff_column_data)


def update_tariff_column_service(tariff_column_data, tariff_column_id: int):
    return update_tariff_column_crud(tariff_column_data, tariff_column_id)


def delete_tariff_column_service(tariff_column_id: int):
    return delete_tariff_column_crud(tariff_column_id)  