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
import json

# define router
router = APIRouter(
    prefix='/home',
    tags=['home'],
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
    games = db.query(models.Prediction).all()

    with open('sofascore/json/all.json', 'r' ,encoding='utf-8') as f:
        games = json.load(f)
    # print(games)

    return templates.TemplateResponse("home.html", {"request": request, "games": games['events']})


