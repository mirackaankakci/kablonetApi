from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.packages_channels import PackagesChannels
from app.db.models.channels import Channels
from app.db.models.packages import Packages

db: Session = SessionLocal()

def get_packages_channels_by_id_from_db(packages_channels_id: int):
    packages_channels= db.query(PackagesChannels).options(
        joinedload(PackagesChannels.channels)
            .joinedload(Channels.channel_category),
        joinedload(PackagesChannels.packages)
            .joinedload(Packages.packages_category)
            .joinedload(Packages.main_category)
    ).filter(PackagesChannels.id == packages_channels_id).first()
    db.close()
    return packages_channels
    
def create_packages_channels_from_db(packages_channels_data):
    new_packages_channels = PackagesChannels(**packages_channels_data.dict())
    db.add(new_packages_channels)
    db.commit()
    db.refresh(new_packages_channels)
    db.close()
    return new_packages_channels

def update_packages_channels_from_db(packages_channels_id: int, packages_channels_data):
    packages_channels = db.query(PackagesChannels).filter(PackagesChannels.id == packages_channels_id).first()
    if not packages_channels:
        db.close()
        return None
    for key, value in packages_channels_data.dict().items():
        setattr(packages_channels, key, value)
    db.commit()
    db.refresh(packages_channels)
    db.close()
    return packages_channels

def list_all_packages_channels_from_db(db: Session):
    packages_channels= db.query(PackagesChannels).options(
        joinedload(PackagesChannels.channels)
            .joinedload(Channels.channel_category),
        joinedload(PackagesChannels.packages)
            .joinedload(Packages.packages_category)
            .joinedload(Packages.main_category)
    ).order_by(PackagesChannels.id).all()
    db.close()
    return packages_channels