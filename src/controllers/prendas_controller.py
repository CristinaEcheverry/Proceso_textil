from app import app
from src.models.prendas import Prenda
from src.models.tipo_prenda import TipoPrenda # Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from flask_controller import FlaskController

class PrendasController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/crearPrenda", methods=['GET','POST'])
    def crearPrenda():
        if request.method == 'POST': #si la info que llega viene de un formulario guardarlo en la db
            prenda = request.form.get('prenda')
            tipo_prenda = request.form.get('tipo_prenda')
            prenda = Prenda(prenda,tipo_prenda)
            Prenda.agregar_prenda(prenda)
            return redirect(url_for('prendas'))
        tipo_prenda = TipoPrenda.obtener_tipo_prenda()
        return render_template("crearPrenda.html", tipo_prenda=tipo_prenda)

    @app.route("/prendas")
    def prendas():
        prendas = Prenda.obtener_prenda()
        return render_template("prendas.html",prendas=prendas)

