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

# define router
router = APIRouter(
    prefix='/country',
    tags=['country'],
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
@router.get('/{id}', response_class=HTMLResponse)
async def get_all(request: Request, id: int, db: Session = Depends(get_db)):
    today = str(date.today())

    leagues = db.query(models.Event).filter(models.Event.date == today).distinct(models.Event.tournament_name)
    
    league_games = db.query(models.Event).filter(models.Event.tournament_id == id).filter(models.Event.date == today).all()

    tournaments = db.query(models.Event).filter(models.Event.tournament_id == id).filter(models.Event.date == today).distinct(models.Event.tournament_name)
    
    countries = db.query(models.Event).filter(models.Event.date == today).distinct(models.Event.tournament_category)

    return templates.TemplateResponse("country.html", {
        "request": request,
        "league_games": league_games,
        "tournaments": tournaments,
        "leagues": leagues,
        "countries": countries
        })