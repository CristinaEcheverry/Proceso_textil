from app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template  # render_template es para usar las vistas

@app.route("/consultarPedido")
def consultarPedido():
    return render_template("consultarPedido_form.html", title= "Consultar pedido")