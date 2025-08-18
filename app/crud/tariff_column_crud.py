from app.db.database import get_db
from app.db.models.TariffColumn import TariffColumn
from sqlalchemy.orm import Session, joinedload, selectinload
from app.db.database import SessionLocal



def get_all_tariff_columns_crud():
    db: Session = SessionLocal()
    try:
        tariff_columns = db.query(TariffColumn).order_by(TariffColumn.id).all()
        return tariff_columns
    finally:
        db.close()


def get_tariff_column_by_id_crud(tariff_column_id: int):
    db: Session = SessionLocal()
    try:
        tariff_column = db.query(TariffColumn).filter(TariffColumn.id == tariff_column_id).first()
        return tariff_column
    finally:
        db.close()


def create_tariff_column_crud(tariff_column_data):
    db: Session = SessionLocal()
    try:
        tariff_column = TariffColumn(**tariff_column_data.dict())
        db.add(tariff_column)
        db.commit()
        db.refresh(tariff_column)
        return tariff_column
    finally:
        db.close()

def update_tariff_column_crud(tariff_column_data: dict, tariff_column_id: int):
    db: Session = SessionLocal()
    try:
        tariff_column = db.query(TariffColumn).filter(TariffColumn.id == tariff_column_id).first()
        if tariff_column:
            for key, value in tariff_column_data.items():
                setattr(tariff_column, key, value)
            db.commit()
            db.refresh(tariff_column)
            return tariff_column
        return None
    finally:
        db.close()

def delete_tariff_column_crud(tariff_column_id: int):
    db: Session = SessionLocal()
    try:
        tariff_column = db.query(TariffColumn).filter(TariffColumn.id == tariff_column_id).first()
        if tariff_column:
            db.delete(tariff_column)
            db.commit()
            return True
        return False
    finally:
        db.close()
        