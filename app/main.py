from fastapi import FastAPI
from app.api.v1 import (
    main_category_routes,
    channel_list_routes,
    campaign_routes,
    campaign_features_routes,
    campaign_commitment_routes,
    commitment_period_routes,
    devices_routes,
    device_commitment_routes,
    about_contents_routes,
    tariff_category_routes,
    channels_category_routes,
    channels_routes,
    packages_category_routes,
    packages_channels_routes,
    packages_features_routes,
    packages_routes,
    tariff_line_routes,
    tariff_column_routes,
    tariff_cell_routes,
    tariff_value_routes,
    tariff_category_column_routes

)
from app.db.database import engine
from app.db.base import Base

app = FastAPI()

# Tabloları oluştur (ilk çalıştırmada)
Base.metadata.create_all(bind=engine)

# Router registrations
app.include_router(main_category_routes.router)
app.include_router(channel_list_routes.router)
app.include_router(campaign_routes.router)
app.include_router(campaign_features_routes.router)
app.include_router(campaign_commitment_routes.router)
app.include_router(commitment_period_routes.router)
app.include_router(devices_routes.router)
app.include_router(device_commitment_routes.router)
app.include_router(about_contents_routes.router)
app.include_router(tariff_category_routes.router)
app.include_router(channels_category_routes.router)
app.include_router(channels_routes.router)
app.include_router(packages_category_routes.router)
app.include_router(packages_channels_routes.router)
app.include_router(packages_features_routes.router)
app.include_router(packages_routes.router)
app.include_router(tariff_line_routes.router)
app.include_router(tariff_column_routes.router)
app.include_router(tariff_cell_routes.router)
app.include_router(tariff_value_routes.router)
app.include_router(tariff_category_column_routes.router)
