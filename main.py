from fastapi import FastAPI, Depends
from db import models
from db.database import engine
from typing import Optional
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status
from routers import api


app = FastAPI()

app.include_router(api.router)

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    
     return RedirectResponse("http://127.0.0.1:8000/api/predictions")
    