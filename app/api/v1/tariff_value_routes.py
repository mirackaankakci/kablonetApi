from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_value_service import (
    get_tariff_values_service,
    get_tariff_value_by_id_service,
    create_tariff_value_service,
    update_tariff_value_service,
    delete_tariff_value_service
)
from app.schemas.tariff_value_schema import (
    TariffValueResponse,
    TariffValueCreateRequest,
    TariffValueDeleteRequest,
    TariffValueUpdateRequest
)



router = APIRouter(prefix="/tariff-values", tags=["Tariff Values"])

@router.get("/", response_model=list[TariffValueResponse])
def read_tariff_values():
    return get_tariff_values_service()


@router.get("/{tariff_value_id}", response_model=TariffValueResponse)
def read_tariff_value(tariff_value_id: int):
    db_tariff_value = get_tariff_value_by_id_service(tariff_value_id)
    if not db_tariff_value:
        raise HTTPException(status_code=404, detail="Tariff Value not found")
    return db_tariff_value

@router.post("/", response_model=TariffValueResponse)
def create_tariff_value(tariff_value: TariffValueCreateRequest):
    db_tariff_value = create_tariff_value_service(tariff_value)
    if not db_tariff_value:
        raise HTTPException(status_code=400, detail="Error creating Tariff Value")
    return db_tariff_value

@router.put("/{tariff_value_id}", response_model=TariffValueResponse)
def update_tariff_value(tariff_value_id: int, tariff_value: TariffValueUpdateRequest):
    db_tariff_value = update_tariff_value_service(tariff_value_id, tariff_value)
    if not db_tariff_value:
        raise HTTPException(status_code=404, detail="Tariff Value not found")
    return db_tariff_value

@router.delete("/{tariff_value_id}", response_model=TariffValueDeleteRequest)
def delete_tariff_value(tariff_value_id: int):
    db_tariff_value = delete_tariff_value_service(tariff_value_id)
    if not db_tariff_value:
        raise HTTPException(status_code=404, detail="Tariff Value not found")
    return db_tariff_value
