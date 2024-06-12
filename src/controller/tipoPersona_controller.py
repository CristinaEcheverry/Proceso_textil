from src.app import app
from flask import render_template, request, redirect, url_for
from src.model.tipoPersona_model import TipoPersona
from src.model.enums.enum_tipoPersona import TipoPersonaEnum

@app.route('/tipoPersona', methods=['GET', 'POST'])
def tipoPersona():
    if request.method == 'POST':
        tipo_persona = request.form.get('tipo_persona')
        nuevo_tipo_persona = TipoPersona(tipo_persona)
        TipoPersona.agregar_tipo_persona(nuevo_tipo_persona)
        return redirect(url_for('tipoPersona'))
    tiposPersona = TipoPersona.obtener_tipo_persona()
    return render_template('tipoPersona.html', tipoP=tiposPersona, enum_tipoPersona=TipoPersonaEnum)