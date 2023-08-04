from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class Today:

    today = str(date.today())

    '''
    TODAY ALL GAMES
    '''
    @classmethod
    async def get_games(cls, request: Request, db: Session):
        games = db.query(Prediction).filter(Prediction.date == cls.today).all()

        for game in games:
            print(game.as_dict())

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Predictions not found')
        
        return games


    '''
    TODAY ALL LEAGUES
    '''
    @classmethod
    async def get_leagues(cls, request: Request, db: Session):
        leagues = db.query(Prediction).filter(Prediction.date == cls.today).distinct(Prediction.competition_name)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues not found')
        
        return leagues


    '''
    TODAY ALL TOURNAMENTS
    '''
    @classmethod
    async def get_tournaments(cls, request: Request, db: Session):
        tournamets = db.query(Prediction).filter(Prediction.date == cls.today).limit(4).distinct(Prediction.competition_name)

        if not tournamets:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return tournamets


    '''
    TODAY ALL FEDERATIONS
    '''
    @classmethod
    async def get_federations(cls, request: Request, db: Session):
        federations = db.query(Prediction).filter(Prediction.date == cls.today).distinct(Prediction.federation)

        if not federations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return federations
