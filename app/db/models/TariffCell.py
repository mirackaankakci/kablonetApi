from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base



class TariffCell(Base):
    __tablename__ = "tariff_cell"
    id = Column(Integer, primary_key=True, index=True)
    tariff_line_id = Column(Integer, ForeignKey("tariff_lines.id"), nullable=False)
    tariff_column_id = Column(Integer, ForeignKey("tariff_column.id"), nullable=False)
    tariff_value_id = Column(Integer, ForeignKey("tariff_value.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    add_date = Column(String, nullable=True)
    update_date = Column(String, nullable=True)
    
    tariff_line = relationship("TariffLine", back_populates="tariff_cells")
    tariff_column = relationship("TariffColumn", back_populates="tariff_cells")
    tariff_value = relationship("TariffValue", back_populates="tariff_cells")