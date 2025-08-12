from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.channels import Channels

db: Session = SessionLocal()

def get_channels_by_id_from_db(channels_id: int):
    channel = db.query(Channels).options(
        joinedload(Channels.channel_category)
    ).filter(Channels.id == channels_id).first()
    db.close()
    return channel

def create_channels_from_db(channels_data):
    new_channels = Channels(**channels_data.dict())
    db.add(new_channels)
    db.commit()
    db.refresh(new_channels)
    db.close()
    return new_channels

def update_channels_from_db(channels_id: int, channels_data):
    channel = db.query(Channels).filter(Channels.id == channels_id).first()
    if not channel:
        db.close()
        return None
    for key, value in channels_data.dict().items():
        setattr(channel, key, value)
    db.commit()
    db.refresh(channel)
    db.close()
    return channel

def list_all_channels_from_db(db: Session):
    channel = db.query(Channels).options(
        joinedload(Channels.channel_category)
    ).order_by(Channels.id).all()
    db.close()
    return channel