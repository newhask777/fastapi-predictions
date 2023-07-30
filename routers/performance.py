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
    prefix='/performance',
    tags=['performance'],
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


# router by date
@router.get('/federation/{federation}', response_class=HTMLResponse)
async def get_by_date(request: Request, federation: str, db: Session = Depends(get_db)):

    leagues = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).distinct(models.Prediction.competition_cluster)
    
    games = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).all()

    tournamets = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).distinct(models.Prediction.date)

    federations = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).distinct(models.Prediction.federation)

    wons = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).filter(models.Prediction.status == "won").all()
    w_count = len(wons)

    lost = db.query(models.Prediction).filter(models.Prediction.competition_cluster == federation).filter(models.Prediction.status == "lost").all()
    l_count = len(lost)

    odds =  db.query(models.Prediction.odds).filter(models.Prediction.competition_cluster == federation).all()
    predictions =  db.query(models.Prediction.prediction).filter(models.Prediction.competition_cluster == federation).all()
    # print(odds)

    win_coef = []
    lost_coef = []

    count = len(games)

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
        "profit": profit,
        "count": count
        })