from app import app
from src.models.prendas import Prenda
from src.models.tipo_prenda import TipoPrenda # Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from flask_controller import FlaskController

class PrendasController(FlaskController):
    def __init__(self):
        super().__init__()

    @app.route("/crearTipoPrenda", methods=['GET','POST'])
    def crearTipoPrenda():
        if request.method == 'POST':
            tipo_prenda = request.form.get('tipo_prenda')
            prenda = request.form.get('prenda')
            tipo_prenda = TipoPrenda(tipo_prenda,prenda)
            TipoPrenda.agregar_tipo_prenda(tipo_prenda)
            return redirect(url_for('tipo_prenda'))
        prenda = Prenda.obtener_prenda()
        return render_template("crearTipoPrenda.html", prenda=prenda)

    @app.route("/tipo_prenda")
    def tipo_prenda():
        tipo_prenda = TipoPrenda.obtener_tipo_prenda()
        return render_template("tipo_prenda.html",tipo_prenda=tipo_prenda)