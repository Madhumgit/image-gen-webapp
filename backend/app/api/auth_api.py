from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.database import SessionLocal
from app.core.models import User
from app.core.auth import hash_password, verify_password, create_access_token, decode_access_token
from pydantic import BaseModel
from typing import Optional
router = APIRouter(prefix="/auth")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username: Optional[str] = None
    email: str
    password: str

@router.post("/register")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        # If email exists, check if password matches
        if verify_password(user.password, existing_user.hashed_password):
            access_token = create_access_token(data={"sub": existing_user.email})
            return {"message": "User already exists — logged in", "access_token": access_token}
        else:
            raise HTTPException(status_code=400, detail="Email already registered with a different password")

    # If user doesn't exist — create new one
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    user_email = decode_access_token(token)
    if not user_email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return {"message": f"Welcome {user_email}!"}
