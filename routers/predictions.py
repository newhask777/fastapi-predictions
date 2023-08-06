import sys
sys.path.append("..")

from starlette import status
from starlette.responses import RedirectResponse

from fastapi import Depends, APIRouter, Request, Form
from db import models
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from datetime import date
import numpy as np
import json

from dao.predictions.Today import Today
from dao.predictions.ByDate import ByDate
from dao.predictions.ByDateFederation import ByDateFederation
from dao.predictions.ByFederation import ByFederation
from dao.predictions.ByCountry import ByCountry

# define router
router = APIRouter(
    prefix='/predictions',
    tags=['predictions'],
    responses={404: {"description": "Not found"}}
)

# database init
models.Base.metadata.create_all(bind=engine)

# enable templates
templates = Jinja2Templates(directory="templates")

# database connection
def get_db():
    try:  
        db = SessionLocal()  
        yield db
    finally:
        db.close()

today = str(date.today())

# router all
@router.get('/', response_class=HTMLResponse)
async def get_all(request: Request, db: Session = Depends(get_db)):

    games = await Today.get_games(request, db)
    leagues = await Today.get_leagues(request, db)
    tournaments = await Today.get_tournaments(request, db)
    federations = await Today.get_federations(request, db)
   
    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournaments,
        "leagues": leagues,
        "federations": federations,
        })


# router by date
@router.get('/date/{dt}', response_class=HTMLResponse)
async def get_by_date(request: Request, dt: str, db: Session = Depends(get_db)):

    games = await ByDate.get_games_by_date(request, dt, db)
    leagues = await ByDate.get_leagues_by_date(request, dt, db)
    tournaments = await ByDate.get_tournaments_by_date(request, dt, db)
    federations = await ByDate.get_federations_by_date(request, dt, db)
    
    games_filtered_19 = []

    for game in games:
        for k, v in game.odds.items():
            if k == game.prediction:
                if v is not None and v > 1.7 and v < 1.8:
                    games_filtered_19.append(game)

    wons = [game for game in games_filtered_19 if game.status == 'won']
    lost = [game for game in games_filtered_19 if game.status == 'lost']

    # wons = [game for game in games if game.status == 'won']
    # lost = [game for game in games if game.status == 'lost']

    w_count = len(wons)
    l_count = len(lost)

    odds =  [game.odds for game in games_filtered_19]

    win_coef = []

    for won in wons:
        # print(won.odds)
        for k, v in won.odds.items():
            if won.prediction == k:
                win_coef.append(v)

    cfplus = sum([c for c in win_coef])

    win_clear = cfplus - w_count
    win_clear = round(win_clear, 2)

    profit = win_clear - l_count
    profit = round(profit, 2)

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        "games": games_filtered_19,
        # "games": games,
        "tournamets": tournaments,
        "leagues": leagues,
        "federations": federations,
        "wons": w_count,
        "lost": l_count,
        "cfplus": win_clear,
        "cfminus": l_count,
        "profit": profit
        })


# router by date and federation
@router.get('/date/{td}/federation/{federation}', response_class=HTMLResponse)
async def get_federation_by_date(request: Request, federation: str, td: str, db: Session = Depends(get_db)):

    games = await ByDateFederation.get_games_by_date_federation(request, federation, td, db)
    leagues = await ByDateFederation.get_leagues_by_date_federation(request, federation, td, db)
    tournaments = await ByDateFederation.get_tournaments_by_date_federation(request, federation, td, db)
    federations = await ByDateFederation.get_federations_by_date_federation(request, federation, td, db)

    wons = await ByDateFederation.get_wons(request, federation, td, db)
    losts = await ByDateFederation.get_losts(request, federation, td, db)
    
    coef_plus = await ByDateFederation.get_win_coef(games)

    win_clear = coef_plus - wons
    profit = win_clear - losts

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        "games": games,
        "tournamets": tournaments,
        "leagues": leagues,
        "federations": federations,
        "wons": wons,
        "lost": losts,
        "cfplus": win_clear,
        "cfminus": losts,
        "profit": profit
        })


# get single
@router.get('/{id}', response_class=HTMLResponse)
async def get_game(request: Request, id: int, db: Session = Depends(get_db)):
    today = str(date.today())


    leagues = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_cluster)
    
    tournamets = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.federation)

    game = db.query(models.Prediction).filter(models.Prediction.event_id == id).first()

    h2h = db.query(models.H2H).filter(models.H2H.event_id == id).first()

    hlstat = db.query(models.HomeLeagueStat).filter(models.HomeLeagueStat.event_id == id).first()

    hl10 = db.query(models.HomeLast10).filter(models.HomeLast10.event_id == id).first()

    
    return templates.TemplateResponse("detail.html", {
        "request": request,
        "game": game,
        "h2h": h2h,
        "hlstat": hlstat,
        "hl10": hl10,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations,
        })


# by country
@router.get('/cluster/{country}', response_class=HTMLResponse)
async def get_game(request: Request, country: str, db: Session = Depends(get_db)):

    games = await ByCountry.get_games_by_country(request, country, db)    
    leagues = await ByCountry.get_leagues_by_country(request, country, db)    
    tournaments = await ByCountry.get_tournaments_by_country(request, country, db)
    federations = await ByCountry.get_federations_by_country(request, country, db)

    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournaments,
        "leagues": leagues,
        "federations": federations
        })


# by federation
@router.get('/federation/{federation}', response_class=HTMLResponse)
async def get_game(request: Request, federation: str, db: Session = Depends(get_db)):
   
    games = await ByFederation.get_games_by_federation(request, federation, db)
    leagues = await ByFederation.get_leagues_by_federation(request, federation, db)
    tournaments = await ByFederation.get_tournaments_by_federation(request, federation, db)
    federations = await ByFederation.get_federations_by_federation(request, federation, db)

    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournaments,
        "leagues": leagues,
        "federations": federations
        })