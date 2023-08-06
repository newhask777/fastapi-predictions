import sys
sys.path.append("..")
# fastapi
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, APIRouter, Request, Form, HTTPException
# db
from sqlalchemy.orm.session import Session
from db.models import Event
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
        games = db.query(Event).filter(Event.date == cls.today).all()

        # print(cls.today)
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
        leagues = db.query(Event).filter(Event.date == cls.today).distinct(Event.tournament_name)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues not found')
        
        return leagues
    

    '''
    TODAY ALL TOURNAMENTS
    '''
    @classmethod
    async def get_tournaments(cls, request, db):
        tournaments = db.query(Event).filter(Event.date == cls.today).distinct(Event.tournament_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return tournaments
    

    '''
    TODAY ALL COUNTRIES
    '''
    @classmethod
    async def get_countries(cls, request, db):
        countries = db.query(Event).filter(Event.date == cls.today).distinct(Event.tournament_category)

        if not countries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Countries not found')
        
        return countries
    

    '''
    GAME DETAILS
    '''
    @classmethod
    async def get_detail(cls, id, request, db):
        game = db.query(Event).filter(Event.event_id == id).first()

        if not game:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Game not found')
        
        return game
    

    '''
    GAMES BY DATE
    '''
    @classmethod
    async def get_games_by_date(cls, request, td, db):
        games = db.query(Event).filter(Event.date == td).all()
        tournaments = db.query(Event).filter(Event.date == td).distinct(Event.tournament_name)

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Games by date {td} not found')
        
        return games
    

    '''
    TOURNAMENTS BY DATE
    '''
    @classmethod
    async def get_tournaments_by_date(cls, request, td, db):
        tournaments = db.query(Event).filter(Event.date == td).distinct(Event.tournament_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments by date {td} not found')
        
        return tournaments

    '''
    LIVE GAMES
    '''
    @classmethod
    async def get_live_games(cls, request, db):
        games = db.query(Event).filter(Event.status == 'inprogress').filter(Event.date == cls.today).all()
        
        # tournaments = db.query(Event).filter(Event.status == 'inprogress').filter(Event.date == cls.today).distinct(Event.tournament_name)
        

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No started games')
        
        return games
    
    '''
    LIVE TOURNAMENTS
    '''
    @classmethod
    async def get_live_tournaments(cls, request, db):
        tournaments = db.query(Event).filter(Event.status == 'inprogress').filter(Event.date == cls.today).distinct(Event.tournament_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No started games')
        
        return tournaments
    

    '''
    LIVE LEAGUES
    '''
    @classmethod
    async def get_live_leagues(cls, request, db):
        leagues = db.query(Event).filter(Event.date == cls.today).distinct(Event.tournament_name)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No started games')
        
        return leagues
    

    '''
    LIVE COUNTRIES
    '''
    @classmethod
    async def get_live_countries(cls, request, db):
        countries = db.query(Event).filter(Event.date == cls.today).distinct(Event.tournament_category)

        if not countries:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No started games')
        
        return countries