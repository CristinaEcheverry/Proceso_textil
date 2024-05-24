from flask import Flask
from src.models import Base, engine
from flask_controller import FlaskControllerRegister

from flask_wtf import csrf
from src.controllers.index_controller import error401, error404

app = Flask(__name__)

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

csrf = csrf.CSRFProtect(app)

Base.metadata.create_all(engine)

if __name__ == "__main__":
    csrf.init_app(app)
    app.register_error_handler(401, error401)
    app.register_error_handler(404, error404)
    app.run(debug=True) # si llaman a __name__ se reproduce


    