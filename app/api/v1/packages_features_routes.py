from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.packages_features_services import get_packages_features_services, create_packages_features_services, update_packages_features_services, list_all_packages_features_services,get_packages_features_by_packages_services
from app.schemas.packages_features_schemas import PackagesFeaturesSchemas, PackagesFeaturesResponse, PackagesFeaturesCreateSchemas, PackagesFeaturesUpdateSchemas

router = APIRouter(prefix="/packages-features", tags=["Packages Features"])

@router.get("/", response_model=list[PackagesFeaturesSchemas])
def list_all_packages_features(db: Session = Depends(get_db)):
    packages_features = list_all_packages_features_services(db)
    if not packages_features:
        raise HTTPException(status_code=404, detail="No packages features found")
    return packages_features

@router.get("/packages", response_model=list[PackagesFeaturesSchemas])
def get_packages_features_by_packages(packages_id: int, db: Session = Depends(get_db)):
    packages_features = get_packages_features_by_packages_services(db, packages_id)
    if not packages_features:
        raise HTTPException(status_code=404, detail="No Packages Features found for this Packages")
    return packages_features

@router.get("/{packages_features_id}", response_model=PackagesFeaturesSchemas)
def get_packages_features(packages_features_id: int, db: Session = Depends(get_db)):
    packages_features= get_packages_features_services(db, packages_features_id)
    if not packages_features:
        raise HTTPException(status_code=404, detail="packages features not found")
    return packages_features

@router.post("/new-packages-features", response_model=PackagesFeaturesCreateSchemas)
def add_packages_features(packages_features_data: PackagesFeaturesCreateSchemas, db: Session = Depends(get_db)):
    try:
        created_packages_features = create_packages_features_services(db, packages_features_data)
        return created_packages_features
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{packages_features_id}", response_model=PackagesFeaturesUpdateSchemas)
def update_packages_features(packages_features_id: int, packages_features_data: PackagesFeaturesUpdateSchemas, db: Session = Depends(get_db)):
    try:
        updated_packages_features = update_packages_features_services(db, packages_features_id, packages_features_data)
        if not updated_packages_features:
            raise HTTPException(status_code=404, detail="packages_features not found")
        return updated_packages_features
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))