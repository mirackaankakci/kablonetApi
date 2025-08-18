from sqlalchemy.orm import Session
from app.crud.tariff_line_crud import (
    get_tariff_line_crud,
    get_tariff_line_by_id_crud,
    create_tariff_line_crud,
    update_tariff_line_crud,
    delete_tariff_line_crud,
)


def get_tariff_lines_service(db: Session):
    return get_tariff_line_crud(db)

def get_tariff_line_by_id_service(db: Session, tariff_line_id: int):
    return get_tariff_line_by_id_crud(db, tariff_line_id)

def create_tariff_line_service(db: Session, tariff_line_data):
    payload = tariff_line_data.dict(exclude_unset=True) if hasattr(tariff_line_data, "dict") else dict(tariff_line_data)
    payload.pop("id", None)
    return create_tariff_line_crud(db, payload)

def update_tariff_line_service(db: Session, tariff_line_id: int, tariff_line_data):
    payload = tariff_line_data.dict(exclude_unset=True) if hasattr(tariff_line_data, "dict") else dict(tariff_line_data)
    payload.pop("id", None)
    return update_tariff_line_crud(db, tariff_line_id, payload)

def delete_tariff_line_service(db: Session, tariff_line_id: int):
    return delete_tariff_line_crud(db, tariff_line_id)
