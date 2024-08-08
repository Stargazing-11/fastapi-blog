from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_current_user_id():
    # Placeholder function to get the current user's ID
    return 1

def get_current_user_role(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    user = get_current_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user.role

def admin_required(db: Session = Depends(get_db), user_role: str = Depends(get_current_user_role)):
    if user_role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
