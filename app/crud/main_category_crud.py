from app.db.database import get_db
from app.db.models.MainCategory import MainCategory
from sqlalchemy.orm import Session
from app.db.database import SessionLocal


def get_main_category_by_id_from_db(main_category_id: int):
    db: Session = SessionLocal()
    main_category = db.query(MainCategory).filter(MainCategory.id == main_category_id).first()
    db.close()
    return main_category

def create_main_category_from_db(main_category_data):
    db: Session = SessionLocal()
    new_main_category = MainCategory(**main_category_data.dict())
    db.add(new_main_category)
    db.commit()
    db.refresh(new_main_category)
    db.close()
    return MainCategory.new_main_category
