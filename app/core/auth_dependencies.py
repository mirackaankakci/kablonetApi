from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from app.core.jwt_manager import JWTManager

# Security scheme for Bearer token
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Dependency to get current authenticated user from JWT token
    
    Args:
        credentials: HTTP Authorization credentials (Bearer token)
        
    Returns:
        dict: Current user data from JWT payload
        
    Raises:
        HTTPException: If token is invalid or expired
    """
    token = credentials.credentials
    
    # Verify token
    payload = JWTManager.verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if token is access token
    if payload.get("type") != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token type",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if token is expired
    if JWTManager.is_token_expired(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return {
        "user_id": int(payload.get("sub")),
        "email": payload.get("email"),
        "role": payload.get("role", "user")
    }

async def get_optional_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)) -> Optional[dict]:
    """
    Optional dependency to get current user (doesn't raise error if no token)
    
    Args:
        credentials: Optional HTTP Authorization credentials
        
    Returns:
        Optional[dict]: Current user data if valid token, None if no token
    """
    if not credentials:
        return None
    
    try:
        return await get_current_user(credentials)
    except HTTPException:
        return None

def require_role(required_role: str):
    """
    Role-based access control decorator
    
    Args:
        required_role (str): Required role for access (e.g., "admin", "moderator")
        
    Returns:
        Dependency function that checks user role
    """
    async def role_checker(current_user: dict = Depends(get_current_user)) -> dict:
        user_role = current_user.get("role", "user")
        
        # Admin can access everything
        if user_role == "admin":
            return current_user
        
        # Check specific role
        if user_role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required role: {required_role}"
            )
        
        return current_user
    
    return role_checker

def require_admin():
    """
    Convenience function to require admin role
    
    Returns:
        Dependency function that checks for admin role
    """
    return require_role("admin")

def require_moderator():
    """
    Convenience function to require moderator role
    
    Returns:
        Dependency function that checks for moderator or admin role
    """
    async def moderator_checker(current_user: dict = Depends(get_current_user)) -> dict:
        user_role = current_user.get("role", "user")
        
        if user_role not in ["admin", "moderator"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access denied. Required role: moderator or admin"
            )
        
        return current_user
    
    return moderator_checker
