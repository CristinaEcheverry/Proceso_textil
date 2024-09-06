from sqlalchemy import Column, SmallInteger, Enum
from src.model import session, Base
from src.model.enums.enum_estadoPedido import EstadoPedidoEnum

class EstadoPedido(Base):
    __tablename__ = 'estado_pedido'
    id = Column(SmallInteger, primary_key=True)
    estados = Column(Enum(EstadoPedidoEnum), nullable=False)
    
    def __init__(self, estados):
        self.estados =estados

    #Serializar un enum
    def to_dict(self):
        return {
            'id': self.id,
            'estados': self.estados.value
        }
    
    def agregar_estado_pedido(self):
        session.add(self)
        session.commit()    

    @staticmethod
    def obtener_estado_pedido():
        return session.query(EstadoPedido).all()
    
    def obtener_estado_pedido_por_id(estado_id):
        return session.query(EstadoPedido).filter(EstadoPedido.id == estado_id).first()

    # def mostrar_estado_pedido(self):
    #     return session.query(EstadoPedido).filter(EstadoPedido.id == self.id).first()
    
    def modificar_estado_pedido(self):
        session.commit()

    def eliminar_estado_pedido(self):
        session.delete(self)
        session.commit()
        