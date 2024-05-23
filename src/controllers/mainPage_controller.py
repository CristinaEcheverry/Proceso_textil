from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class MainPageController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/mainPage")
    def mainPage():
        return render_template("mainPage.html", title= "Página Principal")
