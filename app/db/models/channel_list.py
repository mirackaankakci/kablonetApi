from sqlalchemy import Column, Integer, String
from app.db.base import Base

class channel_list(Base):
    __tablename__ = "chanel_list"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    kanal_no = Column(Integer, nullable=False, unique=True)
    kanal_adi = Column(String, nullable=False, unique=True)
    dijital_frekans = Column(String, nullable=True, unique=False)
    analog_frekans = Column(String, nullable=True, unique=False)