from fastapi import APIRouter, Depends, HTTPException
from app.schemas.about_contents_schemas import AboutContentsSchema, AboutContentsCreateSchema, AboutContentsUpdateSchema, AboutContentsResponse
from app.services.about_contents_services import get_about_content_service, create_about_content_service, update_about_content_service


router = APIRouter(prefix="/content", tags=["About Contents"])



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