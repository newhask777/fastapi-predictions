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


# router all
@router.get('/', response_class=HTMLResponse)
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())

    leagues = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)
  
    games = db.query(models.Prediction).filter(models.Prediction.date == today).all()
    for game in games:
        print(game.as_dict())

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == today).limit(4).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.federation)

    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations,
        })


# router by date
@router.get('/date/{td}', response_class=HTMLResponse)
async def get_by_date(request: Request, td: str, db: Session = Depends(get_db)):

    leagues = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.competition_cluster)

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.federation)
    
    games = db.query(models.Prediction).filter(models.Prediction.date == td).all()

    
    games_filtered_19 = []

    for game in games:
        for k, v in game.odds.items():
            # print(v)
            if k == game.prediction:
                if v is not None and v > 1.7 and v < 1.8:
                    
                    # print(v)
                    games_filtered_19.append(game)

    # print(games_filtered_19)

    wons = [game for game in games_filtered_19 if game.status == 'won']
    lost = [game for game in games_filtered_19 if game.status == 'lost']

    w_count = len(wons)
    l_count = len(lost)

    odds =  [game.odds for game in games_filtered_19]

    win_coef = []

    for won in wons:
        # print(won.odds)
        for k, v in won.odds.items():
            if won.prediction == k:
                win_coef.append(v)

    # for game in games:
    #     for k,v in game.odds.items():
    #         print(k)
    #         if k == game.prediction:
    #             if game.status == 'won':
    #                 print(v)

    #                 win_coef.append(v)

    cfplus = sum([c for c in win_coef])
    # print(win_coef)

    win_clear = cfplus - w_count
    win_clear = round(win_clear, 2)

    profit = win_clear - l_count
    profit = round(profit, 2)

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        # "games": games_filtered_19,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations,
        "wons": w_count,
        "lost": l_count,
        "cfplus": win_clear,
        "cfminus": l_count,
        "profit": profit
        })

# router by date
@router.get('/under/date/{td}', response_class=HTMLResponse)
async def get_under(request: Request, td: str, db: Session = Depends(get_db)):

    games = db.query(models.Prediction)\
        .filter(models.Prediction.date == td)\
        .all()
    
    games_filtered_19 = []

    for game in games:
        for k, v in game.odds.items():
            if k == game.prediction:
                if v >= 1.9:
                    print(game.as_dict())
                    games_filtered_19.append(game)

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.competition_name)

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        "games": games_filtered_19,
        "tournamets": tournamets,
        }) 

# router by date and federation
@router.get('/date/{td}/federation/{federation}', response_class=HTMLResponse)
async def get_federation_by_date(request: Request, federation: str, td: str, db: Session = Depends(get_db)):

    leagues = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).distinct(models.Prediction.competition_cluster)

    games = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).all()

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.federation)

    wons = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).filter(models.Prediction.status == "won").all()
    w_count = len(wons)

    lost = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).filter(models.Prediction.status == "lost").all()
    l_count = len(lost)

    odds =  db.query(models.Prediction.odds).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).all()
    predictions =  db.query(models.Prediction.prediction).filter(models.Prediction.date == td).filter(models.Prediction.federation == federation).all()
    # print(odds)

    win_coef = []
    lost_coef = []

    for game in games:
        for k, v in game.odds.items():
            if k == game.prediction:
                if game.status == 'won':

                    win_coef.append(v)

    cfplus = sum([c for c in win_coef])
    # print(cfplus)

    win_clear = cfplus - w_count

    for game in games:
        for k, v in game.odds.items():
            if k == game.prediction:
                if game.status == 'lost':

                    lost_coef.append(v)

    cfminus = sum([c for c in lost_coef])
    print(cfminus)

    profit = win_clear - l_count

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations,
        "wons": w_count,
        "lost": l_count,
        "cfplus": win_clear,
        "cfminus": l_count,
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
    today = str(date.today())
    
    games = db.query(models.Prediction).filter(models.Prediction.date == today).filter(models.Prediction.competition_cluster == country).all()

    leagues = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

    tournamets = db.query(models.Prediction).filter(models.Prediction.competition_cluster == country).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.federation)

    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations
        })


# by federation
@router.get('/federation/{federation}', response_class=HTMLResponse)
async def get_game(request: Request, federation: str, db: Session = Depends(get_db)):
    today = str(date.today())
    
    games = db.query(models.Prediction).filter(models.Prediction.federation == federation).filter(models.Prediction.date == today).all()

    leagues = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

    tournamets = db.query(models.Prediction).filter(models.Prediction.federation == federation).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.federation)

    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations
        })


    # by federation
@router.get('/month/month', response_class=HTMLResponse)
async def get_game(request: Request, db: Session = Depends(get_db)):

    games = db.query(models.Prediction).all() 

    statuses = []
    wons = []
    loses = []
    pred_1 = []
    for game in games:
        odds = game.odds
        # print(odds)

        

        prediction = game.prediction
        # print(prediction)

        status = game.status
        statuses.append(status)

        if game.status == "won":
            wons.append(game.status)

        if game.status == "lost":
            loses.append(game.status)
        # print(status)
        
    coef_filtered_17_18 = []
    coef_filtered_18_19 = []

    # for game in games:
    #     for k, v in game.odds.items():
    #         # print(v)
    #         if k == game.prediction:
    #             if v is not None and v > 1.7 and v < 1.8:
                    
    #                 # print(v)
    #                 coef_filtered_17_18.append(v)

    # cfplus = sum([c for c in coef_filtered_17_18])

    for game in games:
        for k, v in game.odds.items():
            # print(v)
            if k == game.prediction:
                if v is not None and v > 1.6 and v < 1.7:
                    
                    # print(v)
                    coef_filtered_18_19.append(v)

    cfplus = sum([c for c in coef_filtered_18_19])


    return templates.TemplateResponse("predictions.html", {
        "request": request,
        "games": games,
        "statuses": len(statuses),
        "wons": len(wons),
        "loses": len(loses),
        "pred_1": len(pred_1),
        "cfplus": cfplus
        })