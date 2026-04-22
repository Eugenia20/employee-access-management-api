from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import hashlib
from app.core.config import settings

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#  Hash password
def hash_password(password: str) -> str:
    #  Normalize using SHA-256 (fixed length)
    normalized = hashlib.sha256(password.encode("utf-8")).hexdigest()

    #  Hash with bcrypt
    return pwd_context.hash(normalized)


#  Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    normalized = hashlib.sha256(plain_password.encode("utf-8")).hexdigest()
    return pwd_context.verify(normalized, hashed_password)


#  Create JWT token
def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

    return encoded_jwt