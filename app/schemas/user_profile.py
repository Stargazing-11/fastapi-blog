from pydantic import BaseModel

class UserProfileBase(BaseModel):
    name: str
    email: str

class UserProfileUpdate(UserProfileBase):
    pass

class UserProfile(UserProfileUpdate):
    id: int

    class Config:
        orm_mode = True