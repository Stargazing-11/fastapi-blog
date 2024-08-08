from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models
from app.utils import jwt
from app.api.v1.dependencies import get_db, get_current_user_id

router = APIRouter()

def get_current_user(token: str = Depends(jwt.verify_token), db: Session = Depends(get_db)):
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.email == token.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.get("/protected")
def read_protected(user: models.User = Depends(get_current_user)):
    return {"message": f"Hello, {user.name}!"}
