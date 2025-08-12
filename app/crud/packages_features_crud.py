from app.db.database import get_db
from app.db.models.packages_features import PackagesFeatures
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_packages_features_by_id_from_db(packages_features_id: int):
    packages_features = db.query(PackagesFeatures).options(
        joinedload(PackagesFeatures.packages)
    ).filter(PackagesFeatures.id == packages_features_id).first()
    db.close()
    return packages_features

def create_packages_features_from_db(packages_features_data):
    new_packages_features =PackagesFeatures(**packages_features_data.dict())
    db.add(new_packages_features)
    db.commit()
    db.refresh(new_packages_features)
    db.close()
    return new_packages_features

def update_packages_features_from_db(packages_features_id: int, packages_features_data):
    packages_features= db.query(PackagesFeatures).filter(PackagesFeatures.id == packages_features_id).first()
    if not packages_features:
        db.close()
        return None
    for key, value in packages_features_data.dict().items():
        setattr(packages_features, key, value)
    db.commit()
    db.refresh(packages_features)
    db.close()
    return packages_features

def list_all_packages_features_from_db(db: Session):
    packages_features = db.query(PackagesFeatures).options(
        joinedload(PackagesFeatures.packages)
    ).order_by(PackagesFeatures.id).all()
    db.close()
    return packages_features