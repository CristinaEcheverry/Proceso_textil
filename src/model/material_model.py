import datetime
from sqlalchemy import Column, Float, Integer, String, ForeignKey, DateTime, Enum
from src.model import session, Base
from sqlalchemy.orm import relationship, joinedload
from src.model.estadoMaterial_model import EstadoMaterial
from src.model.enums.enum_unidadMedida import UnidadMedidaEnum

class Material(Base):
    __tablename__ = 'material'
    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True, nullable=False)
    num_lote = Column(String(50), nullable=False)
    producto = Column(String(50), nullable=False)
    proveedor = Column(String(50), nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad_medida = Column(Enum(UnidadMedidaEnum), nullable=False)
    color = Column(String(50), nullable=False)
    estado_material_id = Column(Integer, ForeignKey('estado_material.id'), nullable=False)
    descripcion = Column(String(300))
    fecha_documento = Column(DateTime, default=datetime.datetime.now())
    
    #relacion con estado_material
    estado_material = relationship('EstadoMaterial', back_populates='materiales')

    def __init__(self, codigo, num_lote, producto, proveedor, cantidad, unidad_medida, color, estado_material_id, descripcion, fecha_documento):
        self.codigo = codigo
        self.num_lote = num_lote
        self.producto = producto
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.color = color
        self.estado_material_id = estado_material_id
        self.descripcion = descripcion
        self.fecha_documento = fecha_documento

    #Serializar un enum
    def to_dict(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'num_lote': self.num_lote,
            'producto': self.producto,
            'proveedor': self.proveedor,
            'cantidad': self.cantidad,
            'unidad_medida': self.unidad_medida.value,
            'color': self.color,
            'estado_material': self.estado_material_id.value,
            'descripcion': self.descripcion
        }

    def agregar_material(material):
        session.add(material)
        session.commit()

    @staticmethod
    def obtener_material():
        return session.query(Material).all()
    
    @staticmethod
    def obtener_material_criterio(codigo=None, producto=None, estado_material=None):
        query = session.query(Material).join(Material.estado_material)
        query = query.options(joinedload(Material.estado_material))
        if codigo:
            query = query.filter(Material.codigo == codigo)
        elif producto:
            query = query.filter(Material.producto == producto)
        elif estado_material:
            query = query.filter(Material.estado_material_id == estado_material)
        return query.all()
    
    @staticmethod
    def obtener_material_id(id):
        return session.query(Material).filter_by(id=id).first()

    def modificar_material(self):
        session.commit()

    def eliminar_material():
        session.delete()
        session.commit()
        