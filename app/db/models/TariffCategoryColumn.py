from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from app.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .TariffCategory import TariffCategory
    from .TariffColumn import TariffColumn


class TariffCategoryColumn(Base):
    __tablename__ = "category_column"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("tariff_category.id"), nullable=False)
    tariff_column_id = Column(Integer, ForeignKey("tariff_column.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    add_date = Column(String, nullable=True)
    update_date = Column(String, nullable=True)
    
    tariff_category: Mapped["TariffCategory"] = relationship("TariffCategory", back_populates="category_columns")
    tariff_column: Mapped["TariffColumn"] = relationship("TariffColumn", back_populates="category_columns")