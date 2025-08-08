from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "sqlite:///../database/healthmonitor.db"

# Ensure the folder exists
db_path = DATABASE_URL.replace("sqlite:///", "")
db_dir = os.path.dirname(db_path)
os.makedirs(db_dir, exist_ok=True)

engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind = engine, autocommit=False, autoflush=False)
Base = declarative_base()