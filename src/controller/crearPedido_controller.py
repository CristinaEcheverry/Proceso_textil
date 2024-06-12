from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.model.pedido_model import Pedido
from src.model.prenda_model import Prenda
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum
from src.model.enums.enum_estadoPedido import EstadoPedidoEnum
from src.model.enums.enum_tipoPedido import TipoPedidoEnum
from src.model.enums.enum_tipoPrenda import TipoPrendaEnum

class ProductosController(FlaskController):
    @app.route("/crearPedido", methods=['GET','POST'])
    def crearPedido():
        if request.method == 'POST':
            clientes_id = request.form.get('clientes')
            estado_pedido_id = request.form.get('estados')
            fecha_pedido = request.form.get('fecha-pedido')        
            fecha_documento = request.form.get('fecha-recibido')
            fecha_despacho = request.form.get('fecha-despacho')
            tipo_pedido_id = request.form.get('tipos')
            tipo_prenda_id = str(request.form.get('tipo_prenda'))
            prenda_id = request.form.get('prenda')
            material = request.form.get('material')
            cantidad = request.form.get('cantidad')
            nuevo_pedido = Pedido(clientes_id, estado_pedido_id, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido_id, tipo_prenda_id, prenda_id, material, cantidad)
            Pedido.agregar_pedido(nuevo_pedido) 
             
            return redirect(url_for('crearPedido'))
        prendas = Prenda.mostrar_prenda()
        pedido = Pedido.optener_pedido()
        return render_template('crearPedido_form.html', enum_idValue=TipoIdentificacionEnum, enum_estadoPeValue=EstadoPedidoEnum, enum_tipoPeValue=TipoPedidoEnum, enum_values=TipoPrendaEnum, prendas=prendas, pedidos=pedido)
            