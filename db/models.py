from sqlalchemy import Boolean, String, Integer, Column, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from typing import Dict
import datetime


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
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    date = Column(String)
    last_update_at = Column(String)
    odds = Column(JSON)

    

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    # tournament
    tournament_name = Column(String)
    tournament_slug = Column(String)
    tournament_category = Column(String)
    tournament_id = Column(Integer, index=True)
    tournament_flag = Column(String)
    tournament_user_count = Column(Integer)
    tournament_unique_id = Column(Integer)
    tournament_players_stat = Column(Boolean)
    # Round
    round = Column(Integer)
    round_name = Column(String)
    # winner
    winner_code = Column(Integer)
    # home team
    home_team_name = Column(String)
    home_team_shortname = Column(String)
    home_team_users = Column(Integer)
    home_team_code = Column(String)
    home_team_type = Column(Integer)
    home_team_id = Column(Integer, index=True)
    home_team_country_alpha2 = Column(String)
    home_team_country_name = Column(String)
    home_team_primary_color = Column(String)
    home_team_secondary = Column(String)
    home_team_text = Column(String)
     # away team
    away_team_name = Column(String)
    away_team_shortname = Column(String)
    away_team_users = Column(Integer)
    away_team_code = Column(String)
    away_team_type = Column(Integer)
    away_team_id = Column(Integer, index=True)
    away_team_country_alpha2 = Column(String)
    away_team_country_name = Column(String)
    away_team_primary_color = Column(String)
    away_team_secondary = Column(String)
    away_team_text = Column(String)
    # stats
    home_score = Column(JSON)
    away_score = Column(JSON)
    time = Column(JSON)
    changes = Column(JSON)
    # some
    has_global_highlights = Column(Boolean)
    has_event_players_stat = Column(Boolean)
    has_event_players_heat_map = Column(Boolean)
    detailID = Column(Integer)
    event_id = Column(Integer, index=True)
    start_timestamp = Column(String)
    date = Column(String)
    time = Column(String)
    slug = Column(String)
    final_result_only = Column(Boolean)

