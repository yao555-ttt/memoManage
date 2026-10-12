from pydantic import BaseModel
from datetime import datetime

class MemoCreate(BaseModel):
    title:str
    content:str

class MemoUpdate(BaseModel):
    title:str
    content:str

class MemoRead(BaseModel):
    id:int
    title:str
    content:str
    time:datetime