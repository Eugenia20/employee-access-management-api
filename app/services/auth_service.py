from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token
from app.utils.employee_id import generate_employee_id


def register_user(db: Session, full_name: str, email: str, password: str, role: str = "user"):
    # Checks if user exists
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise Exception("User already exists")

    # Get last employee_id
    last_user = db.query(User).order_by(User.id.desc()).first()
    last_id = last_user.employee_id if last_user else None

    new_employee_id = generate_employee_id(last_id)

    user = User(
        employee_id=new_employee_id,
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        role=role,
    )
    print("PASSWORD:", password)
    print("BYTES LENGTH:", len(password.encode("utf-8")))

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise Exception("Invalid credentials")

    if not verify_password(password, user.password_hash):
        raise Exception("Invalid credentials")

    if not user.is_active:
        raise Exception("User is deactivated")

    token = create_access_token(
        {
            "user_id": user.id,
            "role": user.role,
        }
    )

    return token