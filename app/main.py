from fastapi import FastAPI
from app.api.v1.endpoints import user, post, comment, user_profile, admin, auth, protected
from app.db import models, session

app = FastAPI()

models.Base.metadata.create_all(bind=session.engine)

app.include_router(user.router, prefix="/api/v1", tags=["users"])
app.include_router(post.router, prefix="/api/v1", tags=["posts"])
app.include_router(comment.router, prefix="/api/v1", tags=["comments"])
app.include_router(user_profile.router, prefix="/api/v1", tags=["user profiles"])
app.include_router(admin.router, prefix="/api/v1", tags=["admin"])
app.include_router(protected.router, prefix="/api/v1", tags=["protected"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blog!"}
