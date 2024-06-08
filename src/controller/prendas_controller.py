from src.app import app
#Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for 
# render_template es para usar las vistas
# request es para obtener los datos de la petición
# redirect es para redireccionar a una ruta
# url_for es para obtener la url de una ruta
from src.model.tipoPrenda_model import TipoPrenda, TipoPrendaEnum
from src.model.prenda_model import Prenda

@app.route('/prendas', methods=['GET', 'POST'])
def prendas():
    if request.method == 'POST':
        descripcion = request.form.get('nombre-prenda')
        tipo_prenda_id = int(request.form.get('tipo_prenda_id'))
        nueva_prenda = Prenda(descripcion, tipo_prenda_id)
        Prenda.agregar_prenda(nueva_prenda)
        return redirect(url_for('prendas'))
    tipos = TipoPrenda.obtener_tipo_prendas()
    prendas = Prenda.obtener_prendas()
    return render_template('prendas.html', tipos=tipos, prendas=prendas, enum_values=TipoPrendaEnum)