from src.app import app
from flask_controller import FlaskController 
from flask import render_template, request, redirect, url_for 
from src.model.material_model import Material
from src.model.estadoMaterial_model import EstadoMaterial
from src.model.enums.enum_unidadMedida import UnidadMedidaEnum
from flask_restful import Api
import datetime

#importo mi api
from src.apis.crearMaterial_api import CrearMaterialApi

class CrearMaterial(FlaskController):
    api = Api(app)

    # aqui creo una ruta para hacer el llamado a mi api
    api.add_resource(CrearMaterialApi, "/api/crearMaterial") 

    @app.route("/ingresoMaterial", methods=["GET", "POST"])
    def ingresoMaterial():
        if request.method == "POST":
            codigo = request.form.get("codigo_material")
            num_lote = request.form.get("num_lote")
            producto = request.form.get("producto")
            proveedor = request.form.get("proveedor")
            cantidad = request.form.get("amount")
            unidad_medida = request.form.get("unidad")
            color = request.form.get("color")
            estado_material = request.form.get("estado_material")
            descripcion = request.form.get("descripcion")
            fecha_documento = datetime.datetime.now()
            nuevo_material = Material(codigo, num_lote, producto, proveedor, cantidad, unidad_medida, color, estado_material, descripcion, fecha_documento)
            Material.agregar_material(nuevo_material)                     
            return redirect(url_for("ingresoMaterial"))
        material = Material.obtener_material()
        estados_material = EstadoMaterial.obtener_estado_material()
        return render_template("ingresoMaterial_form.html", material=material, estadoMaterial=estados_material, u_m=UnidadMedidaEnum)
