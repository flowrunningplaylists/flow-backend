from database import engine, Base
from app import app
import uvicorn

# fyi: only creates the tables that are not already present
# if we change the schema, we need to drop the tables first, 
# or use a database migration tool like alembic
Base.metadata.create_all(bind=engine) 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


