from typing import List
from pydantic import BaseModel

# Article inside UserDisplay
class PredictionView(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    orm_mode = True

class Prediction(BaseModel):
  username: str
  email: str
  items: List[Article] = []



