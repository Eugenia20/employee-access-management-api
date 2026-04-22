from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import register_user, login_user
from app.api.v1.deps import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = register_user(db, data.full_name, data.email, data.password, data.role)
        return {"message": "User created", "employee_id": user.employee_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        token = login_user(db, data.email, data.password)
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))



@router.post("/logout")
def logout():
    return {"message": "Logout successful"}