from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_cell_service import (
    get_tariff_cells_service,
    get_tariff_cell_by_id_service,
    create_tariff_cell_service,
    update_tariff_cell_service,
    delete_tariff_cell_service,
)
from app.schemas.tariff_cell_schema import (
    TariffCellResponse,
    TariffCellCreate,
    TariffCellUpdate,
    TariffCellDelete
)

router = APIRouter(prefix="/tariff-cells", tags=["Tariff Cells"])

@router.get("/", response_model=list[TariffCellResponse])
def get_tariff_cells():
    return get_tariff_cells_service()

@router.get("/{tariff_cell_id}", response_model=TariffCellResponse)
def get_tariff_cell(tariff_cell_id: int):
    tariff_cell = get_tariff_cell_by_id_service(tariff_cell_id)
    if not tariff_cell:
        raise HTTPException(status_code=404, detail="Tariff cell not found")
    return tariff_cell

@router.post("/", response_model=TariffCellResponse)
def create_tariff_cell(tariff_cell: TariffCellCreate):
    db_tariff_cell = create_tariff_cell_service(tariff_cell)
    if not db_tariff_cell:
        raise HTTPException(status_code=400, detail="Error creating tariff cell")
    return db_tariff_cell

@router.put("/{tariff_cell_id}", response_model=TariffCellResponse)
def update_tariff_cell(tariff_cell_id: int, tariff_cell: TariffCellUpdate):
    db_tariff_cell = update_tariff_cell_service(tariff_cell_id, tariff_cell)
    if not db_tariff_cell:
        raise HTTPException(status_code=404, detail="Tariff cell not found")
    return db_tariff_cell

@router.delete("/{tariff_cell_id}", response_model=TariffCellResponse)
def delete_tariff_cell(tariff_cell_id: int):
    db_tariff_cell = delete_tariff_cell_service(tariff_cell_id)
    if not db_tariff_cell:
        raise HTTPException(status_code=404, detail="Tariff cell not found")
    return db_tariff_cell
