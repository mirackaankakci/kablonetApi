from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class TariffLine(Base):
    __tablename__ = "tariff_lines"
    id = Column(Integer, primary_key=True, index=True)
    # Map to existing DB column (originally created as tariffCategoryId -> stored as lowercase tariffcategoryid in Postgres)
    tariff_category_id = Column("tariffCategoryId", Integer, ForeignKey("tariff_category.id"), nullable=False)
    is_active = Column(Boolean, default=True)

    tariff_category = relationship("TariffCategory", back_populates="tariff_lines")
    tariff_cells = relationship("TariffCell", back_populates="tariff_line")
