from fastapi import FastAPI
from app.api.v1 import main_category_routes
from app.api.v1 import channel_list_routes
from app.api.v1 import campaign_routes
from app.api.v1 import campaign_features_routes
from app.api.v1 import commitment_period_routes
from app.api.v1 import devices_routes
from app.api.v1 import about_contents_routes
from app.api.v1 import campaign_commitment_routes
from app.api.v1 import device_commitment_routes
from app.db.database import engine
from app.db.base import Base

app = FastAPI()

# Tabloları oluştur (ilk çalıştırmada)
Base.metadata.create_all(bind=engine)

app.include_router(main_category_routes.router)
app.include_router(channel_list_routes.router)
app.include_router(campaign_routes.router)
app.include_router(campaign_features_routes.router)
app.include_router(commitment_period_routes.router)
app.include_router(devices_routes.router)
app.include_router(about_contents_routes.router)
app.include_router(campaign_commitment_routes.router)
app.include_router(device_commitment_routes.router)
