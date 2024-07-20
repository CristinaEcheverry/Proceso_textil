from src.app import app
from flask import render_template, request, redirect, url_for, jsonify
from src.model.clientes_model import Clientes
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.tipoPersona_model import TipoPersona
from flask_controller import FlaskController

class ClientesController(FlaskController):
    @app.route('/crearCliente', methods=['GET','POST'])
    def crearCliente():
        if request.method == 'POST':
            tipo_identificacion_id = request.form.get('tipo_identificacion')
            numero_identificacion = request.form.get('num_identificacion')
            tipo_persona = request.form.get('tipo_persona')
            nombre = request.form.get('nombre')
            direccion = request.form.get('direccion')
            ciudad = request.form.get('ciudad')
            telefono = request.form.get('telefono')
            correo = request.form.get('correo')
            cliente_nuevo = Clientes(tipo_identificacion_id, numero_identificacion, tipo_persona, nombre, direccion, ciudad, telefono, correo)
            Clientes.agregar_cliente(cliente_nuevo)
            return redirect(url_for('crearCliente'))
        identificar = TipoIdentificacion.obtener_tipo_identificacion()
        tipoPersona = TipoPersona.obtener_tipo_persona()
        clientes = Clientes.obtener_cliente()
        return render_template('crearCliente.html', title= 'CrearCliente', clientes=clientes, identificacion=identificar, tipoPersona=tipoPersona)
    
    @app.route("/cliente/<id>", methods=['GET'])
    def obtener_cliente_por_id(id):
        cliente = Clientes.obtener_cliente_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            return jsonify({"error": "Cliente no encontrado"}), 404
