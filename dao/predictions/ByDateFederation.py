from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class ByDateFederation:

    # '''
    # ALL GAMES
    # '''
    @classmethod
    async def get_games_by_date_federation(cls, request, federation, td, db):
        games = db.query(Prediction)\
        .filter(Prediction.date == td)\
        .filter(Prediction.federation == federation).all()

        if not games:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Games not found')
        
        return games
    

    # '''
    # ALL LEAGUES
    # '''
    @classmethod
    async def get_leagues_by_date_federation(cls, request, federation, td, db):
        leagues = db.query(Prediction).filter(Prediction.date == td)\
        .filter(Prediction.federation == federation)\
        .distinct(Prediction.competition_cluster)

        if not leagues:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Leagues not found')
        
        return leagues
    

    # '''
    # ALL TOURNAMENTS
    # '''
    @classmethod
    async def get_tournaments_by_date_federation(cls, request, federation, td, db):
        tournaments = db.query(Prediction).filter(Prediction.date == td)\
        .filter(Prediction.federation == federation)\
        .distinct(Prediction.competition_name)

        if not tournaments:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return tournaments
    

    # '''
    # ALL FEDERATIONS
    # '''
    @classmethod
    async def get_federations_by_date_federation(cls, request, federation, td, db):
        federations = db.query(Prediction)\
        .filter(Prediction.date == td)\
        .distinct(Prediction.federation)

        if not federations:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournaments not found')
        
        return federations
    

    # '''
    # GET WONS
    # '''
    @classmethod
    async def get_wons(cls, request, federation, td, db):
        wons = db.query(Prediction)\
        .filter(Prediction.date == td)\
        .filter(Prediction.federation == federation)\
        .filter(Prediction.status == "won").all()

        w_count = len(wons)
        return w_count
    

    # '''
    # GET LOSTS
    # '''
    @classmethod
    async def get_losts(cls, request, federation, td, db):
        lost = db.query(Prediction).filter(Prediction.date == td)\
        .filter(Prediction.federation == federation)\
        .filter(Prediction.status == "lost").all()
        l_count = len(lost)

        return l_count
    

    # '''
    # GET WIN RATE
    # '''
    @classmethod
    async def get_win_coef(cls, games):
        win_coef = []

        for game in games:
            for k, v in game.odds.items():
                if k == game.prediction:
                    if game.status == 'won':

                        win_coef.append(v)

        cf_plus = sum([c for c in win_coef])
        return cf_plus
    

    # '''
    # GET LOST RATE
    # '''
    @classmethod
    async def get_lost_coef(cls, games):
        lost_coef = []

        for game in games:
            for k, v in game.odds.items():
                if k == game.prediction:
                    if game.status == 'lost':

                        lost_coef.append(v)

        cf_minus = sum([c for c in lost_coef])
        return cf_minus

