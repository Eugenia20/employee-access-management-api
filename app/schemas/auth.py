from pydantic import BaseModel, EmailStr
from typing import Optional


class RegisterRequest(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: Optional[str] = "user"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"