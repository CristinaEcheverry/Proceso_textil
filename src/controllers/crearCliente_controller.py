from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class CrearClienteController(FlaskController):
    def __init__(self):
        super().__init__()

        
    @app.route("/crearCliente")
    def crearCliente():
        return render_template("crearCliente_form.html", title= "Crear cliente")