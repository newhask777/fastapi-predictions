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
    async def get_games(cls, request, db):
        games = db.query(Prediction).filter(Prediction.date == cls.today).all()
        print(cls.today)
        # for game in games:
        #     print(game.as_dict())

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Predictions not found')
        
        return games


    '''
    TODAY ALL LEAGUES
    '''
    @classmethod
    async def get_leagues(cls, request, db):
        leagues = db.query(Prediction).filter(Prediction.date == cls.today)\
        .distinct(Prediction.competition_cluster)\
        .distinct(Prediction.competition_name)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues not found')
        
        return leagues


    '''
    TODAY ALL TOURNAMENTS
    '''
    @classmethod
    async def get_tournaments(cls, request, db):
        tournaments = db.query(Prediction).filter(Prediction.date == cls.today)\
        .distinct(Prediction.competition_cluster)\
        .distinct(Prediction.competition_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return tournaments


    '''
    TODAY ALL FEDERATIONS
    '''
    @classmethod
    async def get_federations(cls, request, db):
        federations = db.query(Prediction).filter(Prediction.date == cls.today)\
        .distinct(Prediction.federation)

        if not federations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return federations
