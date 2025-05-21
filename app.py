from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import requests
from fastapi.middleware.cors import CORSMiddleware
from database import Session, get_db
import crud
import schemas

load_dotenv()
CLIENT_ID_STRAVA = os.getenv('CLIENT_ID_STRAVA')
CLIENT_SECRET_STRAVA = os.getenv('CLIENT_SECRET_STRAVA')
TOKEN_URL_STRAVA = "https://www.strava.com/oauth/token"


app = FastAPI()

origins = [
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],         # Allow all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

### strava and spotify auth endpoints ###
@app.post("/strava/token")
def get_strava_tokens(data: schemas.StravaAuthRequest):
    token_params = {
        'client_id': CLIENT_ID_STRAVA,
        'client_secret': CLIENT_SECRET_STRAVA,
        'code': data.code,
        'grant_type': 'authorization_code'
    }

    res = requests.post(TOKEN_URL_STRAVA, data=token_params)
    if not res.ok:
        raise HTTPException(status_code=res.status_code, detail="Failed to fetch Strava tokens")
    
    tokens = res.json()
    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token')

    print(f"Email: {data.email}, Access token: {access_token}, Refresh token: {refresh_token}")

    try:
        with get_db() as db:
            updated_user = crud.update_user(
                db=db, 
                email=data.email, 
                strava_access_token=access_token, 
                strava_refresh_token=refresh_token
            )
            if updated_user is None:
                raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    # Return access token only if needed (optional)
    return {"status": "success"}

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

# TODO: add endpoint to pull strava activities by user

