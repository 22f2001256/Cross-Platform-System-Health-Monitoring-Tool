from pydantic import BaseModel
from datetime import datetime
from typing import List

class HealthCheckIn(BaseModel):
    disk_encrypted: bool
    os_up_to_date: bool
    antivirus_active: bool
    inactivity_timeout: int 

    class Config:
        orm_mode = True

class MachineOut(BaseModel):
    id: str
    hostname: str
    os_type: str
    last_check : datetime
    healthchecks: List[HealthCheckIn] = []
    
    class Config:
        orm_mode = True