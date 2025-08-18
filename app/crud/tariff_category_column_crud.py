from app.db.models.TariffCategoryColumn import TariffCategoryColumn
from app.db.models.TariffCategory import TariffCategory
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal


def _with_rels(query):
    return query.options(
        joinedload(TariffCategoryColumn.tariff_category).joinedload(TariffCategory.main_category),
        joinedload(TariffCategoryColumn.tariff_column),
    )


def get_tariff_category_column_from_db():
    db: Session = SessionLocal()
    try:
        return _with_rels(db.query(TariffCategoryColumn)).all()
    finally:
        db.close()


def get_category_column_by_id_from_db(category_column_id: int):
    db: Session = SessionLocal()
    try:
        return (
            _with_rels(db.query(TariffCategoryColumn))
            .filter(TariffCategoryColumn.id == category_column_id)
            .first()
        )
    finally:
        db.close()


def create_category_column_from_db(payload):
    """Accepts dict or Pydantic model with tariff_category_id -> category_id mapping."""
    if hasattr(payload, "model_dump"):
        data = payload.model_dump(exclude_unset=True)
    elif isinstance(payload, dict):
        data = payload.copy()
    else:
        # Assume already an ORM instance
        data = None
    db: Session = SessionLocal()
    try:
        if data is not None:
            # Map incoming keys to model column names
            mapped = {
                "category_id": data.get("tariff_category_id"),
                "tariff_column_id": data.get("tariff_column_id"),

                "is_active": data.get("is_active", True),
                "add_date": data.get("add_date"),
            }
            category_column = TariffCategoryColumn(**mapped)
        else:
            category_column = payload  # already ORM
        db.add(category_column)
        db.commit()
        db.refresh(category_column)
        # Re-query with relationships for response
        return (
            _with_rels(db.query(TariffCategoryColumn))
            .filter(TariffCategoryColumn.id == category_column.id)
            .first()
        )
    finally:
        db.close()


def update_category_column_from_db(payload, category_column_id: int):
    if hasattr(payload, "model_dump"):
        data = payload.model_dump(exclude_unset=True)
    else:
        data = payload if isinstance(payload, dict) else {}
    db: Session = SessionLocal()
    try:
        db_obj = db.query(TariffCategoryColumn).filter(TariffCategoryColumn.id == category_column_id).first()
        if not db_obj:
            return None
        # Map and apply only provided fields
        if "tariff_category_id" in data and data["tariff_category_id"] is not None:
            db_obj.category_id = data["tariff_category_id"]
        if "tariff_column_id" in data and data["tariff_column_id"] is not None:
            db_obj.tariff_column_id = data["tariff_column_id"]
        if "is_active" in data and data["is_active"] is not None:
            db_obj.is_active = data["is_active"]
        if "update_date" in data:
            db_obj.update_date = data["update_date"]
        db.commit()
        db.refresh(db_obj)
        return (
            _with_rels(db.query(TariffCategoryColumn))
            .filter(TariffCategoryColumn.id == db_obj.id)
            .first()
        )
    finally:
        db.close()


def delete_category_column_from_db(category_column_id: int):
    db: Session = SessionLocal()
    try:
        db_category_column = db.query(TariffCategoryColumn).filter(TariffCategoryColumn.id == category_column_id).first()
        if db_category_column:
            db.delete(db_category_column)
            db.commit()
        return db_category_column
    finally:
        db.close()