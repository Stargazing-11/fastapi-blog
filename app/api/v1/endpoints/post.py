from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas import post as post_schema
from app.services import post as post_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user_id():
    # This is a placeholder for the actual implementation of getting the current user's ID
    # You would typically extract this from a JWT or session
    return 1

@router.post("/posts/", response_model=post_schema.Post)
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    db_post = post_service.create_post(db, post, user_id)
    return db_post

@router.get("/posts/", response_model=list[post_schema.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = post_service.get_posts(db, skip, limit)
    return posts

@router.get("/posts/{post_id}", response_model=post_schema.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = post_service.get_post(db, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
