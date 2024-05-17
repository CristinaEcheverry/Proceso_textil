from flask import Flask
from model import Base, engine

app = Flask(__name__)


from controller import *
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True) # si llaman a __name__ se reproduce

    