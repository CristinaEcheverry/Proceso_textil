from src.app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for, flash  # render_template es para usar las vistas
from flask_controller import FlaskController
from src.model.pedido_model import Pedido, PedidoDetalle
from src.model.clientes_model import Clientes
from src.model.estadoPedido_model import EstadoPedido
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.estadoPedido_model import EstadoPedido


class ConsultarPedidoController(FlaskController):
    @app.route("/consultarPedido", methods=["GET", "POST"])
    def consultarPedido():
        '''Aquí va el código para consultar los pedidos, se debe obtener los pedidos y 
        sus detalles para mostrarlos en la vista.'''
        pedidos = []
        if request.method == 'POST':
            tipo_identificacion = request.form.get('tipo_identificacion')
            num_identificacion = request.form.get('num_identificacion')
            nombre = request.form.get('nombre')
            num_pedido = request.form.get('num_pedido')
            estado_pedido_id = request.form.get('estados')
            fecha_pedido = request.form.get('fecha-pedido')
            fecha_despacho = request.form.get('fecha-despacho')
            
            print(f"tipo_identificacion: {tipo_identificacion}")
            print(f"num_identificacion: {num_identificacion}")
            print(f"nombre: {nombre}")
            print(f"estado_pedido_id: {estado_pedido_id}")
            print(f"num_pedido: {num_pedido}")
            print(f"fecha_pedido: {fecha_pedido}")
            print(f"fecha_despacho: {fecha_despacho}")

            pedidos = PedidoDetalle.obtener_detalle_por_criterio(
                tipo_identificacion=tipo_identificacion,
                num_identificacion=num_identificacion,
                nombre=nombre,
                estado_pedido_id=estado_pedido_id,
                num_pedido=num_pedido,
                fecha_pedido=fecha_pedido,
                fecha_despacho=fecha_despacho
            )

        tipoID = TipoIdentificacion.obtener_tipo_identificacion()
        estadoPedido = EstadoPedido.obtener_estado_pedido()
        return render_template("consultarPedido_form.html", pedidos=pedidos, tipoID=tipoID, estadoPedido=estadoPedido)
        
    #ruta para eliminar un pedido por medio de la consulta
    @app.route('/eliminarPedido/<int:id>', methods=['GET'])
    def eliminarPedido(id):
        '''Aquí va el código para eliminar un pedido.'''
        pedido = Pedido.obtener_pedido_id(id)
        detalle = PedidoDetalle.obtener_detalle(pedido_id=id)
        Pedido.eliminar_pedido(pedido)
        PedidoDetalle.eliminar_pedido_detalle(detalle)  
        flash("Pedido eliminado correctamente.")      
        return redirect(url_for('consultarPedido'))
