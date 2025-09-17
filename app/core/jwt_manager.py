from datetime import datetime, timedelta
from typing import Optional, Union, Any
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv()

# JWT Settings
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-fallback-secret-key-for-development")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class JWTManager:
    """JWT Token Management Class"""
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
        """
        Create JWT access token
        
        Args:
            data (dict): Payload data to encode in token
            expires_delta (Optional[timedelta]): Custom expiration time
            
        Returns:
            str: Encoded JWT token
        """
        to_encode = data.copy()
        
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            
        to_encode.update({"exp": expire})
        to_encode.update({"iat": datetime.utcnow()})
        to_encode.update({"type": "access"})
        
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def create_refresh_token(data: dict) -> str:
        """
        Create JWT refresh token (longer expiration)
        
        Args:
            data (dict): Payload data to encode in token
            
        Returns:
            str: Encoded JWT refresh token
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(days=7)  # 7 days for refresh token
        
        to_encode.update({"exp": expire})
        to_encode.update({"iat": datetime.utcnow()})
        to_encode.update({"type": "refresh"})
        
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    @staticmethod
    def verify_token(token: str) -> Optional[dict]:
        """
        Verify and decode JWT token
        
        Args:
            token (str): JWT token to verify
            
        Returns:
            Optional[dict]: Decoded payload if valid, None if invalid
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            return None
    
    @staticmethod
    def extract_user_id(token: str) -> Optional[int]:
        """
        Extract user ID from JWT token
        
        Args:
            token (str): JWT token
            
        Returns:
            Optional[int]: User ID if valid token, None if invalid
        """
        payload = JWTManager.verify_token(token)
        if payload:
            return payload.get("sub")  # "sub" is standard for user identifier
        return None
    
    @staticmethod
    def is_token_expired(token: str) -> bool:
        """
        Check if token is expired
        
        Args:
            token (str): JWT token to check
            
        Returns:
            bool: True if expired, False if valid
        """
        payload = JWTManager.verify_token(token)
        if not payload:
            return True
            
        exp = payload.get("exp")
        if exp is None:
            return True
            
        return datetime.utcnow().timestamp() > exp

class PasswordManager:
    """Password Hashing and Verification Class"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash password using bcrypt
        
        Args:
            password (str): Plain text password
            
        Returns:
            str: Hashed password
        """
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify password against hash
        
        Args:
            plain_password (str): Plain text password
            hashed_password (str): Hashed password from database
            
        Returns:
            bool: True if password matches, False otherwise
        """
        return pwd_context.verify(plain_password, hashed_password)

# Utility Functions
def create_token_response(user_id: int, email: str, role: str = "user") -> dict:
    """
    Create complete token response with access and refresh tokens
    
    Args:
        user_id (int): User ID
        email (str): User email
        role (str): User role/permissions
        
    Returns:
        dict: Token response with access_token, refresh_token, and metadata
    """
    access_token_data = {
        "sub": str(user_id),
        "email": email,
        "role": role
    }
    
    refresh_token_data = {
        "sub": str(user_id),
        "email": email
    }
    
    access_token = JWTManager.create_access_token(access_token_data)
    refresh_token = JWTManager.create_refresh_token(refresh_token_data)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # in seconds
        "user": {
            "id": user_id,
            "email": email,
            "role": role
        }
    }
