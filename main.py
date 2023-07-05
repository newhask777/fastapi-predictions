from fastapi import FastAPI, Depends
from db import models
from db.database import engine
from typing import Optional
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status

from routers import predictions
from routers import home
from routers import api

app = FastAPI()
app.include_router(predictions.router)
app.include_router(home.router)
app.include_router(api.router)

models.Base.metadata.create_all(bind=engine)

app.mount("/statis", StaticFiles(directory="static"), name="static")

@app.get('/')
async def root():
    
    return {"data": "start"}
    