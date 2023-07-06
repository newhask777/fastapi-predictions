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
    today = date.today()
    print("Today's date:", today)
    games = db.query(models.Prediction).all()

    tournamets = db.query(models.Prediction).distinct(models.Prediction.competition_name)

    return templates.TemplateResponse("predictions.html", {"request": request, "games": games, "tournamets": tournamets})




# get single
@router.get('/{id}', response_class=HTMLResponse)
async def get_game(request: Request, id: int, db: Session = Depends(get_db)):

    game = db.query(models.Prediction).filter(models.Prediction.id == id).first()
    print(game)

    # call function to make request and save to db
    

    return templates.TemplateResponse("detail.html", {"request": request, "game": game})