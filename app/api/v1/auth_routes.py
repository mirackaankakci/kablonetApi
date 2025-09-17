from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy.orm import Session
from app.schemas.auth_schema import (
    UserRegistrationRequest, UserLoginRequest, TokenResponse, 
    AuthResponse, ChangePasswordRequest, UserProfile, UserUpdateRequest
)
from app.services.user_service import UserService
from app.core.jwt_manager import JWTManager, create_token_response
from app.core.auth_dependencies import get_current_user, require_admin
from app.core.database_dependencies import get_db
from app.db.models.User import User

router = APIRouter(prefix="/auth", tags=["🔐Authentication"])

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
    - full_name: Kullanıcının adı soyadı
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
    return UserService.login_user(
        db=db,
        email=request.email,
        password=request.password
    )

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

@router.get("/debug-token", summary="🔍 Debug Token")
async def debug_token(
    current_user: dict = Depends(get_current_user)
):
    """
    Debug endpoint to check token contents
    """
    return {
        "token_valid": True,
        "user_data": current_user,
        "message": "Token is working correctly"
    }

@router.get("/users", summary="👥 List All Users (Admin Only)")
async def list_users(
    current_user: dict = Depends(require_admin()),
    db: Session = Depends(get_db)
):
    """
    Tüm kullanıcıları listele (Sadece Admin).
    
    **Admin Yetkisi Gerekli**
    """
    users = db.query(User).all()
    return {
        "success": True,
        "message": f"Toplam {len(users)} kullanıcı bulundu",
        "users": [
            {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
                "role": user.role,
                "is_active": user.is_active,
                "created_at": user.created_at
            }
            for user in users
        ]
    }

@router.put("/users/{user_id}/role", summary="👑 Change User Role (Admin Only)")
async def change_user_role(
    user_id: int,
    new_role: str = Query(..., description="New role: user, moderator, admin"),
    current_user: dict = Depends(require_admin()),
    db: Session = Depends(get_db)
):
    """
    Kullanıcının rolünü değiştir (Sadece Admin).
    
    **Kullanılabilir Roller:**
    - user: Standart kullanıcı
    - moderator: Moderatör yetkisi
    - admin: Tam yetki
    
    **Admin Yetkisi Gerekli**
    """
    # Geçerli roller kontrolü
    valid_roles = ["user", "moderator", "admin"]
    if new_role not in valid_roles:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Geçersiz rol. Geçerli roller: {', '.join(valid_roles)}"
        )
    
    # Kullanıcıyı bul
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kullanıcı bulunamadı"
        )
    
    # Kendi rolünü değiştirmeyi engelle
    if user.id == current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kendi rolünüzü değiştiremezsiniz"
        )
    
    old_role = user.role
    user.role = new_role
    db.commit()
    
    return {
        "success": True,
        "message": f"Kullanıcı rolü '{old_role}' → '{new_role}' olarak değiştirildi",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "old_role": old_role,
            "new_role": new_role
        }
    }

@router.post("/users/{user_id}/activate", summary="✅ Activate User (Admin Only)")
async def activate_user(
    user_id: int,
    current_user: dict = Depends(require_admin()),
    db: Session = Depends(get_db)
):
    """
    Kullanıcıyı aktif hale getir (Sadece Admin).
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kullanıcı bulunamadı"
        )
    
    user.is_active = True
    db.commit()
    
    return {
        "success": True,
        "message": f"Kullanıcı {user.email} aktif hale getirildi"
    }

@router.post("/users/{user_id}/deactivate", summary="❌ Deactivate User (Admin Only)")
async def deactivate_user(
    user_id: int,
    current_user: dict = Depends(require_admin()),
    db: Session = Depends(get_db)
):
    """
    Kullanıcıyı pasif hale getir (Sadece Admin).
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Kullanıcı bulunamadı"
        )
    
    # Kendi hesabını deaktive etmeyi engelle
    if user.id == current_user["user_id"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Kendi hesabınızı deaktive edemezsiniz"
        )
    
    user.is_active = False
    db.commit()
    
    return {
        "success": True,
        "message": f"Kullanıcı {user.email} pasif hale getirildi"
    }
