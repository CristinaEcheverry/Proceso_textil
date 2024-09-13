from src.app import app
from flask import render_template, request, redirect, url_for, jsonify, flash
from src.model.clientes_model import Clientes
from src.model.tipoIdent_model import TipoIdentificacion
from flask_controller import FlaskController

class ClientesController(FlaskController):
    @app.route("/consultarCliente", methods=['GET', 'POST'])
    def consultarCliente():
        clientes = []
        if request.method == 'POST':
            tipo_identificacion = request.form.get('tipo_identificacion')
            num_identificacion = request.form.get('numero_identificacion')
            print(f"tipo_identificacion: {tipo_identificacion}\nnum_identificacion: {num_identificacion}")

            clientes = Clientes.obtener_cliente_criterio(
                tipo_identificacion, 
                num_identificacion)
        tipo_identificacion = TipoIdentificacion.obtener_tipo_identificacion()
        return render_template('consultarCliente_form.html', tipoID=tipo_identificacion, cliente=clientes)

    @app.route('/eliminarCliente/<int:id>', methods=['GET'])
    def eliminarCliente(id):
        cliente = Clientes.obtener_cliente_id(id)
        Clientes.eliminar_cliente(cliente)
        flash("Cliente eliminado correctamente.")
        return redirect(url_for('consultarCliente'))
