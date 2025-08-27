from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.channel_list import channel_list

db: Session = SessionLocal()


#channel getirme işlemi
def get_channel_list_by_id(channel_id: int, db: Session):
    channel = db.query(channel_list).filter(channel_list.id == channel_id).first()
    db.close()
    return channel


#channel olusturma işlemi
def create_channel_list(channel_data, db: Session):
    new_channel = channel_list(**channel_data)
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    db.close()
    return new_channel

#güncelleme işlemi
def update_channel_list(channel_data, channel_id: int, db: Session):
    channel = db.query(channel_list).filter(channel_list.id == channel_id).first()
    if not channel:
        db.close()
        return None
    for key, value in channel_data.dict().items():
        setattr(channel, key, value)
    db.commit()
    db.refresh(channel)
    db.close()
    return channel

#channel listeleme işlemi
def get_all_channel_list(db: Session):
    channel = db.query(channel_list).order_by(channel_list.id).all()
    db.close()
    return channel

