from sqlalchemy.orm import Session
from app.crud.user_crud import UserCRUD
from app.core.jwt_manager import create_token_response
from app.db.models.User import User
from typing import Optional, Dict, Any, List
from fastapi import HTTPException, status

class UserService:
    """User service layer for business logic"""
    
    @staticmethod
    def register_user(db: Session, email: str, password: str, full_name: Optional[str] = None, 
                     phone: Optional[str] = None) -> Dict[str, Any]:
        """Register a new user"""
        try:
            # Validate input
            if len(password) < 6:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Password must be at least 6 characters long"
                )
            
            # Create user
            user = UserCRUD.create_user(
                db=db,
                email=email,
                password=password,
                full_name=full_name,
                phone=phone,
                role="user"
            )
            
            return {
                "success": True,
                "message": "User registered successfully. Please check your email for verification.",
                "data": {
                    "user": user.to_dict(),
                    "verification_required": True
                }
            }
            
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Registration failed"
            )
    
    @staticmethod
    def login_user(db: Session, email: str, password: str) -> Dict[str, Any]:
        """Authenticate user and return tokens"""
        # Authenticate user
        user = UserCRUD.authenticate_user(db, email, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )
        
        # Check if user is verified (optional - remove if not needed)
        # if not user.is_verified:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Please verify your email address first"
        #     )
        
        # Update last login
        UserCRUD.update_last_login(db, user.id)
        
        # Generate tokens
        token_response = create_token_response(
            user_id=user.id,
            email=user.email,
            role=user.role
        )
        
        return token_response
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return UserCRUD.get_user_by_id(db, user_id)
    
    @staticmethod
    def get_user_profile(db: Session, user_id: int) -> Dict[str, Any]:
        """Get user profile"""
        user = UserCRUD.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return {
            "success": True,
            "message": "User profile retrieved successfully",
            "data": user.to_dict()
        }
    
    @staticmethod
    def update_user_profile(db: Session, user_id: int, **kwargs) -> Dict[str, Any]:
        """Update user profile"""
        user = UserCRUD.update_user(db, user_id, **kwargs)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return {
            "success": True,
            "message": "Profile updated successfully",
            "data": user.to_dict()
        }
    
    @staticmethod
    def change_password(db: Session, user_id: int, current_password: str, new_password: str) -> Dict[str, Any]:
        """Change user password"""
        if len(new_password) < 6:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="New password must be at least 6 characters long"
            )
        
        success = UserCRUD.change_password(db, user_id, current_password, new_password)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid current password"
            )
        
        return {
            "success": True,
            "message": "Password changed successfully"
        }
    
    @staticmethod
    def forgot_password(db: Session, email: str) -> Dict[str, Any]:
        """Initiate password reset process"""
        reset_token = UserCRUD.generate_reset_token(db, email)
        if not reset_token:
            # Don't reveal if email exists for security
            pass
        
        return {
            "success": True,
            "message": "If the email exists, a password reset link has been sent."
        }
    
    @staticmethod
    def reset_password(db: Session, token: str, new_password: str) -> Dict[str, Any]:
        """Reset password using token"""
        if len(new_password) < 6:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must be at least 6 characters long"
            )
        
        success = UserCRUD.reset_password(db, token, new_password)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired reset token"
            )
        
        return {
            "success": True,
            "message": "Password reset successfully"
        }
    
    @staticmethod
    def verify_email(db: Session, token: str) -> Dict[str, Any]:
        """Verify user email"""
        success = UserCRUD.verify_email(db, token)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired verification token"
            )
        
        return {
            "success": True,
            "message": "Email verified successfully"
        }
    
    @staticmethod
    def get_users_list(db: Session, skip: int = 0, limit: int = 100, 
                      role: Optional[str] = None, is_active: Optional[bool] = None) -> Dict[str, Any]:
        """Get users list (admin only)"""
        users = UserCRUD.get_users(db, skip, limit, role, is_active)
        
        return {
            "success": True,
            "message": f"Retrieved {len(users)} users",
            "data": {
                "users": [user.to_dict() for user in users],
                "pagination": {
                    "skip": skip,
                    "limit": limit,
                    "count": len(users)
                }
            }
        }
    
    @staticmethod
    def search_users(db: Session, query: str, skip: int = 0, limit: int = 100) -> Dict[str, Any]:
        """Search users (admin only)"""
        users = UserCRUD.search_users(db, query, skip, limit)
        
        return {
            "success": True,
            "message": f"Found {len(users)} users matching '{query}'",
            "data": {
                "users": [user.to_dict() for user in users],
                "search_query": query,
                "pagination": {
                    "skip": skip,
                    "limit": limit,
                    "count": len(users)
                }
            }
        }
