from sqlalchemy import Boolean, String, Integer, Column, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from typing import Dict
import datetime

# ===============================================================================================================================================================================================

# PREDICTIONS
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
    time = Column(String)
    last_update_at = Column(String)
    odds = Column(JSON)


# HEAD TO HEAD
class H2H(Base):
    __tablename__ = "h2hs"
    id = Column(Integer, primary_key=True, index=True)
    
    num_encounters = Column(Integer)
    over_05 = Column(Integer)
    over_15 = Column(Integer)
    over_25 = Column(Integer)
    over_35 = Column(Integer)
    both_teams_scored = Column(Integer)
    total_goals = Column(Integer)
    avg_goals_per_match = Column(Integer)
    # home team
    home_team_name = Column(String)
    home_goals_scored = Column(Integer)
    home_goals_conceived = Column(Integer)
    home_won = Column(Integer)
    home_draw = Column(Integer)
    home_lost = Column(Integer)
    home_clean_sheet = Column(Integer)
    home_first_half_win = Column(Integer)
    home_first_half_draw  = Column(Integer)
    home_first_half_lost = Column(Integer)
    home_avg_goals_scored = Column(Integer)
    home_avg_goals_conceived = Column(Integer)
    home_avg_bookie_win_chance = Column(Integer)
    home_avg_bookie_draw_chance = Column(Integer)
    home_avg_bookie_lose_chance = Column(Integer)
    # away team
    away_team_name = Column(String)
    away_goals_scored = Column(Integer)
    away_goals_conceived = Column(Integer)
    away_won = Column(Integer)
    away_draw = Column(Integer)
    away_lost = Column(Integer)
    away_clean_sheet = Column(Integer)
    away_first_half_win = Column(Integer)
    away_first_half_draw  = Column(Integer)
    away_first_half_lost = Column(Integer)
    away_avg_goals_scored = Column(Integer)
    away_avg_goals_conceived = Column(Integer)
    away_avg_bookie_win_chance = Column(Integer)
    away_avg_bookie_draw_chance = Column(Integer)
    away_avg_bookie_lose_chance = Column(Integer)
    # encounters
    encounters = Column(JSON)



# HOME TEAM LEAGUE STATISTIC
class HomeLeagueStat(Base):
    __tablename__ = "homelstats"
    id = Column(Integer, primary_key=True, index=True)
    team = Column(String)
    matches_played = Column(Integer)
    won = Column(Integer)
    lost = Column(Integer)
    draw = Column(Integer)
    goals_scored = Column(Integer)
    goals_conceived = Column(Integer)
    points = Column(Integer)
    matches_played_as_home_team = Column(Integer)
    won_as_home_team = Column(Integer)
    draw_as_home_team = Column(Integer)
    lost_as_home_team = Column(Integer)
    goals_scored_as_home_team = Column(Integer)
    goals_conceived_as_home_team = Column(Integer)
    points_as_home_team = Column(Integer)


# HOME TEAM LEAGUE LAST 10 GAMES
class HomeLast10(Base):
    __tablename__ = "homel10s"
    id = Column(Integer, primary_key=True, index=True)
    results = Column(String)
    results_as_home_team = Column(String)
    results_as_away_team = Column(String)
    wins = Column(Integer)
    draws = Column(Integer)
    lost = Column(Integer)
    num_played_as_home_team = Column(Integer)
    num_played_as_away_team = Column(Integer)
    wins_as_home_team = Column(Integer)
    draws_as_home_team = Column(Integer)
    lost_as_home_team = Column(Integer)
    wins_as_away_team = Column(Integer)
    draws_as_away_team = Column(Integer)
    lost_as_away_team = Column(Integer)
    clean_sheets = Column(Integer)
    goals_scored = Column(Integer)
    goals_scored_first_half = Column(Integer)
    goals_scored_second_half = Column(Integer)
    goals_scored_as_home_team = Column(Integer)
    goals_scored_as_away_team = Column(Integer)
    goals_conceived = Column(Integer)
    goals_conceived_first_half = Column(Integer)
    goals_conceived_second_half = Column(Integer)
    goals_conceived_as_home_team = Column(Integer)
    goals_conceived_as_away_team = Column(Integer)
    over_05 = Column(Integer)
    over_15 = Column(Integer)
    over_25 = Column(Integer)
    over_35 = Column(Integer)
    both_teams_scored = Column(Integer)



#  AWAY TEAM LEAGUE STATISTIC
# class AwayLeagueStat(Base):
#     pass


# AWAY TEAM LAST 10 GAMES
# class AwayLast10(Base):
#     pass



#====================================================================================================================================================================================

# EVENTS

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
    status = Column(String)
    final_result_only = Column(Boolean)

