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

    return templates.TemplateResponse("predictions.html", {"request": request, "games": games, "tournamets": tournamets, "leagues": leagues})


# router by date
@router.get('/date/{td}', response_class=HTMLResponse)
async def get_by_date(request: Request, td: str, db: Session = Depends(get_db)):
    
    games = db.query(models.Prediction).filter(models.Prediction.date == td).all()
    tournamets = db.query(models.Prediction).filter(models.Prediction.date == td).distinct(models.Prediction.competition_name)

    return templates.TemplateResponse("predictions.html", {"request": request, "games": games, "tournamets": tournamets})



# get single
@router.get('/{id}', response_class=HTMLResponse)
async def get_game(request: Request, id: int, db: Session = Depends(get_db)):

    game = db.query(models.Prediction).filter(models.Prediction.event_id == id).first()

    h2h = db.query(models.H2H).filter(models.H2H.event_id == id).first()

    hlstat = db.query(models.HomeLeagueStat).filter(models.HomeLeagueStat.event_id == id).first()

    hl10 = db.query(models.HomeLast10).filter(models.HomeLast10.event_id == id).first()

    
    return templates.TemplateResponse("detail.html", {"request": request, "game": game, "h2h": h2h, "hlstat": hlstat, "hl10": hl10})