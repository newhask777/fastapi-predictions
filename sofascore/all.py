import requests
import json

import sys
sys.path.append("..")
# fastapi
from fastapi import Depends, APIRouter, Request, Form
# db
from db import models
from db.database import SessionLocal, engine
from sqlalchemy.orm import Session

url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2023-06-18"

payload = ""
headers = {
    "authority": "api.sofascore.com",
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl-PL;q=0.6,pl;q=0.5",
    "cache-control": "max-age=0",
    "if-none-match": "W/^\^2c2d5bd32d^^",
    "origin": "https://www.sofascore.com",
    "referer": "https://www.sofascore.com/",
    "sec-ch-ua": "^\^Not.A/Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^114^^, ^\^Google",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers).json()

# print(response)

with open('sofascore/json/all.json', 'w', encoding='utf-8') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:  
        db = SessionLocal()  
        yield db
    finally:
        db.close()

def store_events(response: response['events'], db: Session = Depends(get_db)):
    new_event = models.Event()
    # tournament
    new_event.tournament_name = response.tournament_name
    new_event.tournament_slug = response.tournament_slug
    new_event.tournament_category = response.tournament_category
    new_event.tournament_id = response.tournament_id
    new_event.tournament_flag = response.tournament_flag
    new_event.tournament_unique_id = response.tournament_unique_id
    new_event.tournament_players_stat = response.tournament_players_stat
    # round
    new_event.round = response.round
    new_event.round_name = response.round_name
    # winner
    new_event.winner_code = response.winner_code
    # home_team
    new_event.home_team_name = response.home_team_name
    new_event.home_team_shortname = response.home_team_shortname
    new_event.home_team_code = response.home_team_code
    new_event.home_team_type = response.home_team_type
    new_event.home_team_id = response.home_team_id
    new_event.home_team_country_alpha2 = response.home_team_country_alpha2
    new_event.home_team_country_name = response.home_team_country_name
    new_event.home_team_primary_color = response.home_team_primary_color
    new_event.home_team_secondary = response.home_team_secondary
    new_event.home_team_text = response.home_team_text
    # home_team
    new_event.away_team_name = response.away_team_name
    new_event.away_team_shortname = response.away_team_shortname
    new_event.away_team_users = response.away_team_users
    new_event.away_team_code = response.away_team_code
    new_event.away_team_type = response.away_team_type
    new_event.away_team_id = response.away_team_id
    new_event.away_team_country_alpha2 = response.away_team_country_alpha2
    new_event.away_team_country_name = response.away_team_country_name
    new_event.away_team_primary_color = response.away_team_primary_color
    new_event.away_team_secondary = response.away_team_secondary
    new_event.away_team_text = response.away_team_text
    # stats
    new_event.home_score = response.home_score
    new_event.away_score = response.away_score
    new_event.time = response.time
    new_event.changes = response.changes
    # some
    new_event.has_global_highlights = response.has_global_highlights
    new_event.has_event_players_stat = response.has_event_players_stat
    new_event.has_event_players_heat_map = response.has_event_players_heat_map
    new_event.detailID = response.detailID
    new_event.event_id = response.event_id
    new_event.start_timestamp = response.start_timestamp
    new_event.slug = response.slug
    new_event.final_result_only = response.final_result_only

    db.add(new_event)
    db.commit()

    return 'ok'

