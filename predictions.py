import requests
import json
from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import models

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market":"classic","iso_date":"2023-07-06","federation":"UEFA"}

headers = {
	"X-RapidAPI-Key": "7ca9a3c5c9mshef5b48845d7690ep19e04bjsn6041fa46a9c8",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

events = requests.get(url, headers=headers, params=querystring).json()

with open('json/predictions.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, indent=4, ensure_ascii=False)

db = SessionLocal() 

db.query(models.Prediction).delete()
db.commit()
  
for event in events["data"]:
	game = models.Prediction()

	game.home_team = event['home_team']
	game.away_team = event['away_team']
	game.event_id = event['id']
	game.market = event['market']
	game.competition_name = event['competition_name']
	game.prediction = event['prediction']
	game.competition_cluster = event['competition_cluster']
	game.status = event['status']
	game.federation = event['federation']
	game.is_expired = event['is_expired']
	game.season = event['season']
	game.result = event['result']
	game.start_date = event['start_date']
	game.last_update_at = event['last_update_at']
	game.odds = event['odds']
        
	db.add(game)
	db.commit()