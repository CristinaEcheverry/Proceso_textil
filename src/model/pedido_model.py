from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey, func
from src.model import session, Base

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    numero_pedido = Column(String(10), nullable=False)
    clientes_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    estado_pedido_id = Column(SmallInteger, ForeignKey('estado_pedido.id'), nullable=False)
    fecha_pedido = Column(Date)
    fecha_documento = Column(DateTime)
    fecha_despacho = Column(Date)
    tipo_pedido_id = Column(SmallInteger, ForeignKey('tipo_pedido.id'), nullable=False)

    def __init__(self, numero_pedido, clientes_id, estado_pedido_id, fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido_id):    # tipo_prenda_id, prenda_id, material,cantidad
        self.numero_pedido = numero_pedido
        self.clientes_id = clientes_id
        self.estado_pedido_id = estado_pedido_id
        self.fecha_pedido = fecha_pedido
        self.fecha_documento = fecha_documento
        self.fecha_despacho = fecha_despacho
        self.tipo_pedido_id = tipo_pedido_id

    def agregar_pedido(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_pedido():
        return session.query(Pedido).all()
    
    @staticmethod
    def obtener_pedido_id(id):
        return session.query(Pedido).filter_by(id=id).first()

    def modificar_pedido(self):
        session.commit()

    def eliminar_pedido(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def obtener_ultimo_id():
        ultimo_id = session.query(func.max(Pedido.id)).scalar()
        return ultimo_id if ultimo_id is not None else 0

    
class PedidoDetalle(Base):
    __tablename__ = 'pedido_detalle'
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'), nullable=False)
    tipo_prenda_id = Column(SmallInteger, ForeignKey('tipo_prenda.id'), nullable=False)
    prenda_id = Column(Integer, ForeignKey('prenda.id'), nullable=False)
    material = Column(String(50), nullable=False)
    cantidad = Column(Float(10.3), nullable=False)

    def __init__(self, pedido_id, tipo_prenda_id, prenda_id, material, cantidad):
        self.pedido_id = pedido_id
        self.tipo_prenda_id = tipo_prenda_id
        self.prenda_id = prenda_id
        self.material = material
        self.cantidad = cantidad

    def agregar_detalle(self):
        session.add(self)
        session.commit()
