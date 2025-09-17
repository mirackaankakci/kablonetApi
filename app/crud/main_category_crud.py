from app.db.database import get_db
from app.db.models.MainCategory import MainCategory
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.db.database import SessionLocal


def get_all_main_categories_from_db(db: Session):
    main_categories = db.query(MainCategory).filter(MainCategory.is_active == True).order_by(MainCategory.id).all()
    #
    return main_categories

def get_main_category_by_id_from_db(main_category_id: int, db: Session):
    db: Session = SessionLocal()
    main_category = db.query(MainCategory).filter(MainCategory.id == main_category_id,
                                                MainCategory.is_active == True).first()
    #
    return main_category

def create_main_category_from_db(main_category_data, db: Session):
    db: Session = SessionLocal()
    new_main_category = MainCategory(**main_category_data)
    try:
        db.add(new_main_category)
        db.commit()
        db.refresh(new_main_category)
        #
        return new_main_category
    except IntegrityError as e:
        db.rollback()
        if 'idx_unique_active_main_category_name' in str(e):
            raise HTTPException(400, detail="Bu kategori ismi zaten kullanılıyor.")
        else:
            raise HTTPException(400, detail="Benzersizlik hatası.")



def update_main_category_in_db(main_category_data, main_category_id: int, db: Session):
    db: Session = SessionLocal()
    main_category = db.query(MainCategory).filter(MainCategory.id == main_category_id).first()
    
    try:
        if not main_category:
            #
            return None
        for key, value in main_category_data.items():
            setattr(main_category, key, value)
        db.commit()
        db.refresh(main_category)
        #
        return main_category
    except IntegrityError as e:
        db.rollback()
        if 'idx_unique_active_main_category_name' in str(e):
            raise HTTPException(400, detail="Bu kategori ismi zaten kullanılıyor.")
        else:
            raise HTTPException(400, detail="Benzersizlik hatası.")
        

def deactivate_main_category_from_db(main_category_id: int, db: Session):
    main_category = db.query(MainCategory).filter(MainCategory.id == main_category_id,
                                                    MainCategory.is_active == True).first()
    if not main_category:
        #
        return None
    
    if not main_category.is_active:
        return main_category 
    
    main_category.is_active = False
    
    db.commit()
    db.refresh(main_category)
    #
    return main_category