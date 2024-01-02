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
@router.get('/predictions',)
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



# router events
@router.get('/events',)
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())
    events = db.query(models.Event).all()

    return events


# router events live
@router.get('/events/live',)
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())
    live = db.query(models.Event).filter(models.Event.status == 'inprogress').filter(models.Event.date == today).all()

    return live


# router events scheduled
@router.get('/events/scheduled',)
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())
    scheduled = db.query(models.Event).filter(models.Event.status == 'notstarted').filter(models.Event.date == today).all()

    return scheduled


# router events scheduled
@router.get('/events/finished',)
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())
    finished = db.query(models.Event).filter(models.Event.status == 'finished').filter(models.Event.date == today).all()

    return finished



# # # router all
# @router.get('/tournamnets',)
# async def get_all(request: Request, db: Session = Depends(get_db)):
#     url = 'https://api.sofascore.com/api/v1/config/unique-tournaments/BY'

#     headers = {
#         "authority": "api.sofascore.com",
#         "accept": "*/*",
#         "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl-PL;q=0.6,pl;q=0.5",
#         "cache-control": "max-age=0",
#         "if-none-match": "W/^\^2c2d5bd32d^^",
#         "origin": "https://www.sofascore.com",
#         "referer": "https://www.sofascore.com/",
#         "sec-ch-ua": "^\^Not.A/Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^114^^, ^\^Google",
#         "sec-ch-ua-mobile": "?0",
#         "sec-ch-ua-platform": "^\^Windows^^",
#         "sec-fetch-dest": "empty",
#         "sec-fetch-mode": "cors",
#         "sec-fetch-site": "same-site",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
#     }

#     response = requests.request("GET", url, headers=headers).json()
#     print(response)

#     return response


