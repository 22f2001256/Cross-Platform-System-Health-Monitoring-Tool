from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, sessionLocal
from sqlalchemy.orm import Session
from models import Base
import schemas
import controllers

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # All headers
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally: 
        db.close()


@app.post('/healthcheck')
def receive_health(report: schemas.HealthCheckIn, db: Session = Depends(get_db)):
    return controllers.create_health_check(db, report)

@app.get('/machines', response_model=list[schemas.MachineOut])
def get_machines(db: Session = Depends(get_db)):
    return controllers.get_all_machines(db)