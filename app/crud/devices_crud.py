from app.db.database import get_db
from app.db.models.devices import Devices
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_device_by_category_from_db(main_category_id: int, db: Session):
    device = db.query(Devices).options(
        joinedload(Devices.main_category)
    ).filter(Devices.main_category_id == main_category_id,
            Devices.is_active == True).order_by(Devices.id).all()
    #
    return device

def get_device_by_id_from_db(device_id: int, db: Session):
    device = db.query(Devices).options(
        joinedload(Devices.main_category)
    ).filter(Devices.id == device_id,
            Devices.is_active == True).first()
    #
    return device



def create_device_from_db(device_data, db: Session):
    new_device =Devices(**device_data)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    #
    return new_device

def update_device_from_db(device_id: int, device_data, db: Session):
    device= db.query(Devices).filter(Devices.id == device_id).first()
    if not device:
        #
        return None
    for key, value in device_data.items():
        setattr(device, key, value)
    db.commit()
    db.refresh(device)
    #
    return device

def list_all_devices_from_db(db: Session):
    devices = db.query(Devices).options(
        joinedload(Devices.main_category)
    ).filter(Devices.is_active == True).order_by(Devices.id).all()
    #
    return devices


def deactivate_devices_from_db(device_id: int, db: Session):
    device = db.query(Devices).filter(Devices.id == device_id,
                                                    Devices.is_active == True).first()
    if not device:
        #
        return None
    
    if not device.is_active:
        return device 
    
    device.is_active = False
    
    db.commit()
    db.refresh(device)
    #
    return device