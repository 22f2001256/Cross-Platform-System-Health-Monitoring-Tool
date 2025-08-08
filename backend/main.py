from fastapi import FastAPI
from database import engine, sessionLocal
from models import Base



Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()

