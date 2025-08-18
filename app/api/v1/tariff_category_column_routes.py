from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_category_column_services import (
    get_tariff_category_columns_services,
    get_category_column_by_id_services,
    create_category_column_services,
    update_category_column_services,
    delete_category_column_services
)

from app.schemas.tariff_category_column_schema import (
    TariffCategoryColumnCreateRequest,
    TariffCategoryColumnUpdateRequest,
    TariffCategoryColumnResponse
)



router = APIRouter(prefix="/tariff-category-columns", tags=["Tariff Category Columns"])


@router.get("/", response_model=list[TariffCategoryColumnResponse])
def read_tariff_category_columns():
    return get_tariff_category_columns_services()


@router.get("/{category_column_id}", response_model=TariffCategoryColumnResponse)
def read_category_column_by_id(category_column_id: int):
    db_category_column = get_category_column_by_id_services(category_column_id)
    if not db_category_column:
        raise HTTPException(status_code=404, detail="Category column not found")
    return db_category_column

@router.post("/", response_model=TariffCategoryColumnResponse)
def create_category_column(category_column: TariffCategoryColumnCreateRequest):
    db_category_column = create_category_column_services(category_column)
    if not db_category_column:
        raise HTTPException(status_code=400, detail="Category column could not be created")
    return db_category_column

@router.put("/{category_column_id}", response_model=TariffCategoryColumnResponse)
def update_category_column(category_column_id: int, category_column: TariffCategoryColumnUpdateRequest):
    db_category_column = update_category_column_services(category_column_id, category_column)
    if not db_category_column:
        raise HTTPException(status_code=404, detail="Category column not found")
    return db_category_column

@router.delete("/{category_column_id}", response_model=TariffCategoryColumnResponse)
def delete_category_column(category_column_id: int):
    db_category_column = delete_category_column_services(category_column_id)
    if not db_category_column:
        raise HTTPException(status_code=404, detail="Category column not found")
    return db_category_column