from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas import user_profile as user_profile_schema
from app.services import user_profile as user_profile_service

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_current_user_id():
    return 1

@router.get("/users/me", response_model=user_profile_schema.UserProfile)
def get_user_profile(db:Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    user = user_profile_service.get_user_profile(db=db, user_id=user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User Note Found")
    return user

@router.put("/users/me", response_model=user_profile_schema.UserProfile)
def updte_user_profile(user_profile: user_profile_schema.UserProfileUpdate, db:Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    user = user_profile_service.update_user_profile(db=db, user_id=user_id, user_profile=user_profile)

    if user is None:
        raise HTTPException(status_code=404, detail="User Note Found")
    return user

