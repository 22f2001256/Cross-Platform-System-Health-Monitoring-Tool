from sqlalchemy.orm import Session
from models import Health,  Machine
from schemas import HealthCheckIn
from datetime import datetime, timezone

def create_health_check(db: Session, report: HealthCheckIn):
    machine = db.query(Machine).filter(Machine.hostname == report.hostname).first()

    if not machine:
        machine = Machine(hostname=report.hostname, os_type = report.os_type)
        db.add(machine)
        db.commit()


    machine.last_check = datetime.now(timezone.utc)

    health_check = Health(
        machine_id = machine.id,
        disk_encrypted = report.disk_encrypted,
        os_up_to_date = report.os_up_to_date,
        antivirus_active = report.antivirus_active,
        inactivity_timeout = report.inactivity_timeout
    )

    db.add(health_check)
    db.commit()
    db.refresh(health_check)

    return machine


def get_all_machines(db: Session):
    return db.query(Machine).all()

