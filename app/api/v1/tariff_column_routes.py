from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_column_service import (
    get_tariff_columns_service,
    get_tariff_column_by_id_service,
    create_tariff_column_service,
    update_tariff_column_service,
    delete_tariff_column_service
    
)
from app.schemas.tariff_column_schema import (
  TariffColumnCreateRequest,
  TariffColumnResponse,
  TariffColumnUpdateRequest,
  TariffColumnDeleteRequest
)



router = APIRouter(prefix="/tariff-columns", tags=["Tariff Columns"])

@router.get("/", response_model=list[TariffColumnResponse])
def read_tariff_columns():
    return get_tariff_columns_service()

@router.get("/{tariff_column_id}", response_model=TariffColumnResponse)
def read_tariff_column_by_id(tariff_column_id: int):
    db_tariff_column = get_tariff_column_by_id_service(tariff_column_id)
    if not db_tariff_column:
        raise HTTPException(status_code=404, detail="Tariff column not found")
    return db_tariff_column

@router.post("/", response_model=TariffColumnResponse)
def create_tariff_column(tariff_column: TariffColumnCreateRequest):
    db_tariff_column = create_tariff_column_service(tariff_column)
    if not db_tariff_column:
        raise HTTPException(status_code=400, detail="Failed to create tariff column")
    return db_tariff_column

@router.put("/{tariff_column_id}", response_model=TariffColumnResponse)
def update_tariff_column(tariff_column_id: int, tariff_column: TariffColumnUpdateRequest):
    db_tariff_column = update_tariff_column_service(tariff_column_id, tariff_column)
    if not db_tariff_column:
        raise HTTPException(status_code=404, detail="Tariff column not found")
    return db_tariff_column

@router.delete("/{tariff_column_id}", response_model=TariffColumnDeleteRequest)
def delete_tariff_column(tariff_column_id: int):
    db_tariff_column = delete_tariff_column_service(tariff_column_id)
    if not db_tariff_column:
        raise HTTPException(status_code=404, detail="Tariff column not found")
    return TariffColumnDeleteRequest(id=tariff_column_id)