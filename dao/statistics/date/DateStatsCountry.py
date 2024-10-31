from sqlalchemy.orm.session import Session
from db.models import Prediction
# from db.schemas import Prediction
from fastapi import HTTPException, status, Request
from datetime import date


class DateStatsCountry:
    pass