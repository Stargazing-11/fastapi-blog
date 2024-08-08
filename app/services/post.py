from sqlalchemy.orm import Session
from app.db import models
from app.schemas import post as post_schema

def create_post(db:Session, post: post_schema.PostCreate, user_id: int) -> models.Post:
    db_post = models.Post(title = post.title, content = post.content, owner_id = user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 10) -> list:
    return db.query(models.Post).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int) -> models.Post:
    return db.query(models.Post).filter(models.Post.id == post_id).first()