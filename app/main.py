from app.api.v1.main import app
from app.settings.database import engine, SessionLocal  
from app.database.models import User

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
