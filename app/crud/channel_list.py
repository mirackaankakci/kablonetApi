from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.channel_list import channel_list

db: Session = SessionLocal()


#channel getirme işlemi
def get_channel_list_by_id(channel_id: int, db: Session):
    channel = db.query(channel_list).filter(channel_list.id == channel_id,
                                        channel_list.is_active == True).first()
    #
    return channel


#channel olusturma işlemi
def create_channel_list(channel_data, db: Session):
    new_channel = channel_list(**channel_data)
    db.add(new_channel)
    db.commit()
    db.refresh(new_channel)
    #
    return new_channel

#güncelleme işlemi
def update_channel_list(channel_data, channel_id: int, db: Session):
    channel = db.query(channel_list).filter(channel_list.id == channel_id).first()
    if not channel:
        #
        return None
    for key, value in channel_data.items():
        setattr(channel, key, value)
    db.commit()
    db.refresh(channel)
    #
    return channel

#channel listeleme işlemi
def get_all_channel_list(db: Session):
    channel = db.query(channel_list).filter(channel_list.is_active == True).order_by(channel_list.id).all()
    #
    return channel

def deactivate_channel_list_from_db(channel_id: int, db: Session):
    channel = db.query(channel_list).filter(channel_list.id == channel_id,
                                                    channel_list.is_active == True).first()
    if not channel:
        #
        return None
    
    if not channel.is_active:
        return channel 
    
    channel.is_active = False
    
    db.commit()
    db.refresh(channel)
    #
    return channel
