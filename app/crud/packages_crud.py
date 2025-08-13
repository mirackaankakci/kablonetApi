from app.db.database import get_db
from app.db.models.packages import Packages
from app.db.models.packages_category import PackagesCategory
from app.db.models.MainCategory import MainCategory
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_packages_by_id_from_db(packages_id: int):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).filter(Packages.id == packages_id).first()
    db.close()
    return packages

def create_packages_from_db(packages_data):
    new_packages = Packages(**packages_data.dict())
    db.add(new_packages)
    db.commit()
    db.refresh(new_packages)
    db.close()
    return new_packages

def update_packages_from_db(packages_id: int, packages_data):
    packages = db.query(Packages).filter(Packages.id == packages_id).first()
    if not packages:
        db.close()
        return None
    for key, value in packages_data.dict().items():
        setattr(packages, key, value)
    db.commit()
    db.refresh(packages)
    db.close()
    return packages

def list_all_packages_from_db(db: Session):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).order_by(Packages.id).all()
    db.close()
    return packages

# def get_packages_by_main_category_id_from_db(main_category_id: int):
#     packages = db.query(Packages).options(
#         joinedload(Packages.main_category),
#         joinedload(Packages.packages_category)
#     ).filter(Packages.main_category_id == main_category_id).first()
#     db.close()
#     return packages

def get_packages_by_category_id_from_db(packages_category_id: int):
    packages = db.query(Packages).options(
        joinedload(Packages.main_category),
        joinedload(Packages.packages_category)
    ).filter(Packages.packages_category_id == packages_category_id).order_by(Packages.id).all()
    db.close()
    return packages

