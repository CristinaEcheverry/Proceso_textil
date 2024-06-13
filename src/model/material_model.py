import datetime
from sqlalchemy import Column, Float, Integer, String, Enum, DateTime
from src.model import session, Base
from src.model.enums.enum_estadoMaterial import EstadoMaterialEnum

class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(10), unique=True, nullable=False)
    num_lote = Column(String(10), nullable=False)
    producto = Column(String(50), nullable=False)
    cantidad = Column(Float, nullable=False)
    proveedor = Column(String(50), nullable=False)
    color = Column(String(20), nullable=False)
    estado_material = Column(Enum(EstadoMaterialEnum), nullable=False)
    descripcion = Column(String(300))
    fecha_documento = Column(DateTime, default=datetime.datetime.now())
    
    def __init__(self, codigo, num_lote, producto, cantidad, proveedor, color, estado_material, descripcion, fecha_documento):
        self.codigo = codigo
        self.num_lote = num_lote
        self.producto = producto
        self.cantidad = cantidad
        self.proveedor = proveedor
        self.color = color
        self.estado_material = estado_material
        self.descripcion = descripcion
        self.fecha_documento = fecha_documento

    def __str__(self):
        return f'<Material: {self.codigo} {self.estado_material}>'

    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'num_lote': self.num_lote,
            'producto': self.producto,
            'cantidad': self.cantidad,
            'proveedor': self.proveedor,
            'color': self.color,
            'estado_material': self.estado_material,
            'descripcion': self.descripcion
        }

    def agregar_material(material):
        material = session.add(material)
        session.commit()
        return material

    @staticmethod
    def obtener_material():
        material = session.query(Material).all()
        return material
    
    @staticmethod
    def obtener_material_codigo(codigo):
        material = session.query(Material).filter(Material.codigo==codigo).first()
        return material
    
    @staticmethod
    def obtener_material_id(id):
        material = session.query(Material).get(id)
        return material.to_dict()

    def modificar_material(self):
        session.commit()

    def eliminar_material():
        session.delete()
        session.commit()