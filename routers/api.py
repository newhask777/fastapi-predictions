import sys
sys.path.append("..")
# fastapi
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, APIRouter, Request, Form, HTTPException, status, Request
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

from dao.predictions.ByDate import ByDate
from dao.statistics.Today.Today import Today

from datetime import date

from datetime import date
import time


# define router
router = APIRouter(
    prefix='/api',
    tags=['api'],
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

    

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


# router predictions
@router.get('/predictions')
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())

    predictions = db.query(models.Prediction).filter(models.Prediction.date == today).all()
  
    return predictions


# router predictions by date
@router.get('/predictions/date/{dt}',)
async def get_games_by_date(request: Request, dt: str, db: Session = Depends(get_db)):
    # predictionsByDate = db.query(models.Prediction).filter(models.Prediction.date == dt).all()

    predictionsByDate = await ByDate.get_games_by_date(request, dt, db)

    if not predictionsByDate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Games predictions for {date} not found')
        
    return predictionsByDate


@router.get('/predictions/date/statistic/{dt}')
async def get_statistics_by_date(request: Request, dt: str, db: Session = Depends(get_db)):

    stats = {}

    wins = await Today.wins_games_count(request, dt, db)
    losts = await Today.losts_games_count(request, dt, db)

    fede_wins_uefa = await Today.wins_by_date_uefa(request, dt, db)
    fede_losts_uefa = await Today.losts_by_date_uefa(request, dt, db)

    fede_wins_concacaf = await Today.wins_by_date_concacaf(request, dt, db)
    fede_losts_concacaf = await Today.losts_by_date_concacaf(request, dt, db)

    fede_wins_caf = await Today.wins_by_date_caf(request, dt, db)
    fede_losts_caf = await Today.losts_by_date_caf(request, dt, db)



    # if not wins:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #     detail=f'Games predictions for {date} not found')

    stats['wins'] = wins
    stats['losts'] = losts

    stats['uefa_wins'] = fede_wins_uefa
    stats['uefa_losts'] = fede_losts_uefa

    stats['concacaf_wins'] = fede_wins_concacaf
    stats['concacaf_losts'] = fede_losts_concacaf

    stats['caf_wins'] = fede_wins_caf
    stats['caf_losts'] = fede_losts_caf

    return stats





