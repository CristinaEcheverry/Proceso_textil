from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class IngresarMaterialController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/ingresarMaterial")
    def ingresarMaterial():
        return render_template("ingresarMaterial_form.html", title= "Ingresar material")