from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from app import app
from flask_controller import FlaskController

class ModificarRefMaterialController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/modificarRefMaterial")
    def modificarRefMaterial():
        return render_template("modificarRefMaterial_form.html", title= "Modificar referencia de material")