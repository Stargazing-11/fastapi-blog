from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models
from app.api.v1.dependencies import admin_required, get_db, get_current_user_id, get_current_user_role

router = APIRouter()

@router.get("/admin/users/", tags=["admin"])
def read_all_users(db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    admin_required(db, user_role=Depends(get_current_user_role))
    return db.query(models.User).all()
