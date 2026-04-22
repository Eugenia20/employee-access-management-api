from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.deps import require_admin, get_db
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users")
def get_all_users(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    offset = (page - 1) * limit

    users = db.query(User).offset(offset).limit(limit).all()
    total = db.query(User).count()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "data": users,
    }


@router.patch("/users/{employee_id}/activate")
def activate_user(
    employee_id: str,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = db.query(User).filter(User.employee_id == employee_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = True
    db.commit()

    return {"message": "User activated"}


@router.patch("/users/{employee_id}/deactivate")
def deactivate_user(
    employee_id: str,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = db.query(User).filter(User.employee_id == employee_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = False
    db.commit()

    return {"message": "User deactivated"}


@router.get("/users/{employee_id}")
def get_user(
    employee_id: str,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = db.query(User).filter(User.employee_id == employee_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.delete("/users/{employee_id}")
def delete_user(
    employee_id: str,
    db: Session = Depends(get_db),
    admin: User = Depends(require_admin),
):
    user = db.query(User).filter(User.employee_id == employee_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = False
    db.commit()

    return {"message": "User soft deleted"}