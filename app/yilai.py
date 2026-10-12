from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

class Settings(BaseSettings):
    DATABASE_URL:str
    APP_TITLE:str
    class Config():
        env_file='.env'
settings=Settings()
engine=create_engine(settings.DATABASE_URL)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()