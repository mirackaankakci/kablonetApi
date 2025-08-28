from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.packages_channels import PackagesChannels
from app.db.models.channels import Channels
from app.db.models.packages import Packages

db: Session = SessionLocal()

def get_packages_channels_by_id_from_db(packages_channels_id: int, db: Session):
    packages_channels= db.query(PackagesChannels).options(
    joinedload(PackagesChannels.channels)
        .joinedload(Channels.channel_category),
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.main_category),  
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.packages_category)
    ).filter(PackagesChannels.id == packages_channels_id,
            PackagesChannels.is_active == True).first()
    #
    return packages_channels
    
def create_packages_channels_from_db(packages_channels_data, db: Session):
    new_packages_channels = PackagesChannels(**packages_channels_data)
    db.add(new_packages_channels)
    db.commit()
    db.refresh(new_packages_channels)
    #
    return new_packages_channels

def update_packages_channels_from_db(packages_channels_id: int, packages_channels_data, db: Session):
    packages_channels = db.query(PackagesChannels).filter(PackagesChannels.id == packages_channels_id).first()
    if not packages_channels:
        #
        return None
    for key, value in packages_channels_data.items():
        setattr(packages_channels, key, value)
    db.commit()
    db.refresh(packages_channels)
    #
    return packages_channels

def list_all_packages_channels_from_db(db: Session):
    packages_channels= db.query(PackagesChannels).options(
    joinedload(PackagesChannels.channels)
        .joinedload(Channels.channel_category),
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.main_category),  
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.packages_category)
    ).filter(PackagesChannels.is_active == True).order_by(PackagesChannels.id).all()
    #
    return packages_channels


def get_packages_channels_by_packages_from_db(packages_id: int, db: Session):
    packages_channels= db.query(PackagesChannels).options(
    joinedload(PackagesChannels.channels)
        .joinedload(Channels.channel_category),
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.main_category),  
    joinedload(PackagesChannels.packages)
        .joinedload(Packages.packages_category)
    ).filter(PackagesChannels.packages_id == packages_id,
            PackagesChannels.is_active == True).order_by(PackagesChannels.id).all()
    #
    return packages_channels

def deactivate_packages_channels_from_db(packages_channels_id: int, db: Session):
    packages_channels = db.query(PackagesChannels).filter(PackagesChannels.id == packages_channels_id,
                                                    PackagesChannels.is_active == True).first()
    if not packages_channels:
        #
        return None
    
    if not packages_channels.is_active:
        return packages_channels 
    
    packages_channels.is_active = False
    
    db.commit()
    db.refresh(packages_channels)
    #
    return packages_channels