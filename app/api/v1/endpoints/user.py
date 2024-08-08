from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas import user as user_schema
from app.services import user as user_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.create_user(db, user)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User already registered")
    return db_user

@router.post("/login/", response_model=user_schema.User)
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = user_service.authenticate_user(db, user.email, user.password)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    return db_user