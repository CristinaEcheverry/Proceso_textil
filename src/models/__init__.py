from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/fashionprocess")
connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

class Config:
    SECRET_KEY = "j31dy$0l4y4"