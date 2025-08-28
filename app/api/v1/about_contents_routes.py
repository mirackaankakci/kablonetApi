from fastapi import APIRouter, Depends, HTTPException
from app.schemas.about_contents_schemas import AboutContentsSchema, AboutContentsCreateSchema, AboutContentsUpdateSchema, DeleteAboutContentsSchema
from app.services.about_contents_services import get_about_content_service, create_about_content_service, update_about_content_service, get_all_about_contents_service, get_all_about_contents_by_category_service, deactivate_about_content_services
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
    contents = get_all_about_contents_by_category_service(main_category_id, db)
    return contents

@router.get("/{content_id}", response_model=AboutContentsSchema)
def get_about_content(content_id: int, db: Session = Depends(get_db)):
    content = get_about_content_service(content_id, db)
    return content

@router.post("/new-content", response_model=AboutContentsCreateSchema)
def add_about_content(content_data: AboutContentsCreateSchema, db: Session = Depends(get_db)):
    created_content = create_about_content_service(content_data, db)
    return created_content

@router.put("/{content_id}", response_model=AboutContentsUpdateSchema)
def update_about_content(content_id: int, content_data: AboutContentsUpdateSchema, db: Session = Depends(get_db)):
    updated_content = update_about_content_service(content_id, content_data, db)
    return updated_content

@router.delete("/{about_content_id}", response_model=DeleteAboutContentsSchema)
def deactivate_about_content(about_content_id: int, db: Session = Depends(get_db)):
    deactivate = deactivate_about_content_services(about_content_id, db)
    return deactivate

