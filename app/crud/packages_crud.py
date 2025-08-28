from app.db.database import get_db
from app.db.models.packages import Packages
from app.db.models.packages_category import PackagesCategory
from app.db.models.MainCategory import MainCategory
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_packages_by_id_from_db(packages_id: int, db: Session):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).filter(Packages.id == packages_id, Packages.is_active == True).first()
    #
    return packages

def create_packages_from_db(packages_data, db: Session):
    new_packages = Packages(**packages_data)
    db.add(new_packages)
    db.commit()
    db.refresh(new_packages)
    #
    return new_packages

def update_packages_from_db(packages_id: int, packages_data, db: Session):
    packages = db.query(Packages).filter(Packages.id == packages_id).first()
    if not packages:
        #
        return None
    for key, value in packages_data.items():
        setattr(packages, key, value)
    db.commit()
    db.refresh(packages)
    #
    return packages

def list_all_packages_from_db(db: Session):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).filter(Packages.is_active == True).order_by(Packages.id).all()
    #
    return packages

# def get_packages_by_main_category_id_from_db(main_category_id: int):
#     packages = db.query(Packages).options(
#         joinedload(Packages.main_category),
#         joinedload(Packages.packages_category)
#     ).filter(Packages.main_category_id == main_category_id).first()
#     #
#     return packages

def get_packages_by_category_id_from_db(packages_category_id: int, db: Session):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).filter(Packages.packages_category_id == packages_category_id,
            Packages.is_active == True).order_by(Packages.id).all()
    #
    return packages

def deactivate_packages_from_db(packages_id: int, db: Session):
    packages = db.query(Packages).filter(Packages.id == packages_id,
                                        Packages.is_active == True).first()
    if not packages:
        #
        return None
    
    if not packages.is_active:
        return packages 
    
    packages.is_active = False
    
    db.commit()
    db.refresh(packages)
    #
    return packages
