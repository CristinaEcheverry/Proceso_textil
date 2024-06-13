from src.app import app
from flask import render_template, request, redirect, url_for 
from src.model.material_model import Material
from src.model.enums.enum_estadoMaterial import EstadoMaterialEnum

@app.route("/ingresoMaterial", methods=["GET", "POST"])
def ingresoMaterial():
    if request.method == "POST":
        codigo = request.form.get("codigo_material")
        num_lote = request.form.get("num_lote")
        producto = request.form.get("producto")
        cantidad = request.form.get("amount")
        proveedor = request.form.get("proveedor")
        color = request.form.get("color")
        estado_material = request.form.get("estado_material")
        descripcion = request.form.get("descripcion")
        fecha_documento = request.form.get("fecha-recibido")
        nuevo_material = Material(codigo, num_lote, producto, cantidad, proveedor, color, estado_material, descripcion, fecha_documento)
        Material.agregar_material(nuevo_material)                     
        return redirect(url_for("ingresoMaterial"))
    material = Material.obtener_material()
    return render_template("ingresoMaterial_form.html", material=material, enum_estadoMaterial=EstadoMaterialEnum)
