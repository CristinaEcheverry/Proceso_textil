from flask import Flask

app = Flask(__name__)

from controller import *

if __name__ == "__main__":
    app.run(debug=True) # si llaman a __name__ se reproduce