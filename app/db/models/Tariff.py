from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Tariff(Base):
    __tablename__ = "tariff"
    id = Column(Integer, primary_key=True, index=True)
    tarifeCategorieId = Column(Integer, ForeignKey("tariff_category.id"), nullable=False)
    
    tariff_category = relationship("TariffCategory", back_populates="tariff")
    tariffCells = relationship("TariffCell", back_populates="tariff")
