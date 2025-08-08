from app.db.database import get_db
from app.db.models.TariffCategory import TariffCategory
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal




def get_tarfiff_categories_from_db():
    db: Session = SessionLocal()
    tariff_categories = db.query(TariffCategory).options(joinedload(TariffCategory.main_category)).all()
    db.close()
    return tariff_categories

def get_main_tariff_category_by_id_from_db(tariff_category_id: int):
    db: Session = SessionLocal()
    tariff_category = db.query(TariffCategory).options(joinedload(TariffCategory.main_category)).filter(TariffCategory.id == tariff_category_id).first()
    db.close()
    return tariff_category

def create_tariff_category_in_db(tariff_category_data):
    db: Session = SessionLocal()
    new_tariff_category = TariffCategory(**tariff_category_data.dict())
    db.add(new_tariff_category)
    db.commit()
    db.refresh(new_tariff_category)

    # İlişkiyi güvenli şekilde eager load ederek yeniden çek
    tc = (
        db.query(TariffCategory)
        .options(joinedload(TariffCategory.main_category))
        .filter(TariffCategory.id == new_tariff_category.id)
        .first()
    )
    db.close()
    return tc
