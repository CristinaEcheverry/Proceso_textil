from src.app import app
from flask import render_template, request, redirect, url_for, jsonify
from flask_controller import FlaskController
from src.model.pedido_model import Pedido, PedidoDetalle
from src.model.prenda_model import Prenda
from src.model.clientes_model import Clientes
from src.model.enums.enum_estadoPedido import EstadoPedidoEnum
from src.model.enums.enum_tipoPedido import TipoPedidoEnum
from src.model.enums.enum_tipoPrenda import TipoPrendaEnum
import datetime

class PedidosController(FlaskController):
    @app.route("/crearPedido", methods=['GET','POST'])
    def crearPedido():
        if request.method == 'POST':
            numero_pedido = request.form.get('num_pedido')
            clientes_id = request.form.get('num_identificacion')
            estado_pedido_id = request.form.get('estados')
            fecha_pedido = request.form.get('fecha-pedido')        
            fecha_documento = request.form.get('fecha-recibido')
            fecha_despacho = request.form.get('fecha-despacho')
            tipo_pedido_id = request.form.get('tipos')            
            nuevo_pedido = Pedido(numero_pedido, clientes_id, estado_pedido_id, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido_id)
            Pedido.agregar_pedido(nuevo_pedido)

            # Agregar detalle del pedido
            # Obtener todos los datos del formulario
            detalles = request.form.to_dict(flat=False)  
            i = 0
            while f'detalles[{i}][tipo_prenda]' in detalles:
                tipo_prenda_id = detalles[f'detalles[{i}][tipo_prenda]'][0]
                prenda_id = detalles[f'detalles[{i}][prenda]'][0]
                material = detalles[f'detalles[{i}][material]'][0]
                cantidad = detalles[f'detalles[{i}][cantidad]'][0]
                
                # Crear el nuevo detalle del pedido
                nuevo_pedido_detalle = PedidoDetalle(nuevo_pedido.id, tipo_prenda_id, prenda_id, material, cantidad)
                nuevo_pedido_detalle.agregar_detalle()
                
                i += 1    
        fecha_documento = datetime.datetime.now()
        clientes = Clientes.obtener_cliente()       
        prendas = Prenda.obtener_prendas()
        pedido = Pedido.obtener_pedido()
        # Obtener el último ID y calcular el nuevo número de pedido
        ultimo_id = Pedido.obtener_ultimo_id()
        nuevo_numero_pedido = f"PP{ultimo_id + 1:05d}"
        return render_template('crearPedido_form.html', 
                                enum_estadoPeValue=EstadoPedidoEnum, 
                                enum_tipoPeValue=TipoPedidoEnum, 
                                enum_values=TipoPrendaEnum, 
                                prendas=prendas, 
                                pedidos=pedido, 
                                fecha=fecha_documento, 
                                clientes=clientes, 
                                nuevo_numero_pedido=nuevo_numero_pedido)
