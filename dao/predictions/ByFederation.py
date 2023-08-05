from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class ByFederation:

    today = str(date.today())

    # '''
    # ALL GAMES
    # '''
    @classmethod
    async def get_games_by_federation(cls, request, federation, db):
        games = db.query(Prediction)\
        .filter(Prediction.federation == federation)\
        .filter(Prediction.date == cls.today)\
        .all()

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Games not found')
        
        return games
    

    # '''
    # ALL LEAGUES
    # '''
    @classmethod
    async def get_leagues_by_federation(cls, request, federation, db):
        leagues = db.query(Prediction)\
        .filter(Prediction.federation == federation)\
        .filter(Prediction.date == cls.today)\
        .all()

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues not found')
        
        return leagues
    

    # '''
    # ALL TOURNAMENTS
    # '''
    @classmethod
    async def get_tournaments_by_federation(cls, request, federation, db):
        tournaments = db.query(Prediction)\
        .filter(Prediction.federation == federation)\
        .filter(Prediction.date == cls.today)\
        .distinct(Prediction.competition_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return tournaments
    


    # '''
    # ALL FEDERATIONS
    # '''
    @classmethod
    async def get_federations_by_federation(cls, request, federation, db):
        federations = db.query(Prediction)\
        .filter(Prediction.date == cls.today)\
        .distinct(Prediction.federation)

        if not federations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'federations not found')
        
        return federations