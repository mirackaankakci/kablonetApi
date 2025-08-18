from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.tariff_line_service import (
    get_tariff_line_by_id_service,
    get_tariff_lines_service,
    create_tariff_line_service,
    update_tariff_line_service,
    delete_tariff_line_service,
)
from app.schemas.tariff_line_schema import (
    TariffLineResponse,
    TariffLineCreateRequest,
    TariffLineUpdateRequest,
    TariffLineDeleteRequest,
)
from app.db.database import get_db



router = APIRouter(prefix="/tariff-lines", tags=["Tariff Lines"])


@router.get("/", response_model=list[TariffLineResponse])
def read_tariff_lines(db: Session = Depends(get_db)):
    return get_tariff_lines_service(db)

@router.get("/{tariff_line_id}", response_model=TariffLineResponse)
def read_tariff_line(tariff_line_id: int, db: Session = Depends(get_db)):
    tariff_line = get_tariff_line_by_id_service(db, tariff_line_id)
    if not tariff_line:
        raise HTTPException(status_code=404, detail="Tariff line not found")
    return tariff_line


@router.post("/", response_model=TariffLineResponse, status_code=status.HTTP_201_CREATED)
def create_tariff_line(tariff_line: TariffLineCreateRequest, db: Session = Depends(get_db)):
    db_tariff_line = create_tariff_line_service(db, tariff_line)
    if not db_tariff_line:
        raise HTTPException(status_code=400, detail="Error creating tariff line")
    return db_tariff_line

@router.put("/{tariff_line_id}", response_model=TariffLineResponse)
def update_tariff_line(tariff_line_id: int, tariff_line: TariffLineUpdateRequest, db: Session = Depends(get_db)):
    db_tariff_line = update_tariff_line_service(db, tariff_line_id, tariff_line)
    if not db_tariff_line:
        raise HTTPException(status_code=400, detail="Error updating tariff line")
    return db_tariff_line

@router.delete("/{tariff_line_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tariff_line(tariff_line_id: int, db: Session = Depends(get_db)):
    db_tariff_line = delete_tariff_line_service(db, tariff_line_id)
    if not db_tariff_line:
        raise HTTPException(status_code=404, detail="Tariff line not found")
    return None

