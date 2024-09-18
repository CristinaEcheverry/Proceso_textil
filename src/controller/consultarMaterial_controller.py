from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.model.material_model import Material
from src.model.estadoMaterial_model import EstadoMaterial

class ConsultarMaterialController(FlaskController):
    @app.route("/consultarMaterial", methods=["GET", "POST"])
    def consultarMaterial():
        '''Aquí va el código para consultar los materiales, se debe obtener los materiales para mostrarlos en la vista.'''
        materiales = []
        if request.method == 'POST':
            codigo = request.form.get('codigo_material')
            producto = request.form.get('producto')
            estado_material = request.form.get('estado_material')
            
            print(f"codigo: {codigo}")
            print(f"producto: {producto}")
            print(f"estado_material: {estado_material}")

            materiales = Material.obtener_material_criterio(
                codigo=codigo,
                producto=producto,
                estado_material=estado_material,
            )
            print(materiales)
        estados_materiales= EstadoMaterial.obtener_estado_material()
        return render_template("consultarMaterial.html", material=materiales, estados_materiales=estados_materiales)
        
    @app.route('/eliminarMaterial/<int:id>', methods=['GET'])
    def eliminarMaterial(id):
        '''Aquí va el código para eliminar un material.'''
        material = Material.obtener_material_id(id)
        Material.eliminar_material(material)
        flash('Material eliminado exitosamente', 'success')
        return redirect(url_for('consultarMaterial'))
    