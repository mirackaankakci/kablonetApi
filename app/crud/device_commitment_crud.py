from app.db.database import get_db
from sqlalchemy.orm import Session, joinedload
from app.db.database import SessionLocal
from app.db.models.device_commitment import DeviceCommitment
from app.db.models.devices import Devices


db: Session = SessionLocal()

def get_device_commitment_by_id_from_db(device_commitment_id: int):
    device_commitment = db.query(DeviceCommitment).options(
        joinedload(DeviceCommitment.devices)
            .joinedload(Devices.main_category),
        joinedload(DeviceCommitment.commitment_period)
    ).filter(DeviceCommitment.id == device_commitment_id).first()
    db.close()
    return device_commitment

def create_device_commitment_from_db(device_commitment_data):
    new_device_commitment = DeviceCommitment(**device_commitment_data.dict())
    db.add(new_device_commitment)
    db.commit()
    db.refresh(new_device_commitment)
    db.close()
    return new_device_commitment

def update_device_commitment_from_db(device_commitment_id: int, device_commitment_data):
    device_commitment = db.query(DeviceCommitment).filter(DeviceCommitment.id == device_commitment_id).first()
    if not device_commitment:
        db.close()
        return None
    for key, value in device_commitment_data.dict().items():
        setattr(device_commitment, key, value)
    db.commit()
    db.refresh(device_commitment)
    db.close()
    return device_commitment

def get_all_device_commitments_from_db(device_id: int):
    # device_commitments = db.query(DeviceCommitment).options(
    #     joinedload(DeviceCommitment.devices)
    #         .joinedload(Devices.main_category),
    #     joinedload(DeviceCommitment.commitment_period)
    # ).order_by(Devices.id).all()
    # db.close()
    device_commitments = db.query(DeviceCommitment).options(
        joinedload(DeviceCommitment.devices)
            .joinedload(Devices.main_category),
        joinedload(DeviceCommitment.commitment_period)
    ).filter(DeviceCommitment.devices_id == device_id).order_by(DeviceCommitment.id).all()
    db.close()
    return device_commitments