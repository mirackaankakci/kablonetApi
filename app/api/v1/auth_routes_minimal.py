from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.schemas.auth_schema import (
    UserRegistrationRequest, UserLoginRequest, TokenResponse, 
    AuthResponse, ChangePasswordRequest, UserProfile, UserUpdateRequest
)
from app.services.user_service import UserService
from app.core.jwt_manager import JWTManager, create_token_response
from app.core.auth_dependencies import get_current_user
from app.core.database_dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=AuthResponse, summary="📝 Register New User")
async def register_user(
    request: UserRegistrationRequest,
    db: Session = Depends(get_db)
):
    """
    Yeni kullanıcı kaydı oluştur.
    
    **Gerekli Alanlar:**
    - email: Geçerli email adresi
    - password: Minimum 6 karakter
    - full_named: Kullanıcının adı soyadı
    - phone: Telefon numarası (opsiyonel)
    """
    return UserService.register_user(
        db=db,
        email=request.email,
        password=request.password,
        full_name=request.full_name,
        phone=request.phone
    )

@router.post("/login", response_model=TokenResponse, summary="🔑 User Login")
async def login_user(
    request: UserLoginRequest,
    db: Session = Depends(get_db)
):
    """
    Kullanıcı girişi yap ve JWT token al.
    
    **Döndürür:**
    - access_token: API doğrulama için (30 dakika)
    - refresh_token: Token yenileme için (7 gün)
    - token_type: Bearer
    """
    # Kullanıcı doğrulama
    user = UserService.authenticate_user(
        db=db,
        email=request.email,
        password=request.password
    )
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Geçersiz email veya şifre"
        )
    
    # Token oluştur
    return create_token_response(user)

@router.get("/me", response_model=AuthResponse, summary="👤 Get Profile")
async def get_current_user_profile(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Mevcut kullanıcının profil bilgilerini getir.
    
    **Gereksinim:** Geçerli JWT access token
    """
    user = UserService.get_user_by_id(db, current_user["user_id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kullanıcı bulunamadı"
        )
    
    return AuthResponse(
        success=True,
        message="Profil başarıyla getirildi",
        user=UserProfile.from_orm(user)
    )

@router.put("/me", response_model=AuthResponse, summary="✏️ Update Profile")
async def update_user_profile(
    request: UserUpdateRequest,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Kullanıcı profilini güncelle.
    
    **Güncellenebilir Alanlar:**
    - full_name: Kullanıcının adı soyadı
    - phone: Telefon numarası
    """
    user = UserService.update_user_profile(
        db=db,
        user_id=current_user["user_id"],
        full_name=request.full_name,
        phone=request.phone
    )
    
    return AuthResponse(
        success=True,
        message="Profil başarıyla güncellendi",
        user=UserProfile.from_orm(user)
    )

@router.post("/change-password", response_model=AuthResponse, summary="🔒 Change Password")
async def change_password(
    request: ChangePasswordRequest,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Kullanıcının şifresini değiştir.
    
    **Gerekli:**
    - current_password: Doğrulama için mevcut şifre
    - new_password: Yeni şifre (minimum 6 karakter)
    """
    success = UserService.change_password(
        db=db,
        user_id=current_user["user_id"],
        current_password=request.current_password,
        new_password=request.new_password
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mevcut şifre yanlış"
        )
    
    return AuthResponse(
        success=True,
        message="Şifre başarıyla değiştirildi"
    )
