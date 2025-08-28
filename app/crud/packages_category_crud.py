from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.packages_category import PackagesCategory

db: Session = SessionLocal()

def get_packages_category_by_id_from_db(packages_category_id: int, db: Session):
    packages_category= db.query(PackagesCategory).filter(PackagesCategory.id == packages_category_id,
                                                        PackagesCategory.is_active == True).first()
    #
    return packages_category

def create_packages_category_from_db(packages_category_data, db: Session):
    new_packages_category = PackagesCategory(**packages_category_data)
    db.add(new_packages_category)
    db.commit()
    db.refresh(new_packages_category)
    #
    return new_packages_category

def update_packages_category_in_db(packages_category_data, packages_category_id: int, db: Session):
    packages_category = db.query(PackagesCategory).filter(PackagesCategory.id == packages_category_id).first()
    if not packages_category:
        #
        return None
    for key, value in packages_category_data.items():
        setattr(packages_category, key, value)
    db.commit()
    db.refresh(packages_category)
    #
    return packages_category

def list_all_packages_category_from_db(db: Session):
    packages_categories = db.query(PackagesCategory).filter(PackagesCategory.is_active == True).order_by(PackagesCategory.id).all()
    #
    return packages_categories

def deactivate_packages_category_from_db(packages_category_id: int, db: Session):
    packages_category = db.query(PackagesCategory).filter(PackagesCategory.id == packages_category_id,
                                                    PackagesCategory.is_active == True).first()
    if not packages_category:
        #
        return None
    
    if not packages_category.is_active:
        return packages_category 
    
    packages_category.is_active = False
    
    db.commit()
    db.refresh(packages_category)
    #
    return packages_category