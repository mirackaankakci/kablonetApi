from app.db.database import get_db
from app.db.models.about_contents import About_Contents
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_about_content_by_id_from_db(about_content_id: int, db: Session):
    about_content = db.query(About_Contents).options(
        joinedload(About_Contents.main_category)
    ).filter(About_Contents.id == about_content_id,
            About_Contents.is_active == True).first()
    
    return about_content

def create_about_content_from_db(about_content_data, db: Session):
    new_about_content = About_Contents(**about_content_data)
    db.add(new_about_content)
    db.commit()
    db.refresh(new_about_content)
    
    return new_about_content

def update_about_content_from_db(about_content_id: int, about_content_data, db: Session):
    about_content = db.query(About_Contents).filter(About_Contents.id == about_content_id).first()
    if not about_content:
        
        return None
    for key, value in about_content_data.items():
        setattr(about_content, key, value)
    db.commit()
    db.refresh(about_content)
    
    return about_content

# Get all about contents from the database
def get_all_about_contents_from_db(db: Session):
    about_contents = db.query(About_Contents).options(
        joinedload(About_Contents.main_category)
    ).filter(About_Contents.is_active == True).order_by(About_Contents.id).all()
    
    return about_contents
   

## Get all about contents by category from the database
def get_all_about_contents_by_category_from_db(main_category_id: int, db: Session):
    about_contents = db.query(About_Contents).options(
        joinedload(About_Contents.main_category)
    ).filter(About_Contents.main_category_id == main_category_id,
            About_Contents.is_active == True).order_by(About_Contents.id).all()
    
    return about_contents

def deactivate_about_content_from_db(about_content_id: int, db: Session):
    about_content = db.query(About_Contents).filter(About_Contents.id == about_content_id,
                                                    About_Contents.is_active == True).first()
    if not about_content:
        
        return None
    
    if not about_content.is_active:
        return about_content 
    
    about_content.is_active = False
    
    db.commit()
    db.refresh(about_content)
    
    return about_content