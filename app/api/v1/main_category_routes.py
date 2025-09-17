from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.main_category_service import get_main_category_by_id, create_main_category_service, update_main_category_service, get_all_main_categories_service, deactivate_main_category_services
from app.schemas.main_category_schema import (
    MainCategoryResponse, 
    MainCategoryCreateRequest,
    MainCategoryCreateResponse, 
    MainCategoryUpdateResponse,
    MainCategoryUpdate, 
    DeleteMainCategoryResponse
)
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator

router = APIRouter(prefix="/main-categories", tags=["Main Categories"])

@router.get("/categories", response_model=list[MainCategoryResponse], summary="Get All Main Categories (Public)")
def list_all_main_categories(db: Session = Depends(get_db)):
    return get_all_main_categories_service(db)

@router.get("/{main_category_id}", response_model=MainCategoryResponse, summary="Get Main Category by ID (Public)")
def get_main_category(main_category_id: int, db: Session = Depends(get_db)):
    main_category = get_main_category_by_id(main_category_id, db)
    return main_category

@router.post("/new-categories", response_model=MainCategoryCreateResponse, summary="Create New Main Category (Admin Only)")
def add_main_category(
    main_category_data: MainCategoryCreateRequest,  # Input schema
    db: Session = Depends(get_db), 
    current_user: dict = Depends(require_admin())
):
    created_category = create_main_category_service(main_category_data, db)
    return created_category

@router.put("/{main_category_id}", response_model=MainCategoryUpdateResponse, summary="Update Main Category (Admin Only)")
def update_main_category(
    main_category_id: int, 
    main_category_data: MainCategoryUpdate,  # Input schema
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    updated_category = update_main_category_service(main_category_data, main_category_id, db)
    return updated_category

@router.delete("/{main_category_id}", response_model=DeleteMainCategoryResponse, summary="Delete Main Category (Admin Only)")
def deactivate_main_category(
    main_category_id: int, 
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_admin())
):
    deactivate = deactivate_main_category_services(main_category_id, db)
    return deactivate
