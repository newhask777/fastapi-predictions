from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date

today = str(date.today())


async def get_games(request: Request, db: Session):
  prediction = db.query(Prediction).filter(Prediction.date == today).all()

  if not prediction:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'Predictions not found')
  
  return prediction


async def get_leagues(request: Request, db: Session):
  pass