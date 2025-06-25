# routers/user_router.py (Fixed)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import schemas
from models import models
from database import database
from utils import utils
from typing import List
from auth.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from main import limiter # FIX: Import the limiter from main.py

router = APIRouter()

# --- User Registration and Management ---
@router.post("/register", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        # FIX: Use a generic error message to prevent user enumeration.
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Could not create user.")

    hashed_password = utils.hash_password(user.password)
    
    # FIX: Create the user object without the role from the request.
    # The role will use the database default 'user', preventing privilege escalation.
    db_user = models.User(
        username=user.username,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# FIX: Add rate limiting to the login endpoint to prevent brute-force attacks.
@router.post("/login", response_model=schemas.Token)
@limiter.limit("5/minute") # Example: 5 login attempts per minute per IP.
def login(request: Request, user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    if not utils.verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.User)
def get_user_me(current_user: schemas.User = Depends(get_current_user)):
    # This endpoint is already secure as it relies solely on the token.
    return current_user
