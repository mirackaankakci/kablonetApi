from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.packages_schemas import PackagesSchemas, PackagesResponse, PackagesCreateSchemas, PackagesUpdateSchemas, DeletePackagesSchemas
from app.services.packages_services import get_packages_services, create_packages_services, update_packages_services, list_all_packages_services, get_packages_by_category_services, deactivate_packages_services

router = APIRouter(prefix="/packages", tags=["Packages"])

@router.get("/", response_model=list[PackagesSchemas])
def list_all_packages(db: Session = Depends(get_db)):
    packages = list_all_packages_services(db)
    return packages

@router.get("/packages_category ", response_model=list[PackagesSchemas])
def list_all_packages_category(packages_category_id: int, db: Session = Depends(get_db)):
    device_commitments = get_packages_by_category_services(packages_category_id, db)
    return device_commitments

@router.get("/{packages_id}", response_model=PackagesSchemas)
def get_packages(packages_id: int, db: Session = Depends(get_db)):
    packages = get_packages_services(packages_id, db)
    return packages

@router.post("/new-package", response_model=PackagesCreateSchemas)
def add_packages(packages_data: PackagesCreateSchemas, db: Session = Depends(get_db)):
    created_package = create_packages_services(packages_data, db)
    return created_package
    
@router.put("/{packages_id}", response_model=PackagesUpdateSchemas)
def update_packages(packages_id: int, packages_data: PackagesUpdateSchemas, db: Session = Depends(get_db)):
    updated_packages = update_packages_services(packages_id, packages_data, db)
    return updated_packages

@router.delete("/{packages_id}", response_model= DeletePackagesSchemas)
def deactivate_packages(packages_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_packages_services(packages_id, db)
    return deactivate