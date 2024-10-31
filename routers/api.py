import sys
sys.path.append("..")

# fastapi
from starlette import status
from fastapi import Depends, APIRouter, Request, HTTPException
# db
from db import models
from sqlalchemy import distinct, select, table, inspect

from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

# classes
from dao.predictions.ByDate import ByDate
from dao.statistics.date.DateStats import DateStats
from dao.statistics.date.DateStatsFederation import DateStatsFederation

import json
from datetime import date


# define router
router = APIRouter(
    prefix='/api',
    tags=['api'],
    responses={404: {"description": "Not found"}}
)

# database init
models.Base.metadata.create_all(bind=engine)


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

    predictionsByDate = await ByDate.get_games_by_date(request, dt, db)

    if not predictionsByDate:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Games predictions for {date} not found')
        
    return predictionsByDate


@router.get('/predictions/date/statistic/{dt}')
async def get_statistics_by_date(request: Request, dt: str, db: Session = Depends(get_db)):

    stats = {}
    stats_list = []

    wins = await DateStats.wins_games_count(request, dt, db)
    losts = await DateStats.losts_games_count(request, dt, db)

    fede_wins_uefa = await DateStatsFederation.wins_by_date_uefa(request, dt, db)
    fede_losts_uefa = await DateStatsFederation.losts_by_date_uefa(request, dt, db)

    fede_wins_concacaf = await DateStatsFederation.wins_by_date_concacaf(request, dt, db)
    fede_losts_concacaf = await DateStatsFederation.losts_by_date_concacaf(request, dt, db)

    fede_wins_caf = await DateStatsFederation.wins_by_date_caf(request, dt, db)
    fede_losts_caf = await DateStatsFederation.losts_by_date_caf(request, dt, db)

    fede_wins_afc = await DateStatsFederation.wins_by_date_afc(request, dt, db)
    fede_losts_afc = await DateStatsFederation.losts_by_date_afc(request, dt, db)

    fede_wins_comnebol = await DateStatsFederation.wins_by_date_comnebol(request, dt, db)
    fede_losts_comnebol = await DateStatsFederation.losts_by_date_comnebol(request, dt, db)


    stats['wins'] = wins
    stats['losts'] = losts

    stats['uefa_wins'] = fede_wins_uefa
    stats['uefa_losts'] = fede_losts_uefa

    stats['concacaf_wins'] = fede_wins_concacaf
    stats['concacaf_losts'] = fede_losts_concacaf

    stats['caf_wins'] = fede_wins_caf
    stats['caf_losts'] = fede_losts_caf

    stats['afc_wins'] = fede_wins_afc
    stats['afc_losts'] = fede_losts_afc

    stats['comnebol_wins'] = fede_wins_comnebol
    stats['comnebol_losts'] = fede_losts_comnebol

    stats_list.append(stats)

    # json.dumps(stats_list)

    return stats_list





