from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class DateStats:

    # '''
    # DAY WINS STATISTICS
    # '''
    @classmethod
    async def wins_games_count(cls, request: Request, dt: str, db: Session):
    
        wins_count = []
        games = db.query(Prediction).filter(Prediction.date == dt).all()
       
        if not games:
            return ""
        
        if len(games) > 0:
            for game in games:
                if game.status == 'won':
                    wins_count.append(game)

        return len(wins_count)
    

    # '''
    # DAY LOSTS STATISTICS 
    # '''
    @classmethod
    async def losts_games_count(cls, request: Request, dt: str, db: Session):
    
        losts_count = []
        games = db.query(Prediction).filter(Prediction.date == dt).all()
       
        if not games:
            return ""
        
        if len(games) > 0:
            for game in games:
                if game.status == 'lost':
                    losts_count.append(game)

        return len(losts_count)
    

    # FEDERATIONS
    
    