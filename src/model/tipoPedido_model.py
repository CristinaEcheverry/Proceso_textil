from sqlalchemy import Column, SmallInteger, Enum, String
from src.model import session, Base
from src.model.enums.enum_tipoPedido import TipoPedidoEnum
from sqlalchemy.orm import relationship

class TipoPedido(Base):
    __tablename__ = 'tipo_pedido'
    id = Column(SmallInteger, primary_key=True)
    tipo_pedido = Column(Enum(TipoPedidoEnum), nullable=False)
    
    
    #se crea relacion con tabla pedidos
    pedido = relationship('Pedido',backref='tipo_pedido')

    def __init__(self, tipo_pedido):
        self.tipo_pedido = tipo_pedido

    def __repr__(self):
        return f'{self.tipo_pedido}'
    
    def agregar_tipo_pedido(self):
        session.add(self)
        session.commit()    

    @staticmethod
    def obtener_tipo_pedido():
        return session.query(TipoPedido).all()
    
    def mostrar_tipo_pedido(self):
        return session.query(TipoPedido).filter(TipoPedido.id == self.id).first()
    
    def modificar_tipo_pedido(self):
        session.commit()

    def eliminar_tipo_pedido(self):
        session.delete(self)
        session.commit()