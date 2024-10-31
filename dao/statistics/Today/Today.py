from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class Today:


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
    
    # '''
    # DAY WINS STATISTICS BY UEFA
    # '''
    @classmethod
    async def wins_by_date_uefa(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "UEFA")\
            .filter(Prediction.status == "won")\
            .all()

        if not games:
            return ""
            
        return len(games)


    # '''
    # DAY LOSTS STATISTICS BY UEFA
    # '''
    @classmethod
    async def losts_by_date_uefa(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "UEFA")\
            .filter(Prediction.status == "lost")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY WINS STATISTICS BY CONCACAF
    # '''
    @classmethod
    async def wins_by_date_concacaf(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CONCACAF")\
            .filter(Prediction.status == "won")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY LOSTS STATISTICS BY CONCACAF
    # '''
    @classmethod
    async def losts_by_date_concacaf(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CONCACAF")\
            .filter(Prediction.status == "lost")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY WINS STATISTICS BY CAF
    # '''
    @classmethod
    async def wins_by_date_caf(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CAF")\
            .filter(Prediction.status == "won")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY LOSTS STATISTICS BY CAF
    # '''
    @classmethod
    async def losts_by_date_caf(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CAF")\
            .filter(Prediction.status == "lost")\
            .all()

        if not games:
            return ""
            
        return len(games)
    
    

    


    