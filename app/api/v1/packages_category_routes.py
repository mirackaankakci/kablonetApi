from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.packages_category_schemas import PackagesCategorySchemas, PackagesCategoryResponse, PackagesCategoryCreateResponse, PackagesCategoryUpdateResponse, DeletePackagesCategoryResponse
from app.services.packages_category_services import get_packages_category_services, create_packages_category_services, update_packages_category_services, list_all_packages_category_services, deactivate_packages_category_services

router = APIRouter(prefix="/packages-category", tags=["Packages Category"])

@router.get("/", response_model=list[PackagesCategorySchemas])
def list_all_packages_category(db: Session = Depends(get_db)):
    packages_category = list_all_packages_category_services(db)
    return packages_category

@router.get("/{packages_category_id}", response_model=PackagesCategorySchemas)
def get_packages_category(packages_category_id: int, db: Session = Depends(get_db)):
    packages_category = get_packages_category_services(packages_category_id, db)
    return packages_category

@router.post("/new-packages-category", response_model=PackagesCategoryCreateResponse)
def add_packages_category(packages_category_data: PackagesCategoryCreateResponse, db: Session = Depends(get_db)):
    created_packages_category = create_packages_category_services(packages_category_data, db)
    return created_packages_category

@router.put("/{packages_category_id}", response_model=PackagesCategoryUpdateResponse)
def update_packages_category(packages_category_data: PackagesCategoryUpdateResponse, packages_category_id: int, db: Session = Depends(get_db)):
    updated_packages_category = update_packages_category_services(packages_category_data, packages_category_id, db)
    return updated_packages_category

@router.delete("/{packages_category_id}", response_model= DeletePackagesCategoryResponse)
def deactivate_packages_category(packages_category_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_packages_category_services(packages_category_id, db)
    return deactivate