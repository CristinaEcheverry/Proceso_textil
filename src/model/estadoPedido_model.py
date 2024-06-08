from sqlalchemy import Column, SmallInteger, Enum
from src.model import session, Base
from src.model.enums.enum_estadoPedido import EstadoPedidoEnum
from sqlalchemy.orm import relationship

class EstadoPedido(Base):
    __tablename__ = 'estado_pedido'
    id = Column(SmallInteger, primary_key=True)
    estados = Column(Enum(EstadoPedidoEnum), nullable=False)
    
    #se crea relacion con tabla pedidos
    pedido = relationship('Pedido',backref='estado_pedido')

    def __init__(self, estados):
        self.estados =estados

    def __repr__(self):
        return f'{self.estados}'
    
    def agregar_estado_pedido(self):
        session.add(self)
        session.commit()    

    @staticmethod
    def obtener_estado_pedido():
        return session.query(EstadoPedido).all()
    
    def mostrar_estado_pedido(self):
        return session.query(EstadoPedido).filter(EstadoPedido.id == self.id).first()
    
    def modificar_estado_pedido(self):
        session.commit()

    def eliminar_estado_pedido(self):
        session.delete(self)
        session.commit()