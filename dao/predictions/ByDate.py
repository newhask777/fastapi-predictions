from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class ByDate:


    '''
    BY DATE ALL GAMES
    '''
    @classmethod
    async def get_games_by_date(cls, request: Request, dt: str, db: Session):
        games = db.query(Prediction).filter(Prediction.date == dt).all()

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Games for {date} not found')
        
        return games


    '''
    BY DATE ALL LEAGUES
    '''
    @classmethod
    async def get_leagues_by_date(cls, request: Request, dt: str, db: Session):
        leagues = db.query(Prediction).filter(Prediction.date == dt).distinct(Prediction.competition_cluster)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues for {date} not found')
        
        return leagues


    '''
    BY DATE ALL TOURNAMENTS
    '''
    @classmethod
    async def get_tournaments_by_date(cls, request: Request, dt: str, db: Session):
        tournaments = db.query(Prediction).filter(Prediction.date == dt)\
        .distinct(Prediction.competition_cluster)\
        .distinct(Prediction.competition_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments for {date} not found')
        
        return tournaments


    '''
    BY DATE ALL FEDERATIONS
    '''
    @classmethod
    async def get_federations_by_date(cls, request: Request, dt: str, db: Session):
        federations = db.query(Prediction).filter(Prediction.date == dt).distinct(Prediction.federation)

        if not federations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Federations for {date} not found')
        
        return federations