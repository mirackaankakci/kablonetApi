"""
🔒 API Yetki Kontrolü Rehberi

Bu dosya farklı endpoint'lerde nasıl yetki kontrolü yapılacağını gösterir.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from app.core.auth_dependencies import get_current_user, require_admin, require_moderator, require_role

router = APIRouter(prefix="/examples", tags=["Authorization Examples"])

# ============================================================================
# 1. PUBLIC ENDPOINT - Herkes Erişebilir
# ============================================================================
@router.get("/public", summary="Public Endpoint (No Auth Required)")
async def public_endpoint():
    """
    Herkes erişebilir - authentication gerekmez.
    
    **Use Cases:**
    - Ana sayfa verileri
    - Ürün katalogları
    - Genel bilgiler
    """
    return {"message": "Bu endpoint herkese açık!"}

# ============================================================================
# 2. AUTHENTICATED ENDPOINT - Giriş Yapmış Kullanıcılar
# ============================================================================
@router.get("/authenticated", summary="Authenticated Users Only")
async def authenticated_endpoint(current_user: dict = Depends(get_current_user)):
    """
    Sadece giriş yapmış kullanıcılar erişebilir.
    
    **Authorization Required:**
    - Valid JWT access token
    - Any role (user, moderator, admin)
    
    **Use Cases:**
    - Kullanıcı profil bilgileri
    - Kişisel veriler
    - Kullanıcıya özel içerik
    """
    return {
        "message": f"Merhaba {current_user['email']}!",
        "user_role": current_user['role'],
        "user_id": current_user['user_id']
    }

# ============================================================================
# 3. ADMIN ONLY - Sadece Admin
# ============================================================================
@router.get("/admin-only", summary="Admin Only Access")
async def admin_only_endpoint(current_user: dict = Depends(require_admin())):
    """
    Sadece admin role'üne sahip kullanıcılar erişebilir.
    
    **Authorization Required:**
    - Valid JWT access token
    - Admin role required
    
    **Use Cases:**
    - Sistem yönetimi
    - Kullanıcı yönetimi
    - Kritik ayarlar
    """
    return {
        "message": "Admin area - sensitive operations allowed",
        "admin_user": current_user['email'],
        "permissions": ["delete_users", "modify_system", "view_all_data"]
    }

# ============================================================================
# 4. MODERATOR OR ADMIN - Moderator veya Admin
# ============================================================================
@router.get("/moderator-access", summary="Moderator or Admin Access")
async def moderator_access_endpoint(current_user: dict = Depends(require_moderator())):
    """
    Moderator veya admin kullanıcılar erişebilir.
    
    **Authorization Required:**
    - Valid JWT access token
    - Moderator or Admin role required
    
    **Use Cases:**
    - İçerik moderasyonu
    - Kullanıcı yönetimi (kısıtlı)
    - Raporlama
    """
    return {
        "message": "Moderator area - content management allowed",
        "user": current_user['email'],
        "role": current_user['role'],
        "permissions": ["moderate_content", "view_reports", "manage_users"]
    }

# ============================================================================
# 5. CUSTOM ROLE - Özel Role
# ============================================================================
@router.get("/premium-content", summary="Premium Users Only")
async def premium_content_endpoint(current_user: dict = Depends(require_role("premium"))):
    """
    Sadece "premium" role'üne sahip kullanıcılar erişebilir.
    
    **Authorization Required:**
    - Valid JWT access token
    - Premium role required
    
    **Use Cases:**
    - Premium içerikler
    - Ücretli özellikler
    - VIP kullanıcı alanları
    """
    return {
        "message": "Premium content unlocked!",
        "premium_user": current_user['email'],
        "exclusive_data": "Special premium features and content"
    }

# ============================================================================
# 6. CONDITIONAL ACCESS - Koşullu Erişim
# ============================================================================
@router.get("/conditional-access", summary="Conditional Access Example")
async def conditional_access_endpoint(current_user: dict = Depends(get_current_user)):
    """
    Kullanıcı rolüne göre farklı veriler döner.
    
    **Authorization Required:**
    - Valid JWT access token
    - Different data based on user role
    """
    user_role = current_user['role']
    
    base_data = {
        "message": "Welcome to the platform!",
        "user": current_user['email']
    }
    
    if user_role == "admin":
        base_data["admin_data"] = "Sensitive admin information"
        base_data["permissions"] = ["all"]
    elif user_role == "moderator":
        base_data["moderator_data"] = "Moderation tools"
        base_data["permissions"] = ["moderate", "view"]
    else:
        base_data["user_data"] = "Standard user content"
        base_data["permissions"] = ["view"]
    
    return base_data

# ============================================================================
# 7. RESOURCE OWNERSHIP - Kaynak Sahipliği
# ============================================================================
@router.get("/my-data/{resource_id}", summary="Resource Ownership Check")
async def resource_ownership_endpoint(
    resource_id: int,
    current_user: dict = Depends(get_current_user)
):
    """
    Kullanıcı sadece kendi verilerine erişebilir.
    
    **Authorization Required:**
    - Valid JWT access token
    - Resource must belong to current user
    
    **Use Cases:**
    - Kişisel dosyalar
    - Kullanıcı siparişleri
    - Özel veriler
    """
    
    # Örnek: Veritabanından resource'u kontrol et
    # resource = get_resource_by_id(resource_id)
    # if resource.user_id != current_user['user_id'] and current_user['role'] != 'admin':
    #     raise HTTPException(status_code=403, detail="Access denied to this resource")
    
    # Simülasyon için basit kontrol
    if resource_id != current_user['user_id'] and current_user['role'] != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own resources"
        )
    
    return {
        "message": f"Resource {resource_id} accessed successfully",
        "owner": current_user['email'],
        "data": f"Private data for resource {resource_id}"
    }

# ============================================================================
# 8. MULTIPLE CONDITIONS - Çoklu Koşullar
# ============================================================================
@router.post("/advanced-operation", summary="Advanced Authorization Example")
async def advanced_operation_endpoint(
    operation_type: str,
    current_user: dict = Depends(get_current_user)
):
    """
    Karmaşık yetki kontrolü örneği.
    
    **Authorization Rules:**
    - 'read': Any authenticated user
    - 'write': Moderator or Admin
    - 'delete': Admin only
    - 'system': Admin with special flag
    """
    
    user_role = current_user['role']
    
    if operation_type == "read":
        # Any authenticated user can read
        pass
    elif operation_type == "write":
        if user_role not in ["moderator", "admin"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Write permission requires moderator or admin role"
            )
    elif operation_type == "delete":
        if user_role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Delete permission requires admin role"
            )
    elif operation_type == "system":
        if user_role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="System operations require admin role"
            )
        # Ek kontrol: Admin'in sistem yetkisi var mı?
        # if not current_user.get('system_access'):
        #     raise HTTPException(status_code=403, detail="System access not granted")
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid operation type"
        )
    
    return {
        "message": f"Operation '{operation_type}' completed successfully",
        "performed_by": current_user['email'],
        "user_role": user_role
    }
