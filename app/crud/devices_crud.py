from app.db.database import get_db
from app.db.models.devices import Devices
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_device_by_id_from_db(device_id: int):
    device = db.query(Devices).options(
        joinedload(Devices.main_category)
    ).filter(Devices.id == device_id).first()
    db.close()
    return device

def create_device_from_db(device_data):
    new_device =Devices(**device_data.dict())
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    db.close()
    return new_device

def update_device_from_db(device_id: int, device_data):
    device= db.query(Devices).filter(Devices.id == device_id).first()
    if not device:
        db.close()
        return None
    for key, value in device_data.dict().items():
        setattr(device, key, value)
    db.commit()
    db.refresh(device)
    db.close()
    return device

def list_all_devices_from_db(db: Session):
    devices = db.query(Devices).options(
        joinedload(Devices.main_category)
    ).order_by(Devices.id).all()
    db.close()
    db.close()
    return devices