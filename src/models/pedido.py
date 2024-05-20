from sqlalchemy import Column, Integer, String, Float, ForeignKey, SmallInteger, Date, DateTime
from src.models import Base, Session

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    estado_pedido = Column(Integer, ForeignKey('estado_pedido.id'), nullable=False)
    fecha_recibido = Column(Date, nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    fecha_despacho = Column(Date, nullable=False)
    tipo_pedido = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    tipo_prenda = Column(Integer, ForeignKey('tipo_prenda.id'), nullable=False)
    prenda = Column(Integer, ForeignKey('prenda.id'), nullable=False)
    material = Column(Integer, ForeignKey('material.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    observaciones = Column(String(45), nullable=False)
    usuario = Column(Integer, ForeignKey('usuarios.id'), nullable=False)

    def __init__(self, estado_pedido, fecha_recibido, fecha_pedido, fecha_despacho, tipo_pedido, cliente, tipo_prenda, prenda, material, cantidad, observaciones, usuario):
        self.estado_pedido = estado_pedido
        self.fecha_recibido = fecha_recibido
        self.fecha_pedido = fecha_pedido
        self.fecha_despacho = fecha_despacho
        self.tipo_pedido = tipo_pedido
        self.cliente = cliente
        self.tipo_prenda = tipo_prenda
        self.prenda = prenda
        self.material = material
        self.cantidad = cantidad
        self.observaciones = observaciones
        self.usuario = usuario

    def __str__(self):
        return f'{self.estado_pedido} {self.fecha_recibido} {self.fecha_pedido} {self.fecha_despacho} {self.tipo_pedido} {self.cliente} {self.tipo_prenda} {self.prenda} {self.material} {self.cantidad} {self.observaciones} {self.usuario}'
    
    def agregar_pedido(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_pedido():
        session = Session()
        pedido = session.query(Pedido).all()
        session.close()
        return pedido
    
    @staticmethod
    def obtener_pedido_por_id(id):
        session = Session()
        pedido = session.query(Pedido).filter_by(id=id).first()
        session.close()
        return pedido
    
    def modificar_pedido(self):
        session = Session()
        session.query(Pedido).filter_by(id=self.id).update({
            'estado_pedido': self.estado_pedido,
            'fecha_recibido': self.fecha_recibido,
            'fecha_pedido': self.fecha_pedido,
            'fecha_despacho': self.fecha_despacho,
            'tipo_pedido': self.tipo_pedido,
            'cliente': self.cliente,
            'tipo_prenda': self.tipo_prenda,
            'prenda': self.prenda,
            'material': self.material,
            'cantidad': self.cantidad,
            'observaciones': self.observaciones,
            'usuario': self.usuario
        })
        session.commit()
        session.close()

    def eliminar_pedido(self):
        session = Session()
        session.query(Pedido).filter_by(id=self.id).delete()
        session.commit()
        session.close()