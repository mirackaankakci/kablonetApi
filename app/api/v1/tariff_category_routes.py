from fastapi import APIRouter, Depends, HTTPException
from app.services.tariff_category_service import get_main_tariff_category_by_id, create_tariff_category_service, get_tariff_categories_service
from app.schemas.tariff_category_schema import TariffCategoryCreatedResponse, TariffCategoryResponse
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator


router = APIRouter(prefix="/tariff-categories", tags=["Tariff Categories"])

@router.get("/", response_model=list[TariffCategoryResponse], summary="Get All Tariff Categories")
def read_tariff_categories(current_user: dict = Depends(get_current_user)):
    """
    Get all tariff categories.
    
    **Authorization Required:**
    - Valid JWT token (any authenticated user)
    """
    return get_tariff_categories_service()

@router.get("/{tariff_category_id}", response_model=TariffCategoryResponse, summary="Get Tariff Category by ID")
def read_tariff_category(tariff_category_id: int, current_user: dict = Depends(get_current_user)):
    """
    Get specific tariff category by ID.
    
    **Authorization Required:**
    - Valid JWT token (any authenticated user)
    """
    db_tariff_category = get_main_tariff_category_by_id(tariff_category_id)
    if not db_tariff_category:
        raise HTTPException(status_code=404, detail="Tariff category not found")
    return db_tariff_category

@router.post("/", response_model=TariffCategoryResponse, summary="Create Tariff Category (Admin Only)")
def create_tariff_category(
    tariff_category: TariffCategoryCreatedResponse, 
    current_user: dict = Depends(require_admin())
):
    """
    Create a new tariff category.
    
    **Authorization Required:**
    - Valid JWT token
    - Admin role required
    """
    db_tariff_category = create_tariff_category_service(tariff_category)
    if not db_tariff_category:
        raise HTTPException(status_code=400, detail="Error creating tariff category")
    return db_tariff_category
