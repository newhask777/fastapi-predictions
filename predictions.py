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

today = str(date.today())

# db.query(models.Prediction).delete()
# db.query(models.Prediction).filter(models.Prediction.date == "2024-01-01").delete()
# db.query(models.Prediction).filter(models.Prediction.date == today).delete()
# db.commit()

print(today)

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {f"market":"classic","iso_date":{today}}
# querystring = {"market":"classic","iso_date":"2024-01-13"}

headers = {
    # "X-RapidAPI-Key": "42fe1d95e8msh68f2a34f3ade683p172d0ejsn85f061cc437b",
	"X-RapidAPI-Key": "7ca9a3c5c9mshef5b48845d7690ep19e04bjsn6041fa46a9c8",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

events = requests.get(url, headers=headers, params=querystring).json()

with open('json/predictions.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, indent=4, ensure_ascii=False)


  
for event in events["data"]:
        
	dates = event['start_date'].split('T')
	dated = dates[0]
	time = dates[1][:-3]
        
	print(dates)

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
	game.date = dated
	game.time = time
	game.last_update_at = event['last_update_at']
	game.odds = event['odds']
        
	db.add(game)
	db.commit()