from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from pathlib import Path
import os
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'),os.getenv('DB_NAME'))

engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
 