from sqlalchemy import Boolean, String, Integer, Column, ForeignKey, JSON
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from typing import Dict



class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String)
    away_team = Column(String)
    event_id = Column(Integer)
    market = Column(String)
    competition_name = Column(String)
    prediction = Column(String)
    competition_cluster = Column(String)
    status = Column(String)
    federation = Column(String)
    is_expired = Column(Boolean)
    season = Column(String)
    result = Column(String)
    start_date = Column(String)
    last_update_at = Column(String)
    odds = Column(JSON)

    

class Detail(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True, index=True)