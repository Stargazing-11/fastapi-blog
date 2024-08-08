from sqlalchemy.orm import Session
from app.db import models
from app.schemas import user_profile as user_profile_schema

def get_user_profile(db:Session, user_id: int) -> models.User:
    db_user_profile = db.query(models.User).filter(models.User.id == user_id).first()
    return db_user_profile

def update_user_profile(db:Session, user_profile: user_profile_schema.UserProfileUpdate, user_id: int) -> models.User:
    db_user_profile = db.query(models.User).filter(models.User.id == user_id).first()
    
    if db_user_profile:
        db_user_profile.name = user_profile.name
        db_user_profile.email = user_profile.email

        db.commit()
        db.refresh(db_user_profile)
        return db_user_profile
    
    return None