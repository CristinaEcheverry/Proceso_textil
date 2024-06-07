from src.app import app
from flask import render_template, request, redirect, url_for 
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum

@app.route('/tipoIdent', methods=['GET', 'POST'])
def tipoIdent():
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        descripcion = request.form.get('descripcion')
        nuevo_tipo_ident = TipoIdentificacion(codigo, descripcion)
        TipoIdentificacion.agregar_tipo_identificacion(nuevo_tipo_ident)
        return redirect(url_for('tipoIdent'))
    identificacion = TipoIdentificacion.obtener_tipo_identificacion()
    return render_template('tipoIdent.html', identificaciones=identificacion, enum_idValue= TipoIdentificacionEnum)