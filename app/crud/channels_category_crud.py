from app.db.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.db.database import SessionLocal
from app.db.models.channel_category import ChannelCategory

db: Session = SessionLocal()

def get_channel_category_by_id_from_db(channel_category_id: int, db: Session):
    channel_category= db.query(ChannelCategory).filter(ChannelCategory.id == channel_category_id,
                                                    ChannelCategory.is_active == True).first()
    #
    return channel_category

def create_channel_category_from_db(channel_category_data, db: Session):
    new_channel_category = ChannelCategory(**channel_category_data)
    
    try:
        db.add(new_channel_category)
        db.commit()
        db.refresh(new_channel_category)
        #
        return new_channel_category
    except IntegrityError as e:
        db.rollback()
        if 'idx_unique_active_channel_category_name' in str(e):
            raise HTTPException(400, detail="Bu kategori ismi zaten kullanılıyor.")
        else:
            raise HTTPException(400, detail="Benzersizlik hatası.")

def update_channel_category_in_db(channel_category_data, channel_category_id: int, db: Session):
    channel_category = db.query(ChannelCategory).filter(ChannelCategory.id == channel_category_id).first()
    try:
        if not channel_category:
            #
            return None
        for key, value in channel_category_data.items():
            setattr(channel_category, key, value)
        db.commit()
        db.refresh(channel_category)
        #
        return channel_category
    except IntegrityError as e:
        db.rollback()
        if 'idx_unique_active_channel_category_name' in str(e):
            raise HTTPException(400, detail="Bu kategori ismi zaten kullanılıyor.")
        else:
            raise HTTPException(400, detail="Benzersizlik hatası.")

def list_all_channel_category_from_db(db: Session):
    channel_categories = db.query(ChannelCategory).filter(ChannelCategory.is_active == True).order_by(ChannelCategory.id).all()
    #
    return channel_categories

def deactivate_channel_category_from_db(channel_category_id: int, db: Session):
    channel_category = db.query(ChannelCategory).filter(ChannelCategory.id == channel_category_id,
                                                    ChannelCategory.is_active == True).first()
    if not channel_category:
        #
        return None
    
    if not channel_category.is_active:
        return channel_category 
    
    channel_category.is_active = False
    
    db.commit()
    db.refresh(channel_category)
    #
    return channel_category