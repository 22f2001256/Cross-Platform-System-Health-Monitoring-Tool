from pydantic import BaseModel
from datetime import datetime

class HealthCheckIn(BaseModel):
    hostname: str
    os_type: str
    disk_encrypted: bool
    os_up_to_date: bool
    antivirus_active: bool
    inactivity_timeout: int

class MachineOut(BaseModel):
    id: str
    hostname: str
    os_type: str
    last_check : datetime