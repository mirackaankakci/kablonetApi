from app.db.database import get_db
from app.db.models.commitment_period import CommitmentPeriod
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

db: Session = SessionLocal()

def get_commitment_period_by_id_from_db(commitment_period_id: int, db: Session):
    commitment_period = db.query(CommitmentPeriod).filter(CommitmentPeriod.id == commitment_period_id,
                                                        CommitmentPeriod.is_active == True).first()
    #
    return commitment_period

def create_commitment_period_from_db(commitment_period_data, db: Session):
    new_commitment_period = CommitmentPeriod(**commitment_period_data)
    db.add(new_commitment_period)
    db.commit()
    db.refresh(new_commitment_period)
    #
    return new_commitment_period

def update_commitment_period_in_db(commitment_period_data, commitment_period_id: int, db: Session):
    commitment_period = db.query(CommitmentPeriod).filter(CommitmentPeriod.id == commitment_period_id).first()
    if not commitment_period:
        #
        return None
    for key, value in commitment_period_data.items():
        setattr(commitment_period, key, value)
    db.commit()
    db.refresh(commitment_period)
    #
    return commitment_period

def list_all_commitment_period_from_db(db: Session):
    commitment_periods = db.query(CommitmentPeriod).filter(CommitmentPeriod.is_active == True).order_by(CommitmentPeriod.id).all()
    #
    return commitment_periods

def deactivate_commitment_period_from_db(commitment_period_id: int, db: Session):
    commitment_period = db.query(CommitmentPeriod).filter(CommitmentPeriod.id == commitment_period_id,
                                                    CommitmentPeriod.is_active == True).first()
    if not commitment_period:
        #
        return None
    
    if not commitment_period.is_active:
        return commitment_period 
    
    commitment_period.is_active = False
    
    db.commit()
    db.refresh(commitment_period)
    #
    return commitment_period