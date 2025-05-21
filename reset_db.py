from database import engine, Base
from app import app
import uvicorn

# Running this file will drop all tables and recreate them
# WARNING: This will delete all data in the database
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) 
