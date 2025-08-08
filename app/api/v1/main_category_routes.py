from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.services.main_category_service import get_main_category_by_id, create_main_category_service, update_main_category_service, get_all_main_categories_service
from app.schemas.main_category_schema import MainCategoryResponse, MainCategoryCreateResponse, MainCategoryUpdateResponse, MainCategoryUpdate

router = APIRouter(prefix="/main-categories", tags=["Main Categories"])

@router.get("/categories", response_model=list[MainCategoryResponse])
def list_all_main_categories(db: Session = Depends(get_db)):
    return get_all_main_categories_service(db)

@router.get("/{main_category_id}", response_model=MainCategoryResponse)
def get_main_category(main_category_id: int):
    main_category = get_main_category_by_id(main_category_id)
    if not main_category:
        raise HTTPException(status_code=404, detail="Ana kategori bulunamadı")
    return main_category

@router.post("/new-categories", response_model=MainCategoryCreateResponse)
def add_main_category(main_category_data: MainCategoryCreateResponse):
    try:
        created_category = create_main_category_service(main_category_data)
        return created_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{main_category_id}", response_model=MainCategoryUpdate)
def update_main_category(main_category_id: int, main_category_data: MainCategoryUpdateResponse):
    try:
        updated_category = update_main_category_service(main_category_data, main_category_id)
        if not updated_category:
            raise HTTPException(status_code=404, detail="Ana kategori bulunamadı")
        return updated_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
