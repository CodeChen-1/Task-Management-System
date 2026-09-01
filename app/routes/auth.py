from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse, UserUpdate
from app.utils.security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username = user.username,
        email = user.email,
        password_hash = hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid Credentials")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid Credentials")


    access_token = create_access_token(data={"sub": str(db_user.id)})

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/me", response_model=UserResponse)
def update_profile(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update current user's profile"""
    if user_update.username:
        existing = db.query(User).filter(
            User.username == user_update.username,
            User.id != current_user.id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already taken")
        current_user.username = user_update.username

    if user_update.email:
        existing = db.query(User).filter(
            User.email == user_update.email,
            User.id != current_user.id
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already taken")
        current_user.email = user_update.email

    db.commit()
    db.refresh(current_user)
    return current_user