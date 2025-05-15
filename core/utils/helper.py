import hashlib
import os 
from datetime import datetime
import pytz
from cryptography.fernet import Fernet
from fastapi import Request, logger
from passlib.context import CryptContext
from slowapi.util import get_remote_address

from config import session_config
from fastapi.encoders import jsonable_encoder

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from apps.v1.api.auth.models.methods.method1 import UserAuthMethod
from apps.v1.api.auth.models.methods.method1 import AdminAuthMethod
from core.utils import message_variable
import base64
from pydantic import EmailStr


class PasswordUtils:
    """This class is used to manage password management"""

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str):
        """
        This function is used to hash password
        Arguments:
            password(str) : password argument of string format.

        Returns:
            Hash of the password
        """
        return self.pwd_context.hash(password)


class EnrytionDecrytionUtils:

    # Initialize Fernet for encryption
    FERNET_KEY = os.getenv(
        "FERNET_KEY", Fernet.generate_key()
    )  # For encrypting session data
    fernet = Fernet(FERNET_KEY)

    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive session data."""
        return self.fernet.encrypt(data.encode()).decode()

    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive session data."""
        return self.fernet.decrypt(encrypted_data.encode()).decode()


class SessionUtils:

    def get_client_ip(self, request: Request) -> str:
        """Retrieve client IP from headers or remote address."""
        return get_remote_address(request)

    def generate_session_id(self, user_agent: str, ip: str) -> str:
        """Generates a session ID bound to user-agent and IP."""
        return hashlib.sha256(
            f"{session_config.SECRET_KEY}{user_agent}{ip}".encode()
        ).hexdigest()


# class DateTimeUtils:

    # def get_time(self):
    #     """Returns current datetime in default timezone India Standard Time"""
    #     timezone = "Asia/Kolkata"
    #     current = datetime.now(pytz.timezone(timezone))

class DateTimeUtils:
    @staticmethod
    def get_time():
        """Returns current datetime in default timezone India Standard Time"""
        timezone = "Asia/Kolkata"
        current = datetime.now(pytz.timezone(timezone))
        return current

#not needed
class decode_data:
    def encode_and_serialize(self,client_object, serializer_class):
        client_data = jsonable_encoder(client_object)
        #client_data = jsonable_encoder(client_object, custom_encoder={datetime: lambda x: x.isoformat()})
        serialized_data = serializer_class().dump(client_data)
        return serialized_data
    

class DecodeImage:
    
    def decode_image(self, profile_image: str) -> bytes:
        if profile_image:
            try:
                # Remove the prefix if it's a data URL (e.g., data:image/png;base64,...)
                if profile_image.startswith("data:image"):
                    profile_image = profile_image.split(",")[1]

                # Decode the Base64-encoded image
                return base64.b64decode(profile_image)
            except Exception as e:
                logger.error(f"Invalid image format: {e}")
                raise HTTPException(status_code=400, detail="Invalid image format")
        return None


class AdminUtils:
    async def get_admin_by_email(self, db: AsyncSession, email: EmailStr, model):
        """Fetches Admin object by email."""
        data_object = await AdminAuthMethod(model).find_by_email(db, email)

        if not data_object:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message_variable.AUTH_EMAIL_NOT_EXISTS,
            )
        return data_object


class DateTimeUtils:
    
    def get_time(self):
        """Returns current datetime in default timezone India Standard Time"""
        timezone = "Asia/Kolkata"
        return datetime.now(pytz.timezone(timezone)).replace(tzinfo=None)
    
class EmailIsAvailable:
    
    async def IsAvailable(self,db: AsyncSession, email: EmailStr, model):
        """Check if an email exists for the given model User."""
        data_object = await UserAuthMethod(model).find_by_email(db, email)
        if not data_object:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message_variable.AUTH_EMAIL_NOT_EXISTS
            )
        return data_object


# class RBACHelper:
#     """Helper methods for RBAC functionality"""
    
#     @staticmethod
#     async def check_user_has_permission(
#         required_permission: str,
#         user_role_id: int,
#         db: AsyncSession
#     ):
#         """
#         Check if a user with a given role has a specific permission
        
#         Args:
#             required_permission (str): The permission name required
#             user_role_id (int): The role ID of the user
#             db (AsyncSession): The database session
        
#         Returns:
#             bool: True if the user has the permission, False otherwise
#         """
#         # Get the permission ID
#         stmt = select(Permission).where(Permission.permission == required_permission)
#         result = await db.execute(stmt)
#         permission = result.scalars().first()
        
#         if not permission:
#             return False
        
#         # Check if the role has this permission
#         stmt = select(RolePermission).where(
#             RolePermission.role_id == user_role_id,
#             RolePermission.permission_id == permission.id
#         )
#         result = await db.execute(stmt)
#         role_permission = result.scalars().first()
        
#         return role_permission is not None
    
#     @staticmethod
#     def permission_required(required_permission: str):
#         """
#         Dependency for checking if a user has a required permission
        
#         Args:
#             required_permission (str): The permission name required
        
#         Returns:
#             function: A dependency that checks if the user has the permission
#         """
#         async def check_permission(
#             db: AsyncSession = Depends(get_db),
#             # This would come from your auth system
#             # In a real implementation, you'd get this from your JWT token or session
#             # For example: user = Depends(get_current_user)
#             user_role_id: int = 1  # Default for testing, replace with actual auth
#         ):
#             has_permission = await RBACHelper.check_user_has_permission(
#                 required_permission, user_role_id, db
#             )
            
#             if not has_permission:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="You don't have permission to perform this action"
#                 )
            
#             return True
        
#         return check_permission
    
#     @staticmethod
#     def role_required(required_roles: List[str]):
#         """
#         Dependency for checking if a user has one of the required roles
        
#         Args:
#             required_roles (List[str]): List of role names, any of which grants access
        
#         Returns:
#             function: A dependency that checks if the user has one of the roles
#         """
#         async def check_role(
#             db: AsyncSession = Depends(get_db),
#             # This would come from your auth system
#             # In a real implementation, you'd get this from your JWT token or session
#             user_role_id: int = 1  # Default for testing, replace with actual auth
#         ):
#             # Get the user's role
#             stmt = select(Role).where(Role.id == user_role_id)
#             result = await db.execute(stmt)
#             role = result.scalars().first()
            
#             if not role or role.role not in required_roles:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="You don't have the required role to perform this action"
#                 )
            
#             return True
        
#         return check_role