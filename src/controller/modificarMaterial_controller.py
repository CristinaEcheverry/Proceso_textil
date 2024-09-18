from src.app import app
from flask import render_template, request, redirect, url_for, flash
from src.model.material_model import Material
from src.model.estadoMaterial_model import EstadoMaterial
from src.model.enums.enum_unidadMedida import UnidadMedidaEnum
from flask_controller import FlaskController

class ModificarMaterialController(FlaskController):
    @app.route("/modificarMaterial", methods=['GET', 'POST'])
    def modificarMaterial():
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            producto = request.form.get('producto')
            material = Material.obtener_material_criterio(codigo, producto)
            if material:
                material_id = material[0].id
                return redirect(url_for('actualizarMaterial', id=material_id))
        return render_template('modificarMaterial_boton.html')

    @app.route("/actualizarMaterial/<int:id>", methods=['GET', 'POST'])
    def actualizarMaterial(id):
        '''Aquí va el código para modificar el material, se debe obtener el material para mostrarlo en la vista.
        La persona debe poder modificar los datos del material.'''
        material = Material.obtener_material_id(id)

        if request.method == 'POST':
            try:
                material.codigo = request.form.get('codigo_material')
                material.num_lote = request.form.get('num_lote')
                material.producto = request.form.get('producto')
                material.proveedor = request.form.get('proveedor')
                material.cantidad = request.form.get('cantidad')
                material.unidad_medida = request.form.get('unidad')
                material.color = request.form.get('color')
                material.estado_material.estado_material = request.form.get('estado_material')
                material.descripcion = request.form.get('descripcion')
                
                Material.modificar_material()
                flash('Material actualizado exitosamente', 'success')
                return redirect(url_for('actualizarMaterial', id=id))
            except Exception as e:
                flash(f'Error al actualizar el material: {str(e)}', 'error')
                return redirect(url_for('actualizarMaterial', id=id))
        estados_materiales = EstadoMaterial.obtener_estado_material()
        return render_template('modificarMaterial_form.html', m=material, estados_materiales=estados_materiales, um=UnidadMedidaEnum)
    