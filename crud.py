from models import *

### User model ###

def create_user(db, email: str, password_hash: str):
    db_user = User(email=email, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(
        db, 
        id: int, 
        email: str = None, 
        password_hash: str = None,
        name: str = None,
        strava_auth_code: str = None,
        strava_access_token: str = None,
    ):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise Exception("User not found")
    if name:
        user.name = name
    if password_hash:
        user.password_hash = password_hash
    if email:
        user.email = email
    if strava_auth_code:
        user.strava_auth_code = strava_auth_code
    if strava_access_token:
        user.strava_access_token = strava_access_token
    db.commit()
    db.refresh(user)
    return user

def delete_user(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise Exception("User not found")
    db.delete(user)
    db.commit()
    return user

### Activity model ###
def create_activity(
        db, 
        user_id: int, 
        distance: float, 
        moving_time: float, 
        name: str = None
    ):
    db_activity = Activity(user_id=user_id, distance=distance, moving_time=moving_time, name=name)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def get_activity(db, activity_id: int):
    return db.query(Activity).filter(Activity.id == activity_id).first()

def get_activities(db, skip: int = 0, limit: int = 100):
    return db.query(Activity).offset(skip).limit(limit).all()

def get_activities_by_user(db, user_id: int):
    return db.query(Activity).filter(Activity.user_id == user_id).all()
