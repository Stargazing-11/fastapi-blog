from pydantic import BaseModel

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentCreate):
    id: int
    post_id: int
    owner_id: int

    class Config:
        orm_mode = True