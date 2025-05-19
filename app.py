from fastapi import FastAPI
from dotenv import load_dotenv
import os
from database import Session, get_db
import crud
import schemas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{email}", response_model=schemas.User)
def get_user_by_email(email: str):
    with get_db() as db:
        db_user = crud.get_user_by_email(db, email=email)
        return db_user

@app.post("/create-user")
def create_user(user: schemas.UserCreate):
    with get_db() as db:
        db_user = crud.create_user(db, email=user.email, password_hash=user.password_hash)
        return db_user
    