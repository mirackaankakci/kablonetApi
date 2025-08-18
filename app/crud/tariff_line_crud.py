from sqlalchemy.orm import Session, joinedload
from app.db.models.TariffLine import TariffLine
from app.db.models.TariffCategory import TariffCategory

_EAGER = joinedload(TariffLine.tariff_category).joinedload(TariffCategory.main_category)

def get_tariff_line_crud(db: Session):
    return db.query(TariffLine).options(_EAGER).order_by(TariffLine.id).all()

def get_tariff_line_by_id_crud(db: Session, tariff_line_id: int):
    return (
        db.query(TariffLine)
        .options(_EAGER)
        .filter(TariffLine.id == tariff_line_id)
        .first()
    )

def create_tariff_line_crud(db: Session, tariff_line_data: dict):
    data = dict(tariff_line_data)
    data.pop("id", None)
    obj = TariffLine(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return get_tariff_line_by_id_crud(db, obj.id)

def update_tariff_line_crud(db: Session, tariff_line_id: int, tariff_line_data: dict):
    obj = db.query(TariffLine).filter(TariffLine.id == tariff_line_id).first()
    if not obj:
        return None
    for key, value in tariff_line_data.items():
        if key == "id" or value is None:
            continue
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return get_tariff_line_by_id_crud(db, obj.id)

def delete_tariff_line_crud(db: Session, tariff_line_id: int):
    obj = db.query(TariffLine).filter(TariffLine.id == tariff_line_id).first()
    if not obj:
        return None
    db.delete(obj)
    db.commit()
    return obj

def get_tariff_lines_by_category_id_crud(category_id: int):
    """Get all tariff lines for a specific category"""
    from app.db.database import SessionLocal
    db = SessionLocal()
    try:
        lines = (
            db.query(TariffLine)
            .options(_EAGER)
            .filter(TariffLine.tariff_category_id == category_id)
            .order_by(TariffLine.id)
            .all()
        )
        return lines
    finally:
        db.close()
