from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models.channel_category import ChannelCategory

db: Session = SessionLocal()

def get_channel_category_by_id_from_db(channel_category_id: int):
    channel_category= db.query(ChannelCategory).filter(ChannelCategory.id == channel_category_id).first()
    db.close()
    return channel_category

def create_channel_category_from_db(channel_category_data):
    new_channel_category = ChannelCategory(**channel_category_data.dict())
    db.add(new_channel_category)
    db.commit()
    db.refresh(new_channel_category)
    db.close()
    return new_channel_category

def update_channel_category_in_db(channel_category_data, channel_category_id: int):
    db: Session = SessionLocal()
    channel_category = db.query(ChannelCategory).filter(ChannelCategory.id == channel_category_id).first()
    if not channel_category:
        db.close()
        return None
    for key, value in channel_category_data.dict().items():
        setattr(channel_category, key, value)
    db.commit()
    db.refresh(channel_category)
    db.close()
    return channel_category

def list_all_channel_category_from_db(db: Session):
    channel_categories = db.query(ChannelCategory).order_by(ChannelCategory.id).all()
    db.close()
    return channel_categories