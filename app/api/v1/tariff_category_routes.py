from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_category_service import get_main_tariff_category_by_id, create_tariff_category_service, get_tariff_categories_service
from app.schemas.tariff_category_schema import TariffCategoryCreatedResponse, TariffCategoryResponse


router = APIRouter(prefix="/tariff-categories", tags=["Tariff Categories"])

@router.get("/", response_model=list[TariffCategoryResponse])
def read_tariff_categories():
    return get_tariff_categories_service()

@router.get("/{tariff_category_id}", response_model=TariffCategoryResponse)
def read_tariff_category(tariff_category_id: int):
    db_tariff_category = get_main_tariff_category_by_id(tariff_category_id)
    if not db_tariff_category:
        raise HTTPException(status_code=404, detail="Tariff category not found")
    return db_tariff_category

@router.post("/", response_model=TariffCategoryResponse)
def create_tariff_category(tariff_category: TariffCategoryCreatedResponse):
    db_tariff_category = create_tariff_category_service(tariff_category)
    if not db_tariff_category:
        raise HTTPException(status_code=400, detail="Error creating tariff category")
    return db_tariff_category
