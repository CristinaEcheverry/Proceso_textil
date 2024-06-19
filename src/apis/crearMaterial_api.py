#creo el servicio para traer un material
from flask_restful import Resource
from flask import request, jsonify

#model
from src.model.material_model import Material

class CrearMaterialApi(Resource):

    def get(self):
        return jsonify({"message": "Hola mundo"})
    
    def post(self):
        material = Material(codigo=request.json['codigo'],
                            num_lote=request.json['num_lote'],
                            producto=request.json['producto'],
                            cantidad=request.json['cantidad'],
                            proveedor=request.json['proveedor'],
                            color=request.json['color'],
                            estado_material=request.json['estado_material'],
                            descripcion=request.json['descripcion'],
                            fecha_documento=request.json['fecha_documento'])
        try:
            Material.agregar_material(material)
        except RuntimeError:
            return jsonify({"message": "Error material repetido"}), 409
        except Exception as e:
            return jsonify({"message": "Error al guardar el material"}), 500
        return jsonify({"message": "Material agregado correctamente"}), 200
        # return "Producto almacenado correctamente", 200
        
        # def get(self):
        #     material = Material.obtener_material()
        #     return jsonify(material)
            
    
        # def post(self):#permite almacenar en la base de datos
        #     codigo = request.json.get("codigo_material")
        #     num_lote = request.json.get("num_lote")
        #     producto = request.json.get("producto")
        #     cantidad = request.json.get("amount")
        #     proveedor = request.json.get("proveedor")
        #     color = request.json.get("color")
        #     estado_material = request.json.get("estado_material")
        #     descripcion = request.json.get("descripcion")
        #     fecha_documento = request.json.get("fecha-recibido")
        #     nuevo_material = Material(codigo, num_lote, producto, cantidad, proveedor, color, estado_material, descripcion, fecha_documento)
        #     Material.agregar_material(nuevo_material)
        #     return jsonify({"message": "Material agregado correctamente"}), 200