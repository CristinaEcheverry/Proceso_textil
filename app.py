from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import create_engine
# # import pymysql


app = Flask(__name__)
# engine = create_engine("mysql+pysql://root@localhost/fashionProcess")

# app.config ["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3306/fashionprocess'

# conect = engine.connect()

# Base = declarative_base()
# Base.metadata.create_all(engine)
# Base.metadata.bind = engine

# Sesion = sessionmaker(bind=engine)

# db=SQLAlchemy(app)

# with app.app_context():
#    db.create_all()
from controllers.controller import *

if __name__ == "__main__":
    app.run(debug=True) # si llaman a __name__ se reproduce



    