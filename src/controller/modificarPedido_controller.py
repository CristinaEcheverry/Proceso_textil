from src.app import app
#Aquí se tiene que importar todos los modelos o clases
from flask import render_template, redirect, request, url_for, flash 
from src.model.pedido_model import Pedido
from src.model.clientes_model import Clientes
from src.model.tipoPrenda_model import TipoPrenda
from src.model.prenda_model import Prenda
from src.model.estadoPedido_model import EstadoPedido
from src.model.tipoPedido_model import TipoPedido
from flask_controller import FlaskController

class ModificarPedidoController(FlaskController):
    @app.route("/modificarPedidoId/<int:id>", methods=['GET', 'POST'])
    def modificarPedidoId(id):
        '''Aquí va el código para modificar el pedido, se debe obtener el pedido y sus detalles para mostrarlos en la vista.
        La persona debe poder modificar los datos del pedido y sus detalles.'''
        pedido = Pedido.obtener_pedido_id(id)

        if request.method == 'POST':
            try:
                # Actualizar datos del cliente
                pedido.clientes.nombre = request.form.get('nombre')
                pedido.clientes.direccion = request.form.get('direccion')
                pedido.clientes.ciudad = request.form.get('ciudad')
                pedido.clientes.telefono = request.form.get('telefono')
                pedido.clientes.correo = request.form.get('correo')
                print(pedido.clientes.nombre, pedido.clientes.direccion, pedido.clientes.ciudad, pedido.clientes.telefono, pedido.clientes.correo)            

                # Actualizar datos del pedido
                pedido.estado_pedido.estados = request.form.get('estados')
                pedido.fecha_pedido = request.form.get('fecha_pedido')
                pedido.fecha_documento = request.form.get('fecha_recibido')
                pedido.fecha_despacho = request.form.get('fecha_despacho')
                pedido.tipo_pedido.tipo_pedido = request.form.get('tipos')
                print(pedido.estado_pedido.estados, pedido.fecha_pedido, pedido.fecha_documento, pedido.fecha_despacho, pedido.tipo_pedido.tipo_pedido)

                # Manejo de detalles del pedido                        
                for idx, detalle in enumerate(pedido.detalle_pedido):
                    detalle_form = {
                        'tipo_prenda': request.form.get(f'detalles[{idx}][tipo_prenda]'),
                        'prenda': request.form.get(f'detalles[{idx}][prenda]'),
                        'material': request.form.get(f'detalles[{idx}][material]'),
                        'cantidad': request.form.get(f'detalles[{idx}][cantidad]'),
                        }
                    if detalle_form['tipo_prenda']:
                        detalle = pedido.detalle_pedido[idx]
                        detalle.tipo_prenda_id = detalle_form['tipo_prenda']
                        detalle.prenda_id = detalle_form['prenda']
                        detalle.material = detalle_form['material']
                        detalle.cantidad = detalle_form['cantidad']
                        print(detalle.tipo_prenda_id, detalle.prenda_id, detalle.material, detalle.cantidad)
                Pedido.modificar_pedido()
                flash('Pedido actualizado exitosamente', 'success')
                return render_template('modificarPedido_form.html', pedido=pedido)
            except Exception as e:
                flash(f'Error al actualizar el pedido: {str(e)}', 'error')
                return redirect(url_for('modificarPedido'))
        pedido = Pedido.obtener_pedido_id(id)
        estado_pedido = EstadoPedido.obtener_estado_pedido()
        tipos_pedido = TipoPedido.obtener_tipo_pedido()
        tipo_prenda = TipoPrenda.obtener_tipo_prendas()
        prenda = Prenda.obtener_prendas()
        return render_template('modificarPedido_form.html', pedidos=pedido, enum_estadoPeValue=estado_pedido, enum_tipoPeValue=tipos_pedido, tipos_prenda=tipo_prenda, prendas=prenda)

    @app.route("/modificarPedido", methods=['GET', 'POST'])
    def modificarPedido():
        if request.method == 'POST':
            numero_pedido = request.form.get('num_pedido')
            pedido = Pedido.obtener_pedido_dato(numero_pedido)
            try:
                if pedido:
                    pedido_id = pedido['pedido'][0]['id']
                    return redirect(url_for('modificarPedidoId', id=pedido_id))
            except Exception as e:
                flash(f'Error al buscar el pedido: {str(e)}', 'error')
                return redirect(url_for('modificarPedido'))
        return render_template('modificarPedido_boton.html')