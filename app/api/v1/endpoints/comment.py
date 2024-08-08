from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas import comment as comment_schema
from app.services import comment as comment_service

router = APIRouter()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

def get_current_user_id():
    return 1

@router.post("/posts/{post_id}/comments/", response_model=comment_schema.Comment)
def create_comment(comment:comment_schema.CommentCreate, post_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    db_comment = comment_service.create_comment(db=db, comment=comment, comment_post_id=post_id, user_id=user_id)
    return db_comment

@router.get("/posts/{post_id}/comments/", response_model=list[comment_schema.Comment])
def get_comments(post_id: int,skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comments = comment_service.get_post_comments(db=db, limit=limit, post_id=post_id, skip=skip)
    return comments

@router.get("/posts/{post_id}/comments/{comment_id}", response_model=comment_schema.Comment)
def get_comment(post_id: int,comment_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    comment = comment_service.get_comment(db=db, post_id=post_id, comment_id=comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

