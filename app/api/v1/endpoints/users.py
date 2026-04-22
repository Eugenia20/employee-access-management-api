from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.user import UpdateUserRequest
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])


#  VIEW OWN PROFILE
@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "employee_id": current_user.employee_id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active,
    }


#  UPDATE PROFILE
@router.put("/me")
def update_me(
    data: UpdateUserRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Update full name
    if data.full_name:
        current_user.full_name = data.full_name

    # Update email (must be unique)
    if data.email:
        existing = db.query(User).filter(User.email == data.email).first()
        if existing and existing.id != current_user.id:
            raise HTTPException(status_code=400, detail="Email already in use")

        current_user.email = data.email

    # Update password (secure)
    if data.password:
        current_user.password_hash = hash_password(data.password)

    db.commit()
    db.refresh(current_user)

    return {"message": "Profile updated successfully"}


# DEACTIVATE OWN ACCOUNT
@router.delete("/me")
def deactivate_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    current_user.is_active = False
    db.commit()

    return {"message": "Account deactivated"}