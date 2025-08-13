from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.schemas.packages_category_schemas import PackagesCategorySchemas, PackagesCategoryResponse, PackagesCategoryCreateResponse, PackagesCategoryUpdateResponse
from app.services.packages_category_services import get_packages_category_services, create_packages_category_services, update_packages_category_services, list_all_packages_category_services

router = APIRouter(prefix="/packages-category", tags=["Packages Category"])

@router.get("/", response_model=list[PackagesCategorySchemas])
def list_all_packages_category(db: Session = Depends(get_db)):
    packages_category = list_all_packages_category_services(db)
    if not packages_category:
        raise HTTPException(status_code=404, detail="No packages category found")
    return packages_category

@router.get("/{packages_category_id}", response_model=PackagesCategorySchemas)
def get_packages_category(packages_category_id: int):
    packages_category = get_packages_category_services(packages_category_id)
    if not packages_category:
        raise HTTPException(status_code=404, detail="packages category not found")
    return packages_category

@router.post("/new-packages-category", response_model=PackagesCategoryCreateResponse)
def add_packages_category(packages_category_data: PackagesCategoryCreateResponse):
    try:
        created_packages_category = create_packages_category_services(packages_category_data)
        return created_packages_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{packages_category_id}", response_model=PackagesCategoryUpdateResponse)
def update_packages_category(packages_category_data: PackagesCategoryUpdateResponse, packages_category_id: int):
    try:
        updated_packages_category = update_packages_category_services(packages_category_data, packages_category_id)
        if not updated_packages_category:
            raise HTTPException(status_code=404, detail="Device not found")
        return updated_packages_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))