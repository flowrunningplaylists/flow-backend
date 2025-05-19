from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from contextlib import contextmanager
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)  # pass echo=True to print SQL

Session = sessionmaker(bind=engine)

Base = declarative_base()

@contextmanager
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
