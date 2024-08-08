from sqlalchemy.orm import Session 
from app.db import models
from app.schemas import comment as comment_schema

def create_comment(db: Session, comment: comment_schema.CommentCreate, user_id: int, comment_post_id: int) -> models.Comment:
    db_comment = models.Comment(content = comment.content, post_id = comment_post_id, owner_id = user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_post_comments(db: Session, post_id: int, skip:int = 0, limit:int = 10) -> list:
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).offset(skip).limit(limit).all()

def get_user_comments(db: Session, user_id: int, skip:int = 0, limit:int = 10) -> list:
    return db.query(models.Comment).filter(models.Comment.owner_id == user_id).offset(skip).limit(limit).all()

def get_comment(db: Session, comment_id: int, post_id: int) -> list:
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).filter(models.Comment.id == comment_id).first()
