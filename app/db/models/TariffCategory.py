from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base



class TariffCategory(Base):
    __tablename__ = "tariff_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    add_date = Column(String, nullable=True)
    update_date = Column(String, nullable=True)
    important_information = Column(String, nullable=True)
    main_category_id = Column(Integer, ForeignKey("main_category.id"), nullable=True)

    main_category = relationship("MainCategory", back_populates="tariff_categories")
    tariff_lines = relationship("TariffLine", back_populates="tariff_category")
    category_columns = relationship("TariffCategoryColumn", back_populates="tariff_category")
    