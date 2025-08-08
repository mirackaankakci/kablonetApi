from app.db.database import get_db
from app.db.models.about_contents import About_Contents
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_about_content_by_id_from_db(about_content_id: int):
    about_content = db.query(About_Contents).options(
        joinedload(About_Contents.main_category)
    ).filter(About_Contents.id == about_content_id).first()
    db.close()
    return about_content

def create_about_content_from_db(about_content_data):
    new_about_content = About_Contents(**about_content_data.dict())
    db.add(new_about_content)
    db.commit()
    db.refresh(new_about_content)
    db.close()
    return new_about_content

def update_about_content_from_db(about_content_id: int, about_content_data):
    about_content = db.query(About_Contents).filter(About_Contents.id == about_content_id).first()
    if not about_content:
        db.close()
        return None
    for key, value in about_content_data.dict().items():
        setattr(about_content, key, value)
    db.commit()
    db.refresh(about_content)
    db.close()
    return about_content