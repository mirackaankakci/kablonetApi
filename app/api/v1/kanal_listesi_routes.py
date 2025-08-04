from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services.kanal_listesi_service import get_kanal_listesi_by_id_from_db, create_kanal_listesi_service, update_kanal_listesi_service, get_all_kanal_listesi_service
from app.schemas.kanal_listesi_schema import KanalListesiResponse, KanalListesiCreate, KanalListesiUpdate, KanalListesiAllResponse

router = APIRouter(prefix="/kanal-listesi", tags=["Kanal Listesi"])

@router.get("/kanallar", response_model=list[KanalListesiResponse])
def list_all_kanallar(db: Session = Depends(get_db)):
    return get_all_kanal_listesi_service(db)

@router.get("/{kanal_id}", response_model=KanalListesiResponse)
def get_kanal(kanal_id: int):
    kanal = get_kanal_listesi_by_id_from_db(kanal_id)
    if not kanal:
        raise HTTPException(status_code=404, detail="Kanal bulunamadı")
    return kanal

@router.post("/new-kanal", response_model=KanalListesiResponse)
def add_kanal(kanal_data: KanalListesiCreate):
    created_kanal = create_kanal_listesi_service(kanal_data.dict())
    if not created_kanal:
        raise HTTPException(status_code=400, detail="Kanal oluşturulamadı")
    return created_kanal

@router.put("/{kanal_id}", response_model=KanalListesiResponse)
def update_kanal(kanal_id: int, kanal_data: KanalListesiUpdate):
    updated_kanal = update_kanal_listesi_service(kanal_id, kanal_data.dict())
    if not updated_kanal:
        raise HTTPException(status_code=404, detail="Kanal bulunamadı")
    return updated_kanal

