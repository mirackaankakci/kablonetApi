from fastapi import APIRouter, Depends, HTTPException
from app.schemas.about_contents_schemas import AboutContentsSchema, AboutContentsCreateSchema, AboutContentsUpdateSchema, AboutContentsResponse
from app.services.about_contents_services import get_about_content_service, create_about_content_service, update_about_content_service, get_all_about_contents_service, get_all_about_contents_by_category_service
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(prefix="/content", tags=["About Contents"])

## List all contents - hepsi listelenir
@router.get("/contents", response_model=list[AboutContentsSchema])
def list_all_contents(db: Session= Depends(get_db)):
    return get_all_about_contents_service(db)

## List all contents by category - hepsi kategoriye gore listelenir
@router.get("/contents-category", response_model=list[AboutContentsSchema])
def list_all_contents_category(main_category_id: int, db: Session = Depends(get_db)):
    contents = get_all_about_contents_by_category_service(main_category_id)
    if not contents:
        raise HTTPException(status_code=404, detail="No contents found for this category")
    return contents


@router.get("/{content_id}", response_model=AboutContentsSchema)
def get_about_content(content_id: int):
    content = get_about_content_service(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.post("/new-content", response_model=AboutContentsCreateSchema)
def add_about_content(content_data: AboutContentsCreateSchema):
    try:
        created_content = create_about_content_service(content_data)
        return created_content
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{content_id}", response_model=AboutContentsUpdateSchema)
def update_about_content(content_id: int, content_data: AboutContentsUpdateSchema):
    try:
        updated_content = update_about_content_service(content_id, content_data)
        if not updated_content:
            raise HTTPException(status_code=404, detail="Content not found")
        return updated_content
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))