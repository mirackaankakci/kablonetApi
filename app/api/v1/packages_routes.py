from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.packages_schemas import PackagesSchemas, PackagesResponse, PackagesCreateSchemas, PackagesUpdateSchemas 
from app.services.packages_services import get_packages_services, create_packages_services, update_packages_services, list_all_packages_services, get_packages_by_category_services

router = APIRouter(prefix="/packages", tags=["Packages"])

@router.get("/", response_model=list[PackagesSchemas])
def list_all_packages(db: Session = Depends(get_db)):
    packages = list_all_packages_services(db)
    if not packages:
        raise HTTPException(status_code=404, detail="No packages found")
    return packages

@router.get("/packages_category ", response_model=list[PackagesSchemas])
def list_all_packages_category(packages_category_id: int, db: Session = Depends(get_db)):
    device_commitments = get_packages_by_category_services(packages_category_id)
    if not device_commitments:
        raise HTTPException(status_code=404, detail="No Packages found for this category")
    return device_commitments

@router.get("/{packages_id}", response_model=PackagesSchemas)
def get_packages(packages_id: int):
    packages = get_packages_services(packages_id)
    if not packages:
        raise HTTPException(status_code=404, detail="No packages found")
    return packages

@router.post("/new-package", response_model=PackagesCreateSchemas)
def add_packages(packages_data: PackagesCreateSchemas):
    try:
        created_package = create_packages_services(packages_data)
        return created_package
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{packages_id}", response_model=PackagesUpdateSchemas)
def update_packages(packages_id: int, packages_data: PackagesUpdateSchemas):
    try:
        updated_packages = update_packages_services(packages_id, packages_data)
        if not updated_packages:
            raise HTTPException(status_code=404, detail="packages not found")
        return updated_packages
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))