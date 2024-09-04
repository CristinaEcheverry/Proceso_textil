from src.app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template, redirect, request, url_for, flash  # render_template es para usar las vistas
from src.model.pedido_model import Pedido, PedidoDetalle
from flask_controller import FlaskController

class ModificarPedidoController(FlaskController):
    @app.route("/modificarPedido/<int:id>", methods=['GET', 'POST'])
    def modificarPedidoId(id):
        '''Aquí va el código para modificar el pedido, se debe obtener el pedido y sus detalles para mostrarlos en la vista.
        La persona debe poder modificar los datos del pedido y sus detalles.'''

        #Validar si el pedido existe en la db
        pedido = Pedido.obtener_pedido(id)
        if not pedido:
            return  flash("Pedido no encontrado", error)

        #Validar si el cliente existe en la db
        cliente = pedido.cliente
        if not cliente:
            flash('Cliente no encontrado', 'error')
            return redirect(url_for('index'))
        
            if request.method == 'POST':
                try:
                    # Actualizar datos del cliente
                    cliente.numero_identificacion = request.form.get('num_identificacion')
                    cliente.nombre = request.form.get('nombre')
                    cliente.direccion = request.form.get('direccion')
                    cliente.ciudad = request.form.get('ciudad')
                    cliente.telefono = request.form.get('telefono')
                    cliente.correo = request.form.get('correo')

                    # Actualizar datos del pedido
                    pedido.estado = request.form.get('estado')
                    pedido.fecha_pedido = request.form.get('fecha_pedido')
                    pedido.fecha_documento = request.form.get('fecha_documento')
                    pedido.fecha_despacho = request.form.get('fecha_despacho')
                    pedido.tipo_pedido = request.form.get('tipo_pedido')

                    # Manejo de detalles del pedido
                    for idx, detalle in enumerate(pedido.detalles):
                        detalle_form = PedidoDetalle(request.form, prefix=f"detalles[{idx}]")
                        if detalle_form.validate_on_submit():
                            detalle.tipo_prenda = detalle_form.tipo_prenda.data
                            detalle.prenda_id = detalle_form.prenda.data
                            detalle.material = detalle_form.material.data
                            detalle.cantidad = detalle_form.cantidad.data
                            # detalle.medidas = detalle_form.medidas.data

                            #mirar si este codigo funciona
                            # for idx in range(len(pedido.detalles)):
                            #     detalle_form = {
                            #         'tipo_prenda': request.form.get(f'detalles[{idx}][tipo_prenda]'),
                            #         'prenda': request.form.get(f'detalles[{idx}][prenda]'),
                            #         'material': request.form.get(f'detalles[{idx}][material]'),
                            #         'cantidad': request.form.get(f'detalles[{idx}][cantidad]'),
                            #         'medidas': request.form.get(f'detalles[{idx}][medidas]')
                            #      }
                                # if detalle_form['tipo_prenda']:
                                #     detalle = pedido.detalles[idx]
                                #     detalle.tipo_prenda = detalle_form['tipo_prenda']
                                #     detalle.prenda_id = detalle_form['prenda']
                                #     detalle.material = detalle_form['material']
                                #     detalle.cantidad = detalle_form['cantidad']
                                #     detalle.medidas = detalle_form['medidas']
                                #     detalle.modificar_detalle()  # Asume que este método existe para guardar los cambios
                            
                        # Crear el nuevo detalle del pedido
                        nuevo_pedido_detalle = PedidoDetalle(tipo_prenda, prenda_id, material, cantidad)
                        nuevo_pedido_detalle.modificar_detalle()
                    flash('Pedido actualizado exitosamente', 'success')
                    return redirect(url_for('modificarPedido', id=pedido_id.id))
                except Exception as e:
                    flash(f'Error al actualizar el pedido: {str(e)}', 'error')


        pedido = Pedido.obtener_pedido()
        pedido_detalles = PedidoDetalle.obtener_pedido_detalle(id)
        return render_template('modificarPedido_form.html', pedido=pedido, pedido_detalle=pedido_detalles)

    @app.route("/modificarPedido")
    def modificarPedido():
        return render_template('modificarPedido_form.html')
            