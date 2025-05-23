from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    email: str
    name: Optional[str] = None
    strava_auth_code: Optional[str] = None
    spotify_auth_code: Optional[str] = None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: str
    password_hash: str
    name: Optional[str] = None
    strava_auth_code: Optional[str] = None
    spotify_auth_code: Optional[str] = None

    