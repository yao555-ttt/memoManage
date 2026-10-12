from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from app.yilai import engine
Base=declarative_base()

class Memo(Base):
    __tablename__='memo'
    id=Column(Integer,primary_key=True)
    title=Column(String(100),nullable=False)
    content=Column(String(100),nullable=False)
    time=Column(DateTime,default=datetime.now)

Base.metadata.create_all(engine)

