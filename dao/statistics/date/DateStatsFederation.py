from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class DateStatsFederation:

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
    


    # '''
    # DAY WINS STATISTICS BY AFC
    # '''
    @classmethod
    async def wins_by_date_afc(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "AFC")\
            .filter(Prediction.status == "won")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY LOSTS STATISTICS BY AFC
    # '''
    @classmethod
    async def losts_by_date_afc(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "AFC")\
            .filter(Prediction.status == "lost")\
            .all()

        if not games:
            return ""
            
        return len(games)
    


     # '''
    # DAY WINS STATISTICS BY COMNEBOL
    # '''
    @classmethod
    async def wins_by_date_comnebol(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CONMEBOL")\
            .filter(Prediction.status == "won")\
            .all()

        if not games:
            return ""
            
        return len(games)
    

    # '''
    # DAY LOSTS STATISTICS BY COMNEBOL
    # '''
    @classmethod
    async def losts_by_date_comnebol(cls, request, td, db):

        games = db.query(Prediction)\
            .filter(Prediction.date == td)\
            .filter(Prediction.federation == "CONMEBOL")\
            .filter(Prediction.status == "lost")\
            .all()

        if not games:
            return ""
            
        return len(games)
    
    

    


    