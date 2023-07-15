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

	url = f"https://football-prediction-api.p.rapidapi.com/api/v2/home-last-10/{event_id}"

	headers = {
		"X-RapidAPI-Key": "617e5d6f38mshb3f8fa141064797p178000jsna5d47fa5bb9c",
		"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
	}

	event = requests.get(url, headers=headers).json()
	games.append(event)

	game = models.HomeLast10()
    
	# print(event['data']['stats']['results'])
	try:
		game.event_id = event_id
		game.results = event['data']['stats']['results']
		game.results_as_home_team = event['data']['stats']['results_as_home_team']
		game.results_as_away_team = event['data']['stats']['results_as_away_team']
		game.wins = event['data']['stats']['wins']
		game.draws = event['data']['stats']['draws']
		game.lost = event['data']['stats']['lost']
		game.num_played_as_home_team = event['data']['stats']['num_played_as_home_team']
		game.num_played_as_away_team = event['data']['stats']['num_played_as_away_team']
		game.wins_as_home_team = event['data']['stats']['wins_as_home_team']
		game.draws_as_home_team = event['data']['stats']['draws_as_home_team']
		game.lost_as_home_team = event['data']['stats']['lost_as_home_team']
		game.wins_as_away_team = event['data']['stats']['wins_as_away_team']
		game.draws_as_away_team = event['data']['stats']['draws_as_away_team']
		game.lost_as_away_team = event['data']['stats']['lost_as_away_team']
		game.clean_sheets = event['data']['stats']['clean_sheets']
		game.goals_scored = event['data']['stats']['goals_scored']
		game.goals_scored_first_half = event['data']['stats']['goals_scored_first_half']
		game.goals_scored_second_half = event['data']['stats']['goals_scored_second_half']
		game.goals_scored_as_home_team = event['data']['stats']['goals_scored_as_home_team']
		game.goals_scored_as_away_team = event['data']['stats']['goals_scored_as_away_team']
		game.goals_conceived = event['data']['stats']['goals_conceived']
		game.goals_conceived_first_half = event['data']['stats']['goals_conceived_first_half']
		game.goals_conceived_second_half = event['data']['stats']['goals_conceived_second_half']
		game.goals_conceived_as_home_team = event['data']['stats']['goals_conceived_as_home_team']
		game.goals_conceived_as_away_team = event['data']['stats']['goals_conceived_as_away_team']
		game.over_05 = event['data']['stats']['over_05']
		game.over_15 = event['data']['stats']['over_15']
		game.over_25 = event['data']['stats']['over_25']
		game.over_35 = event['data']['stats']['over_35']
		game.both_teams_scored = event['data']['stats']['both_teams_scored']
		game.encounters = event['data']['encounters']

		db.add(game)
		db.commit()	
	except:
		continue	


with open('json/hl10.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, indent=4, ensure_ascii=False)