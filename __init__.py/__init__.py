#Aquí es donde inicializas tu aplicación Flask y cualquier extensión que estés utilizando.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)