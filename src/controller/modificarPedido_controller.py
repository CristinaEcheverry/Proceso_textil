from src.app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template  # render_template es para usar las vistas

@app.route("/modificarPedido")
def modificarPedido():
    return render_template("modificarPedido_form.html", title= "Modificar pedido")