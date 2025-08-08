from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class TariffColumn(Base):
    __tablename__ = "tariff_column"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    number = Column(Integer, nullable=False)
    add_date = Column(String, nullable=True) 
    update_date = Column(String, nullable=True)

    category_columns = relationship("CategoryColumn", back_populates="tariff_column")
    tariff_cells = relationship("TariffCell", back_populates="tariff_column")


