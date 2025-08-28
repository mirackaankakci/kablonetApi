from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.packages_features_services import get_packages_features_services, create_packages_features_services, update_packages_features_services, list_all_packages_features_services,get_packages_features_by_packages_services, deactivate_packages_features_services
from app.schemas.packages_features_schemas import PackagesFeaturesSchemas, PackagesFeaturesResponse, PackagesFeaturesCreateSchemas, PackagesFeaturesUpdateSchemas, DeletePackagesFeaturesSchemas

router = APIRouter(prefix="/packages-features", tags=["Packages Features"])

@router.get("/", response_model=list[PackagesFeaturesSchemas])
def list_all_packages_features(db: Session = Depends(get_db)):
    packages_features = list_all_packages_features_services(db)
    return packages_features

@router.get("/packages", response_model=list[PackagesFeaturesSchemas])
def get_packages_features_by_packages(packages_id: int, db: Session = Depends(get_db)):
    packages_features = get_packages_features_by_packages_services(packages_id, db)
    return packages_features

@router.get("/{packages_features_id}", response_model=PackagesFeaturesSchemas)
def get_packages_features(packages_features_id: int, db: Session = Depends(get_db)):
    packages_features= get_packages_features_services(packages_features_id, db)
    return packages_features

@router.post("/new-packages-features", response_model=PackagesFeaturesCreateSchemas)
def add_packages_features(packages_features_data: PackagesFeaturesCreateSchemas, db: Session = Depends(get_db)):
    created_packages_features = create_packages_features_services(packages_features_data, db)
    return created_packages_features

@router.put("/{packages_features_id}", response_model=PackagesFeaturesUpdateSchemas)
def update_packages_features(packages_features_id: int, packages_features_data: PackagesFeaturesUpdateSchemas, db: Session = Depends(get_db)):
    updated_packages_features = update_packages_features_services(packages_features_id, packages_features_data, db)
    return updated_packages_features

@router.delete("/{packages_features_id}", response_model= DeletePackagesFeaturesSchemas)
def deactivate_packages_features(packages_features_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_packages_features_services(packages_features_id, db)
    return deactivate
