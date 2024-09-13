from src.app import app
from flask import render_template, request, redirect, url_for, jsonify, flash
from src.model.clientes_model import Clientes
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.tipoPersona_model import TipoPersona
from flask_controller import FlaskController

class ClientesController(FlaskController):
    #Ruta para buscar el cliente a modificar
    @app.route("/modificarCliente", methods=['GET', 'POST'])
    def modificarCliente():
        if request.method == 'POST':
            num_identificacion = request.form.get('numero_identificacion')
            cliente = Clientes.obtener_cliente_numeroId(num_identificacion)
            try:
                if cliente:
                    cliente_id = cliente['cliente'][0]['id']                    
                    return redirect(url_for('actualizarCliente', id=cliente_id))
            except Exception as e:
                flash(f'Error al buscar el cliente: {str(e)}', 'error')
                return redirect(url_for('modificarCliente'))
        return render_template('modificarCliente_boton.html')

    #Ruta para actualizar el cliente
    @app.route("/actualizarCliente/<int:id>", methods=['GET', 'POST'])
    def actualizarCliente(id):
        '''Actualizar datos del cliente'''
        cliente = Clientes.obtener_cliente_id(id)
        print(cliente)

        if request.method == 'POST':
            try:
                #Actualiza los datos del cliente
                cliente.tipo_identificacion.codigo = request.form.get('tipo_identificacion')
                cliente.numero_identificacion = request.form.get('numero_identificacion')
                cliente.tipo_persona.tipo_persona = request.form.get('tipo_persona')
                cliente.nombre = request.form.get('nombre')
                cliente.direccion = request.form.get('direccion')
                cliente.ciudad = request.form.get('ciudad')
                cliente.telefono = request.form.get('telefono')
                cliente.correo = request.form.get('correo')
                Clientes.modificar_cliente()
                flash('Cliente actualizado exitosamente', 'success')
                return redirect(url_for('actualizarCliente', id=id))
            except Exception as e:
                flash(f'Error al actualizar el cliente: {str(e)}', 'error')
                return redirect(url_for('actualizarCliente', id=id))
        tipos_identificacion = TipoIdentificacion.obtener_tipo_identificacion()
        tipoPersona = TipoPersona.obtener_tipo_persona()
        return render_template('modificarCliente_form.html', cliente=cliente, identificacion=tipos_identificacion, tipoPersona=tipoPersona)