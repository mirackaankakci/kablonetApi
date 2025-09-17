from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.services.tariff_line_service import TariffLineService
from app.schemas.tariff_line_schema import (
    TariffLineResponse,
    TariffLineCreateRequest,
    TariffLineUpdateRequest,
    TariffLineDeleteRequest,
)
from app.db.database import get_db
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator



router = APIRouter(prefix="/tariff-lines", tags=["Tariff Lines"])


@router.get("/", response_model=list[TariffLineResponse], summary="Get All Tariff Lines (Authenticated)")
def read_tariff_lines(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Get all tariff lines.
    
    **Authorization Required:**
    - Valid JWT token (any authenticated user)
    """
    return TariffLineService.get_tariff_lines(db)

@router.get("/{tariff_line_id}", response_model=TariffLineResponse, summary="Get Tariff Line by ID (Authenticated)")
def read_tariff_line(
    tariff_line_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Get specific tariff line by ID.
    
    **Authorization Required:**
    - Valid JWT token (any authenticated user)
    """
    return TariffLineService.get_tariff_line_by_id(db, tariff_line_id)

@router.post("/", response_model=TariffLineResponse, status_code=status.HTTP_201_CREATED, summary="Create Tariff Line (Admin Only)")
def create_tariff_line(
    tariff_line: TariffLineCreateRequest, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    """
    Create new tariff line.
    
    **Authorization Required:**
    - Admin privileges
    """
    return TariffLineService.create_tariff_line(db, tariff_line)

@router.put("/{tariff_line_id}", response_model=TariffLineResponse, summary="Update Tariff Line (Admin Only)")
def update_tariff_line(
    tariff_line_id: int, 
    tariff_line: TariffLineUpdateRequest, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    """
    Update existing tariff line.
    
    **Authorization Required:**
    - Admin privileges
    """
    return TariffLineService.update_tariff_line(db, tariff_line_id, tariff_line)

@router.delete("/{tariff_line_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Tariff Line (Admin Only)")
def delete_tariff_line(
    tariff_line_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    """
    Delete tariff line.
    
    **Authorization Required:**
    - Admin privileges
    """
    TariffLineService.delete_tariff_line(db, tariff_line_id)
    return None

