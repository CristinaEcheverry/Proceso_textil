from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey
from src.model import session, Base

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    tipo_identificacion_id = Column(SmallInteger, ForeignKey('tipo_identificacion.id'), nullable=False)
    numero_identificacion = Column(String(15))
    nombre = Column(String(50))
    direccion = Column(String(50))
    ciudad = Column(String(40))
    telefono = Column(String(30))
    correo = Column(String(50))
    estado_pedido_id = Column(SmallInteger, ForeignKey('estado_pedido.id'), nullable=False)
    fecha_pedido = Column(Date)
    fecha_documento = Column(DateTime)
    fecha_despacho = Column(Date)
    tipo_pedido_id = Column(SmallInteger, ForeignKey('tipo_pedido.id'), nullable=False)
    #agrego prenda como llave foranea
    prenda_id = Column(Integer, ForeignKey('prenda.id'), nullable=False)
    material = Column(String(50), nullable=False)
    cantidad = Column(Float(10.3), nullable=False)

    def __init__(self, tipo_identificacion_id, numero_identificacion, nombre, direccion, ciudad, telefono, correo, estado_pedido_id, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido_id, prenda_id, material,cantidad):
        self.tipo_identificacion = tipo_identificacion_id
        self.numero_identificacion = numero_identificacion
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.correo = correo
        self.estado_pedido = estado_pedido_id
        self.fecha_pedido = fecha_pedido
        self.fecha_documento = fecha_documento
        self.fecha_despacho = fecha_despacho
        self.tipo_pedido = tipo_pedido_id
        self.prenda_id = prenda_id
        self.material = material
        self.cantidad = cantidad

    def agregar_pedido(self):
        session.add(self)
        session.commit()

    def optener_pedido(self):
        return session.query(Pedido).all()

    def modificar_pedido(self):
        session.commit()

    def eliminar_pedido(self):
        session.delete(self)
        session.commit()
    


    