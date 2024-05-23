from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class ConsultarMaterialController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/consultarMaterial")
    def consultarMaterial():
        return render_template("consultarMaterial_form.html", title= "Consultar material")