from flask_restful import Resource
from flask import request, jsonify

from flask_cors import cross_origin

from src.model.prenda_model import Prenda

class PrendasApi(Resource):  
    
    @cross_origin()   
    def post(self):
        prenda = Prenda(codigo=request.json['codigo'],
                        descripcion=request.json['descripcion'],
                        tipo_prenda_id=request.json['tipo_prenda_id'])
        try:
            Prenda.agregar_prenda(prenda)
        except RuntimeError:
            return jsonify({"message": "Error material repetido"}), 409
        except Exception as e:
            return jsonify({"message": "Error al guardar el material"}), 500
        return jsonify({"message": "Material agregado correctamente"}), 200
    
    def get(self):
        prendas = Prenda.obtener_prendas()
        prendas_result = []
        for prenda in prendas:
            prendas_result.append(prenda.to_dict())            
        return prendas_result