from src.app import app
from flask import render_template, request, redirect, url_for
from src.model.clientes_model import Clientes
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.tipoPersona_model import TipoPersona

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


#manejo de errores
#cuando esta duplicado un dato
# @app.errorhandler(1062)
# def handle_error(error):
#     try:
#       print("Entrada duplicada", error)
#     except Exception as ex:
#         print("")
    
