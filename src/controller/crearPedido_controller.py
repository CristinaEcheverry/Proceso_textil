from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.model.pedido_model import Pedido
from src.model.tipoPrenda_model import TipoPrenda
from src.model.prenda_model import Prenda


class ProductosController(FlaskController):
    @app.route("/crearPedido", methods=['GET','POST'])
    def crearPedido():
        if request.method == 'POST':
            tipo_identificacion = request.form.get('tipo_identificacion')
            numero_identificacion = request.form.get('num_identificacion')
            nombre = request.form.get('nombre')
            direccion = request.form.get('direccion')
            ciudad = request.form.get('ciudad')
            telefono = request.form.get('telefono')
            correo = request.form.get('correo')
            estado_pedido = request.form.get('estado-pedido')
            fecha_pedido = request.form.get('fecha-pedido')
            fecha_documento = request.form.get('fecha-recibido')
            fecha_despacho = request.form.get('fecha-despacho')
            tipo_pedido = request.form.get('tipo-pedido')
            tipo_prenda_id = request.form.get('tipo_prenda_id')
            prenda_id = request.form.get('prenda_id')
            material = request.form.get('material')
            cantidad = request.form.get('cantidad')
            pedido = Pedido(nombre, direccion, tipo_identificacion, numero_identificacion, telefono, correo, ciudad, estado_pedido, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido, tipo_prenda_id, prenda_id, material,cantidad)
            Pedido.agregar_pedido(pedido)
            return redirect(url_for('crearPedido'))
        tipo_prenda_id = TipoPrenda.obtener_tipo_prendas()
        prenda_id = Prenda.obtener_prendas()
        return render_template("crearPedido_form.html", title= "Crear pedido")