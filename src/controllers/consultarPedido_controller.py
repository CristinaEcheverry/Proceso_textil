from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from flask_controller import FlaskController

class ConsultarPedidoController(FlaskController):
    def __init__(self):
        super().__init__()

        
    @app.route("/consultarPedido")
    def consultarPedido():
        return render_template("consultarPedido_form.html", title= "Consultar pedido")