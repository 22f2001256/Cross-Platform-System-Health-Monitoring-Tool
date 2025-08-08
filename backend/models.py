from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base

class Machine(Base):
    __tablename__ = "machines"
    id = Column(String, primary_key=True, index=True)
    hostname = Column(String)
    os_type = Column(String)
    last_seen = Column(DateTime, default = datetime.now(timezone.utc))
    reports = relationship("Health", back_populates="machine")

class Health(Base):
    __tablename__ = "health"
    id = Column(Integer, primary_key=True, index=True)
    machine_id = Column(String, ForeignKey("machines.id"))
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    disk_encrypted = Column(Boolean)
    os_up_to_date = Column(Boolean)
    antivirus_active = Column(Boolean)
    inactivity_timeout = Column(Integer)

    machine = relationship("Machine", back_populates="health")

