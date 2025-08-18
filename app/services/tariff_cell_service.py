from app.crud.tariff_cell_crud import (
    get_tariff_cell_crud,
    get_tariff_cell_by_id_crud,
    create_tariff_cell_crud,
    update_tariff_cell_crud,
    delete_tariff_cell_crud,
)

def get_tariff_cells_service():
    return get_tariff_cell_crud()

def get_tariff_cell_by_id_service(tariff_cell_id: int):
    return get_tariff_cell_by_id_crud(tariff_cell_id)

def create_tariff_cell_service(tariff_cell_data):
    return create_tariff_cell_crud(tariff_cell_data)

def update_tariff_cell_service(tariff_cell_id: int, tariff_cell_data):
    return update_tariff_cell_crud(tariff_cell_data, tariff_cell_id)

def delete_tariff_cell_service(tariff_cell_id: int):
    return delete_tariff_cell_crud(tariff_cell_id)