from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import config

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{config.settings.DB_USER}:{config.settings.DB_PASS}@{config.settings.DB_HOST}:{config.settings.DB_PORT}/{config.settings.DB_NAME}?charset=utf8mb4"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()