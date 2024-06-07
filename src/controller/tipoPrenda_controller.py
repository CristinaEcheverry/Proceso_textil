from src.app import app
#Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for 
from src.model.tipoPrenda_model import TipoPrenda

@app.route('/tipo_prendas', methods=['GET', 'POST'])
def tipo_prendas():
    if request.method == 'POST':
        descripcion = request.form.get('nombre')
        nuevo_tipo = TipoPrenda(descripcion)
        TipoPrenda.agregar_tipo_prenda(nuevo_tipo)
        return redirect(url_for('tipo_prendas'))
    tipos = TipoPrenda.obtener_tipo_prendas()
    return render_template('crearTipoPrenda.html', tipos=tipos)