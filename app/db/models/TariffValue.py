from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class TariffValue(Base):
    __tablename__ = "tariff_value"
    id = Column(Integer, primary_key=True, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    isActive = Column(Boolean, unique=False, index=True, nullable=False, default=True)
    add_date = Column(String, nullable=False)
    update_date = Column(String, nullable=False)

    tariff_cells = relationship("TariffCell", back_populates="tariff_value")
    # Removed category_columns relationship to avoid back_populates conflicts
