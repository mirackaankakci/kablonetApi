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
    tariff_category_column_routes,
    auth_routes,
    authorization_examples
)
from app.db.database import engine
from app.db.base import Base

# Import all models to ensure they're registered with Base
from app.db.models.MainCategory import MainCategory  
from app.db.models.User import User

app = FastAPI(
    title="KabloNet API",
    description="KabloNet Platform REST API Documentation",
    version="1.0.0"
)

# Tabloları oluştur (ilk çalıştırmada)
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    """Create database tables on startup"""
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully!")

@app.get("/")
async def root():
    """API ana sayfası"""
    return {
        "message": "🚀 KabloNet API'ye hoş geldiniz!", 
        "version": "1.0.0",
        "docs": "/docs",
        "api_version": "/api/v1"
    }

# Router registrations
app.include_router(auth_routes.router, prefix="/api/v1")
app.include_router(authorization_examples.router, prefix="/api/v1")
app.include_router(main_category_routes.router, prefix="/api/v1")
app.include_router(channel_list_routes.router, prefix="/api/v1")
app.include_router(campaign_routes.router, prefix="/api/v1")
app.include_router(campaign_features_routes.router, prefix="/api/v1")
app.include_router(campaign_commitment_routes.router, prefix="/api/v1")
app.include_router(commitment_period_routes.router, prefix="/api/v1")
app.include_router(devices_routes.router, prefix="/api/v1")
app.include_router(device_commitment_routes.router, prefix="/api/v1")
app.include_router(about_contents_routes.router, prefix="/api/v1")
app.include_router(channels_category_routes.router, prefix="/api/v1")
app.include_router(channels_routes.router, prefix="/api/v1")
app.include_router(packages_category_routes.router, prefix="/api/v1")
app.include_router(packages_channels_routes.router, prefix="/api/v1")
app.include_router(packages_features_routes.router, prefix="/api/v1")
app.include_router(packages_routes.router, prefix="/api/v1")
app.include_router(tariff_category_routes.router, prefix="/api/v1")
app.include_router(tariff_line_routes.router, prefix="/api/v1")
app.include_router(tariff_column_routes.router, prefix="/api/v1")
app.include_router(tariff_cell_routes.router, prefix="/api/v1")
app.include_router(tariff_value_routes.router, prefix="/api/v1")
app.include_router(tariff_category_column_routes.router, prefix="/api/v1")

