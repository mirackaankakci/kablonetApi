from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.kanal_listesi import kanal_listesi

#kanal getirme işlemi
def get_kanal_listesi_by_id(kanal_id: int):
    db: Session = SessionLocal()
    kanal = db.query(kanal_listesi).filter(kanal_listesi.id == kanal_id).first()
    db.close()
    return kanal


#kanal olusturma işlemi
def create_kanal_listesi(kanal_data: dict):
    db: Session = SessionLocal()
    new_kanal = kanal_listesi(**kanal_data)
    db.add(new_kanal)
    db.commit()
    db.refresh(new_kanal)
    db.close()
    return new_kanal

#güncelleme işlemi
def update_kanal_listesi(kanal_id: int, kanal_data: dict):
    db: Session = SessionLocal()
    kanal = db.query(kanal_listesi).filter(kanal_listesi.id == kanal_id).first()
    if not kanal:
        db.close()
        return None
    for key, value in kanal_data.items():
        setattr(kanal, key, value)
    db.commit()
    db.refresh(kanal)
    db.close()
    return kanal

#kanal listeleme işlemi
def get_all_kanal_listesi(db: Session):
    # db: Session = SessionLocal()
    # kanal_list = db.query(kanal_listesi).all()
    # db.close()
    return db.query(kanal_listesi).order_by(kanal_listesi.id).all()

#silme işlemi 