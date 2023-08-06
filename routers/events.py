import sys
sys.path.append("..")
# fastapi
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, APIRouter, Request, Form
# db
from db import models
from sqlalchemy import distinct, select, table, inspect

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
# html
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json
import requests

from datetime import date

from dao.events.Today import Today

# define router
router = APIRouter(
    prefix='/events',
    tags=['events'],
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


# router all
@router.get('', response_class=HTMLResponse)
async def get_all(request: Request, db: Session = Depends(get_db)):
    games = await Today.get_games(request, db)
    leagues = await Today.get_leagues(request, db)
    tournaments = await Today.get_tournaments(request, db)
    countries = await Today.get_countries(request, db)
    
    type = 'all'
    temp = 'all'

    return templates.TemplateResponse("events.html",
        {
			"request": request,
			"games": games,
			"tournaments": tournaments,
			"leagues": leagues,
			"countries": countries,
			"type":type,
			"temp": temp
        })


# router by event
@router.get('/event/{id}', response_class=HTMLResponse)
async def get_single(request: Request, id: int, db: Session = Depends(get_db)):
    game = Today.get_detail(request, id, db)

    type = 'game'

    return templates.TemplateResponse("game.html",
        {
			"request": request,
			"game": game,
			"type": type
        })


# router by date
@router.get('/date/{td}', response_class=HTMLResponse)
async def get_by_date(request: Request, td: str, db: Session = Depends(get_db)):
    games = await Today.get_games_by_date(request, td, db)
    tournaments = await Today.get_tournaments_by_date(request, td, db)

    return templates.TemplateResponse("events.html", 
        {
            "request": request,
            "games": games,
            "tournaments": tournaments
        })


# router live all
@router.get('/live', response_class=HTMLResponse)
async def get_all(request: Request, db: Session = Depends(get_db)):

    games = await Today.get_live_games(request, db)
    tournaments = await Today.get_live_tournaments(request, db)
    leagues = await Today.get_live_leagues(request, db)
    countries = await Today.get_live_countries(request, db)
   
    type = 'all'
    temp = 'live'
    
    return templates.TemplateResponse("events.html", {
        "request": request, 
        "games": games, 
        "tournaments": tournaments, 
        "leagues":leagues,
        "countries": countries,
        "type": type,
        "temp": temp
        })

