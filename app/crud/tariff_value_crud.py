from app.db.database import get_db
from app.db.models.TariffValue import TariffValue
from sqlalchemy.orm import Session, joinedload, selectinload
from app.db.database import SessionLocal



def get_all_tariff_values():
    db: Session = SessionLocal()
    try:
        tariff_values = db.query(TariffValue).order_by(TariffValue.id).all()
        return tariff_values
    finally:
        db.close()


def get_tariff_value_by_id(tariff_value_id: int):
    db: Session = SessionLocal()
    try:
        tariff_value = db.query(TariffValue).filter(TariffValue.id == tariff_value_id).first()
        return tariff_value
    finally:
        db.close()


def create_tariff_value(tariff_value_data):
    db: Session = SessionLocal()
    try:
        new_tariff_value = TariffValue(**tariff_value_data.dict())
        db.add(new_tariff_value)
        db.commit()
        db.refresh(new_tariff_value)
        return new_tariff_value
    finally:
        db.close()


def update_tariff_value(tariff_value_id: int, tariff_value_data: dict):
    db: Session = SessionLocal()
    try:
        tariff_value = db.query(TariffValue).filter(TariffValue.id == tariff_value_id).first()
        if not tariff_value:
            return None
        for key, value in tariff_value_data.items():
            setattr(tariff_value, key, value)
        db.commit()
        db.refresh(tariff_value)
        return tariff_value
    finally:
        db.close()


def delete_tariff_value(tariff_value_id: int):
    db: Session = SessionLocal()
    try:
        tariff_value = db.query(TariffValue).filter(TariffValue.id == tariff_value_id).first()
        if not tariff_value:
            return None
        db.delete(tariff_value)
        db.commit()
        return tariff_value
    finally:
        db.close()