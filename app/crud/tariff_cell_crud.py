from app.db.database import SessionLocal
from app.db.models.TariffCell import TariffCell
from sqlalchemy.orm import Session, joinedload
from app.db.models.TariffLine import TariffLine
from app.db.models.TariffColumn import TariffColumn
from app.db.models.TariffValue import TariffValue
from app.db.models.TariffCategory import TariffCategory

def get_tariff_cell_crud():
    db: Session = SessionLocal()
    tariff_cells = (
        db.query(TariffCell)
        .options(
            joinedload(TariffCell.tariff_line)
            .joinedload(TariffLine.tariff_category)
            .joinedload(TariffCategory.main_category),
            joinedload(TariffCell.tariff_column),
            joinedload(TariffCell.tariff_value),
        )
        .all()
    )
    db.close()
    return tariff_cells

def get_tariff_cell_by_id_crud(tariff_cell_id: int):
    db: Session = SessionLocal()
    tariff_cell = (
        db.query(TariffCell)
        .options(
            joinedload(TariffCell.tariff_line)
            .joinedload(TariffLine.tariff_category)
            .joinedload(TariffCategory.main_category),
            joinedload(TariffCell.tariff_column),
            joinedload(TariffCell.tariff_value),
        )
        .filter(TariffCell.id == tariff_cell_id)
        .first()
    )
    db.close()
    return tariff_cell

def create_tariff_cell_crud(tariff_cell_data: dict):
    db: Session = SessionLocal()
    # Defensive copy
    data = dict(tariff_cell_data)
    data.pop("id", None)
    db_tariff_cell = TariffCell(**data)
    db.add(db_tariff_cell)
    db.commit()
    db.refresh(db_tariff_cell)
    # Re-query with relationship loaded
    result = (
        db.query(TariffCell)
        .options(
            joinedload(TariffCell.tariff_line)
            .joinedload(TariffLine.tariff_category)
            .joinedload(TariffCategory.main_category),
            joinedload(TariffCell.tariff_column),
            joinedload(TariffCell.tariff_value),
        )
        .filter(TariffCell.id == db_tariff_cell.id)
        .first()
    )
    db.close()
    return result

def update_tariff_cell_crud(tariff_cell_data: dict, tariff_cell_id: int):
    db: Session = SessionLocal()
    db_tariff_cell = db.query(TariffCell).filter(TariffCell.id == tariff_cell_id).first()
    if db_tariff_cell:
        for key, value in tariff_cell_data.items():
            if key in ("id",) or value is None:
                continue
            setattr(db_tariff_cell, key, value)
        db.commit()
        db.refresh(db_tariff_cell)
        result = (
            db.query(TariffCell)
            .options(
                joinedload(TariffCell.tariff_line)
                .joinedload(TariffLine.tariff_category)
                .joinedload(TariffCategory.main_category),
                joinedload(TariffCell.tariff_column),
                joinedload(TariffCell.tariff_value),
            )
            .filter(TariffCell.id == db_tariff_cell.id)
            .first()
        )
        db.close()
        return result
    db.close()
    return None

def delete_tariff_cell_crud(tariff_cell_id: int):
    db: Session = SessionLocal()
    db_tariff_cell = db.query(TariffCell).filter(TariffCell.id == tariff_cell_id).first()
    if db_tariff_cell:
        db.delete(db_tariff_cell)
        db.commit()
    db.close()
    return db_tariff_cell

def get_tariff_cells_by_line_and_column_crud(line_id: int, column_id: int):
    """Get tariff cells for specific line and column intersection"""
    db: Session = SessionLocal()
    try:
        cells = (
            db.query(TariffCell)
            .options(
                joinedload(TariffCell.tariff_line),
                joinedload(TariffCell.tariff_column),
                joinedload(TariffCell.tariff_value),
            )
            .filter(
                TariffCell.tariff_line_id == line_id,
                TariffCell.tariff_column_id == column_id
            )
            .all()
        )
        return cells
    finally:
        db.close()
