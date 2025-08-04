from app.crud.kanal_listesi import create_kanal_listesi, get_kanal_listesi_by_id, update_kanal_listesi, get_all_kanal_listesi                                                                                                        
from app.schemas.kanal_listesi_schema import KanalListesiCreate, KanalListesiUpdate, KanalListesiResponse, KanalListesiAllResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session

def get_kanal_listesi_by_id_from_db(kanal_id: int):
    return get_kanal_listesi_by_id(kanal_id)

def create_kanal_listesi_service(kanal_data: KanalListesiCreate):
    return create_kanal_listesi(kanal_data)

def update_kanal_listesi_service(kanal_id: int, kanal_data: KanalListesiUpdate):
    updated_kanal = update_kanal_listesi(kanal_id, kanal_data)
    if not updated_kanal:
        raise HTTPException(status_code=404, detail="Kanal bulunamadı")
    return updated_kanal

def get_all_kanal_listesi_service(db: Session):
    kanal_list = get_all_kanal_listesi(db)
    if not kanal_list:
        raise HTTPException(status_code=404, detail="Kanal listesi bulunamadı")
    return [KanalListesiAllResponse.from_orm(kanal) for kanal in kanal_list]
    