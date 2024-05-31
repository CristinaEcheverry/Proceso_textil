from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey
from src.model import session, Base

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    tipo_identificacion = Column(Enum('C.C', 'C.E', 'NIT'))
    numero_identificacion = Column(String(15))
    nombre = Column(String(50))
    direccion = Column(String(50))
    ciudad = Column(String(40))
    telefono = Column(String(30))
    correo = Column(String(50))
    estado_pedido = Column(Enum('En proceso', 'Abierto', 'Cerrado', 'Cancelado'))
    fecha_pedido = Column(Date)
    fecha_documento = Column(DateTime)
    fecha_despacho = Column(Date)
    tipo_pedido = Column(Enum('Producción', 'Patronaje', 'Diseño', 'Corte', 'Confección' ), nullable=False)
    #agrego tipo_prenda como llave foranea
    tipo_prenda_id = Column(SmallInteger, ForeignKey('tipo_prenda.id'), nullable=False)
    #agrego prenda como llave foranea
    prenda_id = Column(Integer, ForeignKey('prenda.id'), nullable=False)
    material = Column(String(50), nullable=False)
    cantidad = Column(Float(10.3), nullable=False)

    def __init__(self, tipo_identificacion, numero_identificacion, nombre, direccion, ciudad, telefono, correo, estado_pedido, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido, tipo_prenda_id, prenda_id, material,cantidad):
        self.tipo_identificacion = tipo_identificacion
        self.numero_identificacion = numero_identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.correo = correo
        self.estado_pedido = estado_pedido
        self.fecha_pedido = fecha_pedido
        self.fecha_documento = fecha_documento
        self.fecha_despacho = fecha_despacho
        self.tipo_pedido = tipo_pedido
        self.tipo_prenda_id = tipo_prenda_id
        prenda_id = prenda_id
        material = material
        self.cantidad = cantidad

    def agregar_pedido(self):
        session.add(self)
        session.commit()
    


    