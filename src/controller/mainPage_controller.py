from src.app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template  # render_template es para usar las vistas

@app.route("/mainPage")
def mainPage():
    return render_template("mainPage.html", title= "Página Principal")