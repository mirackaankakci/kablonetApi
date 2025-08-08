from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class CategoryColumn(Base):
    __tablename__ = "category_column"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("tariff_category.id"), nullable=False)
    tariff_column_id = Column(Integer, ForeignKey("tariff_column.id"), nullable=False)
    tariff_value_id = Column(Integer, ForeignKey("tariff_value.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    add_date = Column(String, nullable=True)
    update_date = Column(String, nullable=True)
    
    tariff_category = relationship("TariffCategory", back_populates="category_columns")
    tariff_column = relationship("TariffColumn", back_populates="category_columns")
    tariff_value = relationship("TariffValue", back_populates="category_columns")