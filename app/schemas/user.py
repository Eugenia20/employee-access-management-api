from pydantic import BaseModel, EmailStr
from typing import Optional


class UpdateUserRequest(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None