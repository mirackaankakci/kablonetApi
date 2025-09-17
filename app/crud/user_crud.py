from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from app.db.models.User import User
from app.core.jwt_manager import PasswordManager
from typing import Optional, List
from datetime import datetime, timedelta
import secrets

class UserCRUD:
    """User CRUD operations"""
    
    @staticmethod
    def create_user(db: Session, email: str, password: str, full_name: Optional[str] = None, 
                   phone: Optional[str] = None, role: str = "user") -> User:
        """Create a new user"""
        # Check if user already exists
        existing_user = UserCRUD.get_user_by_email(db, email)
        if existing_user:
            raise ValueError("User with this email already exists")
        
        # Hash password
        password_hash = PasswordManager.hash_password(password)
        
        # Generate verification token
        verification_token = secrets.token_urlsafe(32)
        verification_expires = datetime.utcnow() + timedelta(hours=24)
        
        # Create user
        user = User(
            email=email,
            password_hash=password_hash,
            full_name=full_name,
            phone=phone,
            role=role,
            verification_token=verification_token,
            verification_token_expires=verification_expires
        )
        
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100, 
                 role: Optional[str] = None, is_active: Optional[bool] = None) -> List[User]:
        """Get users with pagination and filters"""
        query = db.query(User)
        
        if role:
            query = query.filter(User.role == role)
        
        if is_active is not None:
            query = query.filter(User.is_active == is_active)
        
        return query.offset(skip).limit(limit).all()
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        """Authenticate user with email and password"""
        user = UserCRUD.get_user_by_email(db, email)
        if not user:
            return None
        
        if not user.is_active:
            return None
        
        if not PasswordManager.verify_password(password, user.password_hash):
            return None
        
        return user
    
    @staticmethod
    def update_last_login(db: Session, user_id: int) -> Optional[User]:
        """Update user's last login timestamp"""
        user = UserCRUD.get_user_by_id(db, user_id)
        if user:
            user.last_login = datetime.utcnow()
            db.commit()
            db.refresh(user)
        return user
    
    @staticmethod
    def update_user(db: Session, user_id: int, **kwargs) -> Optional[User]:
        """Update user information"""
        user = UserCRUD.get_user_by_id(db, user_id)
        if not user:
            return None
        
        # Update allowed fields
        allowed_fields = ['full_name', 'phone', 'bio', 'avatar_url', 'is_active', 'role']
        for field, value in kwargs.items():
            if field in allowed_fields and hasattr(user, field):
                setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def change_password(db: Session, user_id: int, current_password: str, new_password: str) -> bool:
        """Change user password"""
        user = UserCRUD.get_user_by_id(db, user_id)
        if not user:
            return False
        
        # Verify current password
        if not PasswordManager.verify_password(current_password, user.password_hash):
            return False
        
        # Update password
        user.password_hash = PasswordManager.hash_password(new_password)
        user.updated_at = datetime.utcnow()
        db.commit()
        return True
    
    @staticmethod
    def generate_reset_token(db: Session, email: str) -> Optional[str]:
        """Generate password reset token"""
        user = UserCRUD.get_user_by_email(db, email)
        if not user:
            return None
        
        reset_token = secrets.token_urlsafe(32)
        user.reset_token = reset_token
        user.reset_token_expires = datetime.utcnow() + timedelta(hours=1)
        
        db.commit()
        return reset_token
    
    @staticmethod
    def reset_password(db: Session, token: str, new_password: str) -> bool:
        """Reset password using token"""
        user = db.query(User).filter(
            and_(
                User.reset_token == token,
                User.reset_token_expires > datetime.utcnow()
            )
        ).first()
        
        if not user:
            return False
        
        # Update password and clear reset token
        user.password_hash = PasswordManager.hash_password(new_password)
        user.reset_token = None
        user.reset_token_expires = None
        user.updated_at = datetime.utcnow()
        
        db.commit()
        return True
    
    @staticmethod
    def verify_email(db: Session, token: str) -> bool:
        """Verify user email using token"""
        user = db.query(User).filter(
            and_(
                User.verification_token == token,
                User.verification_token_expires > datetime.utcnow()
            )
        ).first()
        
        if not user:
            return False
        
        # Mark as verified and clear token
        user.is_verified = True
        user.verification_token = None
        user.verification_token_expires = None
        user.updated_at = datetime.utcnow()
        
        db.commit()
        return True
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete user (soft delete - mark as inactive)"""
        user = UserCRUD.get_user_by_id(db, user_id)
        if not user:
            return False
        
        user.is_active = False
        user.updated_at = datetime.utcnow()
        db.commit()
        return True
    
    @staticmethod
    def search_users(db: Session, query: str, skip: int = 0, limit: int = 100) -> List[User]:
        """Search users by email or full name"""
        search_query = f"%{query}%"
        return db.query(User).filter(
            or_(
                User.email.ilike(search_query),
                User.full_name.ilike(search_query)
            )
        ).offset(skip).limit(limit).all()
