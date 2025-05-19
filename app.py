from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from database import Session, get_db
import crud
import schemas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# TODO: maybe change this to /login
@app.get("/users/{email}", response_model=schemas.User)
def get_user_by_email(email: str):
    with get_db() as db:
        db_user = crud.get_user_by_email(db, email=email)
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user

# TODO: maybe change this to /signup
@app.post("/create-user")
def create_user(user: schemas.UserCreate):
    with get_db() as db:
        try:
            db_user = crud.create_user(db, email=user.email, password_hash=user.password_hash)
        except Exception as e:
            raise HTTPException(status_code=400, detail="User already exists")
        return db_user

# TODO: add endpoint to pull strava activities
