from fastapi import FastAPI, Depends
from database import engine, sessionLocal
from sqlalchemy.orm import Session
from models import Base
import schemas
import controllers

Base.metadata.create_all(bind=engine)
app = FastAPI()


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