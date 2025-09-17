from pydantic import BaseModel, EmailStr, Field, validator, ConfigDict
from typing import Optional
from datetime import datetime

class UserRegistrationRequest(BaseModel):
    """Request model for user registration"""
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=6, description="User password")
    full_name: Optional[str] = Field(None, max_length=100, description="User full name")
    phone: Optional[str] = Field(None, max_length=20, description="User phone number")
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class UserLoginRequest(BaseModel):
    """Request model for user login"""
    email: EmailStr = Field(..., description="User email address")
    password: str = Field(..., min_length=6, description="User password")

class TokenResponse(BaseModel):
    """Response model for successful authentication"""
    access_token: str = Field(..., description="JWT access token")
    refresh_token: str = Field(..., description="JWT refresh token for renewal")
    token_type: str = Field(default="bearer", description="Token type")
    expires_in: int = Field(..., description="Token expiration time in seconds")
    user: "UserInfo" = Field(..., description="User information")

class UserInfo(BaseModel):
    """User information included in token response"""
    id: int = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User email")
    role: str = Field(default="user", description="User role")

class RefreshTokenRequest(BaseModel):
    """Request model for token refresh"""
    refresh_token: str = Field(..., description="Refresh token")

class ChangePasswordRequest(BaseModel):
    """Request model for password change"""
    current_password: str = Field(..., min_length=6, description="Current password")
    new_password: str = Field(..., min_length=6, description="New password")
    
    @validator('new_password')
    def validate_new_password(cls, v):
        if len(v) < 6:
            raise ValueError('New password must be at least 6 characters long')
        return v

class ForgotPasswordRequest(BaseModel):
    """Request model for forgot password"""
    email: EmailStr = Field(..., description="User email address")

class ResetPasswordRequest(BaseModel):
    """Request model for password reset"""
    token: str = Field(..., description="Password reset token")
    new_password: str = Field(..., min_length=6, description="New password")
    
    @validator('new_password')
    def validate_new_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class EmailVerificationRequest(BaseModel):
    """Request model for email verification"""
    token: str = Field(..., description="Email verification token")

class UserProfile(BaseModel):
    """User profile response model"""
    model_config = ConfigDict(from_attributes=True)
    
    id: int = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User email")
    full_name: Optional[str] = Field(None, description="User full name")
    phone: Optional[str] = Field(None, description="User phone number")
    role: str = Field(..., description="User role")
    is_active: bool = Field(..., description="User active status")
    is_verified: bool = Field(..., description="Email verification status")
    created_at: datetime = Field(..., description="Account creation date")
    last_login: Optional[datetime] = Field(None, description="Last login date")

class UserUpdateRequest(BaseModel):
    """Request model for user profile update"""
    full_name: Optional[str] = Field(None, max_length=100, description="User full name")
    phone: Optional[str] = Field(None, max_length=20, description="User phone number")
    bio: Optional[str] = Field(None, max_length=500, description="User biography")
    avatar_url: Optional[str] = Field(None, max_length=500, description="User avatar URL")

class UserListResponse(BaseModel):
    """Response model for user list (admin only)"""
    success: bool = Field(..., description="Operation success status")
    message: str = Field(..., description="Response message")
    data: "UserListData" = Field(..., description="User list data")

class UserListData(BaseModel):
    """User list data structure"""
    users: list[UserProfile] = Field(..., description="List of users")
    pagination: "PaginationInfo" = Field(..., description="Pagination information")

class PaginationInfo(BaseModel):
    """Pagination information"""
    skip: int = Field(..., description="Number of skipped records")
    limit: int = Field(..., description="Maximum number of records")
    count: int = Field(..., description="Number of returned records")

class AuthResponse(BaseModel):
    """Generic authentication response"""
    success: bool = Field(..., description="Operation success status")
    message: str = Field(..., description="Response message")
    data: Optional[dict] = Field(None, description="Additional response data")

# Update forward references
TokenResponse.model_rebuild()
UserListResponse.model_rebuild()
