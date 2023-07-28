import requests
import json
from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import models
from datetime import date, datetime
from datetime import datetime, date
import time

db = SessionLocal() 

db.query(models.Prediction).delete()
db.commit()

url = "https://v3.football.api-sports.io/fixtures"

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "de5706af3e38be4085c43f66097381bc"
}

params ={
    'date': '2023-07-28'
}

events = requests.get(url, headers=headers, params=params).json()['response']

with open('json/fixtures2.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=4)

for event in events:
    print(event)

    game = models.Event2()
    game.event_id = event['fixture']['id']
    game.referee = event['fixture']['referee']
    game.timezone = event['fixture']['timezone']
    game.date = event['fixture']['date']
    game.periods = event['fixture']['periods']
    game.venue = event['fixture']['venue']
    game.status = event['fixture']['status']
    # League
    game.league_id = event['league']['id']
    game.league_name = event['league']['name']
    game.league_country = event['league']['country']
    game.league_logo = event['league']['logo']   
    game.league_flag = event['league']['flag'] 
    game.league_season = event['league']['season']
    game.league_round = event['league']['round'] 
    # Teams
    # home team
    game.home_team_id = event['teams']['home']['id']
    game.home_team_name = event['teams']['home']['name']
    game.home_team_logo = event['teams']['home']['logo']
    game.home_team_winner = event['teams']['home']['winner']
    # away team
    game.away_team_id = event['teams']['away']['id']
    game.away_team_name = event['teams']['away']['name']
    game.away_team_logo = event['teams']['away']['logo']
    game.away_team_winner = event['teams']['away']['winner']
    # goals
    game.home_goals = event['goals']['home']
    game.away_goals = event['goals']['away']
    # score
    game.halftime_score = event['score']['halftime']
    game.fulltime_score = event['score']['fulltime']
    game.extratime_score = event['score']['extratime']
    game.penalty = event['score']['penalty']

    db.add(game)
    db.commit()
    

