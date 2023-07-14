import requests
import json
from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy.ext.serializer import loads, dumps
from pydantic import BaseModel
from db import models
from datetime import date, datetime
import json


with open('json/predictions.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

ids = []
for event in events['data']:
    event_id = event['id']
    ids.append(event_id)

print(ids)

games = []

db = SessionLocal()

for event_id in ids:

    url = f"https://football-prediction-api.p.rapidapi.com/api/v2/home-league-stats/{event_id}"

    headers = {
        "X-RapidAPI-Key": "b606334c27msh64b0f8f28715854p184c23jsn1a16e1bb37ec",
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }

    event = requests.get(url, headers=headers).json()
    games.append(event)

    game = models.HomeLeagueStat()

    try:
        game.event_id = event_id
        game.team = event['data']['team']
        game.matches_played = event['data']['matches_played']
        game.won = event['data']['won']
        game.lost = event['data']['draw']
        game.draw = event['data']['lost']
        game.goals_scored = event['data']['goals_scored']
        game.goals_conceived = event['data']['goals_conceived']
        game.points = event['data']['points']
        game.matches_played_as_home_team = event['data']['matches_played_as_home_team']
        game.won_as_home_team = event['data']['won_as_home_team']
        game.draw_as_home_team = event['data']['draw_as_home_team']
        game.lost_as_home_team = event['data']['lost_as_home_team']
        game.goals_scored_as_home_team = event['data']['goals_scored_as_home_team']
        game.goals_conceived_as_home_team = event['data']['goals_conceived_as_home_team']
        game.points_as_home_team = event['data']['points_as_home_team']

        db.add(game)
        db.commit()
    except:
        continue