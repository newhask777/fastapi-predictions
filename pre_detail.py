import requests
import json
from db.database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy.ext.serializer import loads, dumps
from pydantic import BaseModel
from db import models
from datetime import date, datetime
import json

db = SessionLocal() 

events_ids = db.query(models.Prediction.event_id).all()

with open('json/predictions.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

ids = []
for event in events['data']:
    event_id = event['id']
    ids.append(event_id)

print(ids)

games = []

for event_id in ids:

    url = f"https://football-prediction-api.p.rapidapi.com/api/v2/predictions/{event_id}"

    headers = {
        "X-RapidAPI-Key": "7ca9a3c5c9mshef5b48845d7690ep19e04bjsn6041fa46a9c8",
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }

    event = requests.get(url, headers=headers).json()
    games.append(event)

with open('json/event.json', 'w', encoding='utf-8') as f:
    json.dump(games, f, indent=4, ensure_ascii=False)

