from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.device_commitment import DeviceCommitment
from app.db.models.devices import Devices


db: Session = SessionLocal()

def get_device_commitment_by_id_from_db(device_commitment_id: int, db: Session):
    device_commitment = db.query(DeviceCommitment).options(
        joinedload(DeviceCommitment.devices)
            .joinedload(Devices.main_category),
        joinedload(DeviceCommitment.commitment_period)
    ).filter(DeviceCommitment.id == device_commitment_id,
            DeviceCommitment.is_active == True).first()
    #
    return device_commitment

def create_device_commitment_from_db(device_commitment_data, db: Session):
    new_device_commitment = DeviceCommitment(**device_commitment_data)
    db.add(new_device_commitment)
    db.commit()
    db.refresh(new_device_commitment)
    #
    return new_device_commitment

def update_device_commitment_from_db(device_commitment_id: int, device_commitment_data, db: Session):
    device_commitment = db.query(DeviceCommitment).filter(DeviceCommitment.id == device_commitment_id).first()
    if not device_commitment:
        #
        return None
    for key, value in device_commitment_data.items():
        setattr(device_commitment, key, value)
    db.commit()
    db.refresh(device_commitment)
    #
    return device_commitment

def get_all_device_commitments_device_from_db(device_id: int, db: Session):
    device_commitments = db.query(DeviceCommitment).options(
        joinedload(DeviceCommitment.devices)
            .joinedload(Devices.main_category),
        joinedload(DeviceCommitment.commitment_period)
    ).filter(DeviceCommitment.devices_id == device_id,
            DeviceCommitment.is_active == True).order_by(DeviceCommitment.id).all()
    #
    return device_commitments

def list_all_device_commitments_from_db(db: Session):
    device_commitments = db.query(DeviceCommitment).options(
        joinedload(DeviceCommitment.devices)
            .joinedload(Devices.main_category),
        joinedload(DeviceCommitment.commitment_period)
    ).filter(DeviceCommitment.is_active == True).order_by(DeviceCommitment.id).all()
    #
    return device_commitments


def deactivate_device_commitments_from_db(device_commitment_id: int, db: Session):
    device_commitment = db.query(DeviceCommitment).filter(DeviceCommitment.id == device_commitment_id,
                                                    DeviceCommitment.is_active == True).first()
    if not device_commitment:
        #
        return None
    
    if not device_commitment.is_active:
        return device_commitment 
    
    device_commitment.is_active = False
    
    db.commit()
    db.refresh(device_commitment)
    #
    return device_commitment