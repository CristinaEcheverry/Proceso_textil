from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config ["SQLALCHEMY_DATABASE_URI"] - 'mysql//Proceso_textil.db'

#db=SQLAlchemy(app)

#with app.app_context():
#    db.create_all()


from controller import *

if __name__ == "__main__":
    app.run(debug=True) # si llaman a __name__ se reproduce

    