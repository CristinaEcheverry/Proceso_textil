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
            detalles = request.form.to_dict(flat=False)  # Obtener todos los datos del formulario
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

    # #TODO ruta para modificar o actualizar el pedido por el numero de pedido 
    # @app.route("/modificarPedido/<int:id>", methods=["GET", "POST"])
    # def modificarPedido(id):
    #     '''Aquí actualizará el pedido'''
    #     if request.method == "POST":
    #         # Aquí se tiene que hacer el update
    #         id = request.form["id"]
    #         estado = request.form["estado"]
    #         fecha_entrega = request.form["fecha_entrega"]
    #         fecha_pedido = request.form["fecha_pedido"]
    #         total = request.form["total"]
    #         id_cliente = request.form["id_cliente"]
    #         id_producto = request.form["id_producto"]
    #         cantidad = request.form["cantidad"]
    #         precio = request.form["precio"]
    #         actualPedido = Pedido.modificar_pedido(id, estado, fecha_entrega, fecha_pedido, total, id_cliente, id_producto, cantidad, precio)
    #         return redirect(url_for("modificarPedido", id=id))
    #     record = obtenerPedido(id)
    #     return render_template("modificarPedido_form.html", title= "Modificar pedido", record=record)

    # #TODO ruta para consultar el pedido
    # @app.route("/consultarPedido", methods=["GET"])
    # def consultarPedido():
    #     pedidos = Pedido.obtener_pedido()
    #     return render_template("consultarPedido.html", pedidos=pedidos)

    # #TODO ruta para eliminar un pedido
    # @app.route("/eliminarPedido/<int:id>", methods=["GET"])
    # def eliminarPedido(id):
    #     Pedido.eliminar_pedido(id)
    #     return redirect(url_for("consultarPedido"))

