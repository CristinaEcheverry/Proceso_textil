from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from app import app
from flask_controller import FlaskController


class ModificarPedidoController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/modificarPedido")
    def modificarPedido():
        return render_template("modificarPedido_form.html", title= "Modificar pedido")
