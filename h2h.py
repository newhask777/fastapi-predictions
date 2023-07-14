import requests
import json
from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy.ext.serializer import loads, dumps
from pydantic import BaseModel
from db import models
from datetime import date, datetime
import json



# events_ids = db.query(models.Prediction.event_id).all()

with open('json/predictions.json', 'r', encoding='utf-8') as f:
    predictions = json.load(f)

ids = []
for prediction in predictions['data']:
    prediction_id = prediction['id']
    ids.append(prediction_id)

print(ids)

events = []

db = SessionLocal() 

for id in ids:

    url = f"https://football-prediction-api.p.rapidapi.com/api/v2/head-to-head/{id}"

    headers = {
        "X-RapidAPI-Key": "a056fb72cemshfd977431614cdeep1611c4jsnde64c6399532",
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }

    event = requests.get(url, headers=headers).json()

    # print(game)
    events.append(event)

    game = models.H2H()

    try:
        # print(items['data']['stats']['overall'])
        print(event['data']['stats']['home_team'])
        game.event_id = id
        game.num_encounters = event['data']['stats']['overall']['num_encounters']
        game.over_05 = event['data']['stats']['overall']['over_05']
        game.over_15 = event['data']['stats']['overall']['over_15']
        game.over_25 = event['data']['stats']['overall']['over_25']
        game.over_35 = event['data']['stats']['overall']['over_35']
        game.both_teams_scored = event['data']['stats']['overall']['both_teams_scored']
        game.total_goals = event['data']['stats']['overall']['total_goals']
        game.avg_goals_per_match = event['data']['stats']['overall']['avg_goals_per_match']

        # home team
        game.home_team_name = event['data']['stats']['home_team']['team_name']
        game.home_goals_scored = event['data']['stats']['home_team']['goals_scored']
        game.home_goals_conceived = event['data']['stats']['home_team']['goals_conceived']
        game.home_won = event['data']['stats']['home_team']['won']
        game.home_draw = event['data']['stats']['home_team']['draw']
        game.home_lost = event['data']['stats']['home_team']['lost']
        game.home_clean_sheet = event['data']['stats']['home_team']['clean_sheet']
        game.home_first_half_win = event['data']['stats']['home_team']['first_half_win']
        game.home_first_half_draw  = event['data']['stats']['home_team']['first_half_draw']
        game.home_first_half_lost = event['data']['stats']['home_team']['first_half_lost']
        game.home_avg_goals_scored = event['data']['stats']['home_team']['avg_goals_scored']
        game.home_avg_goals_conceived = event['data']['stats']['home_team']['avg_goals_conceived']
        game.home_avg_bookie_win_chance = event['data']['stats']['home_team']['avg_bookie_win_chance']
        game.home_avg_bookie_draw_chance = event['data']['stats']['home_team']['avg_bookie_draw_chance']
        game.home_avg_bookie_lose_chance = event['data']['stats']['home_team']['avg_bookie_lose_chance']

        # away team
        game.away_team_name = event['data']['stats']['away_team']['team_name']
        game.away_goals_scored = event['data']['stats']['away_team']['goals_scored']
        game.away_goals_conceived = event['data']['stats']['away_team']['goals_conceived']
        game.away_won = event['data']['stats']['away_team']['won']
        game.away_draw = event['data']['stats']['away_team']['draw']
        game.away_lost = event['data']['stats']['away_team']['lost']
        game.away_clean_sheet = event['data']['stats']['away_team']['clean_sheet']
        game.away_first_half_win = event['data']['stats']['away_team']['first_half_win']
        game.away_first_half_draw  = event['data']['stats']['away_team']['first_half_draw']
        game.away_first_half_lost = event['data']['stats']['away_team']['first_half_lost']
        game.away_avg_goals_scored = event['data']['stats']['away_team']['avg_goals_scored']
        game.away_avg_goals_conceived = event['data']['stats']['away_team']['avg_goals_conceived']
        game.away_avg_bookie_win_chance = event['data']['stats']['away_team']['avg_bookie_win_chance']
        game.away_avg_bookie_draw_chance = event['data']['stats']['away_team']['avg_bookie_draw_chance']
        game.away_avg_bookie_lose_chance = event['data']['stats']['away_team']['avg_bookie_lose_chance']

        game.encounters = event['data']['encounters']

        db.add(game)
        db.commit()
    except:
        continue
        
with open('json/h2h.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, indent=4, ensure_ascii=False)