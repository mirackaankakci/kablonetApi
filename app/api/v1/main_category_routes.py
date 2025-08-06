from fastapi import APIRouter, Depends, HTTPException
from app.services.main_category_service import get_main_category_by_id, create_main_category_service
from app.schemas.main_category_schema import MainCategoryResponse, MainCategoryCreateResponse

router = APIRouter(prefix="/main-categories", tags=["Main Categories"])

@router.get("/{main_category_id}", response_model=MainCategoryResponse)
def get_main_category(main_category_id: int):
    main_category = get_main_category_by_id(main_category_id)
    if not main_category:
        raise HTTPException(status_code=404, detail="Ana kategori bulunamadı")
    return main_category

@router.post("/", response_model=MainCategoryResponse)
def add_main_category(main_category_data: MainCategoryCreateResponse):
    try:
        created_category = create_main_category_service(main_category_data)
        return created_category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


