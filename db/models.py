from sqlalchemy import Boolean, String, Integer, Column, ForeignKey, JSON, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from typing import Dict
import datetime

# ===============================================================================================================================================================================================

# PREDICTIONS
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String(255))
    away_team = Column(String(255))
    event_id = Column(Integer)
    market = Column(String(255))
    competition_name = Column(String(255))
    prediction = Column(String(255))
    competition_cluster = Column(String(255))
    status = Column(String(255))
    federation = Column(String(255))
    is_expired = Column(Boolean)
    season = Column(String(255))
    result = Column(String(255))
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    date = Column(String(255))
    time = Column(String(255))
    last_update_at = Column(String(255))
    odds = Column(JSON)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}



