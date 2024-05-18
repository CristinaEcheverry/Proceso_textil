from flask import Flask
from src.models import Base, engine
from flask_controller import FlaskControllerRegister

app = Flask(__name__)

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True) # si llaman a __name__ se reproduce

    