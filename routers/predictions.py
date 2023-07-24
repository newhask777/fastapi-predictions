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

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == today).distinct(models.Prediction.competition_name)

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
    
    games = db.query(models.Prediction).filter(models.Prediction.date == td).all()

    tournamets = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.competition_name)

    federations = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.federation)

    wons = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.status == "won").all()
    w_count = len(wons)

    lost = db.query(models.Prediction).filter(models.Prediction.date == td).filter(models.Prediction.status == "lost").all()
    l_count = len(lost)

    odds =  db.query(models.Prediction.odds).filter(models.Prediction.date == td).all()
    predictions =  db.query(models.Prediction.prediction).filter(models.Prediction.date == td).all()
    # print(odds)

    return templates.TemplateResponse("pred-date.html", {
        "request": request,
        "games": games,
        "tournamets": tournamets,
        "leagues": leagues,
        "federations": federations,
        "wons": w_count,
        "lost": l_count
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

    return templates.TemplateResponse("pred-date.html", {
            "request": request,
            "games": games,
            "tournamets": tournamets,
            "leagues": leagues,
            "federations": federations,
            "wons": w_count,
            "lost": l_count
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