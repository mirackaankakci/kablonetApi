from fastapi import FastAPI
from app.api.v1 import main_category_routes
from app.api.v1 import kanal_listesi_routes
from app.api.v1 import campaign_routes
from app.api.v1 import tariff_category_routes
from app.db.database import engine
from app.db.base import Base

app = FastAPI()

# Tabloları oluştur (ilk çalıştırmada)
Base.metadata.create_all(bind=engine)

app.include_router(main_category_routes.router)
app.include_router(kanal_listesi_routes.router)
app.include_router(campaign_routes.router)
app.include_router(tariff_category_routes.router)
