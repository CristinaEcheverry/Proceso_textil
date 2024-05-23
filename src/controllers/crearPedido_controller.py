from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class CrearPedidoController(FlaskController):
    def __init__(self):
        super().__init__()

        
    @app.route("/crearPedido")
    def crearPedido():
        return render_template("crearPedido_form.html", title= "Crear pedido")
