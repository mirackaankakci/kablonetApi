from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.channels import Channels

db: Session = SessionLocal()

def get_channels_by_id_from_db(channels_id: int, db: Session):
    channel = db.query(Channels).options(
        joinedload(Channels.channel_category)
    ).filter(Channels.id == channels_id,
            Channels.is_active == True).first()
    #
    return channel

def create_channels_from_db(channels_data, db: Session):
    new_channels = Channels(**channels_data)
    db.add(new_channels)
    db.commit()
    db.refresh(new_channels)
    #
    return new_channels

def update_channels_from_db(channels_id: int, channels_data, db: Session):
    channel = db.query(Channels).filter(Channels.id == channels_id).first()
    if not channel:
        #
        return None
    for key, value in channels_data.items():
        setattr(channel, key, value)
    db.commit()
    db.refresh(channel)
    #
    return channel

def list_all_channels_from_db(db: Session):
    channel = db.query(Channels).options(
        joinedload(Channels.channel_category)
    ).filter(Channels.is_active == True).order_by(Channels.id).all()
    #
    return channel

def get_channels_by_category_id_from_db(channel_category_id: int, db: Session):
    channel_category = db.query(Channels).options(
        joinedload(Channels.channel_category)
    ).filter(Channels.channel_category_id == channel_category_id,
            Channels.is_active == True).order_by(Channels.id).all()
    #
    return channel_category

def deactivate_channels_from_db(channels_id: int, db: Session):
    channel = db.query(Channels).filter(Channels.id == channels_id,
                                                    Channels.is_active == True).first()
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