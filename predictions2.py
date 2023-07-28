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

# db.query(models.Prediction).delete()
# db.commit()

today = str(date.today())


url = "https://v3.football.api-sports.io/predictions?fixture=872658"

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "de5706af3e38be4085c43f66097381bc"
}

events = requests.get(url, headers=headers).json()['response']

with open('json/predictions2.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=4)

for event in events:
    pass