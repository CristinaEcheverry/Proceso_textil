from sqlalchemy import Column, Integer, String
from src.models import Base, Session

class EstadoPedido(Base):
    __tablename__ = 'estado_pedido'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(30), unique=True, nullable=False )
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.descripcion}'
    
    def agregar_estado_pedido(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod   
    def obtener_estado_pedido():
        session = Session()
        estado_pedido = session.query(EstadoPedido).all()
        session.close()
        return estado_pedido
    
    @staticmethod
    def obtener_estado_pedido_por_id(id):
        session = Session()
        estado_pedido = session.query(EstadoPedido).filter_by(id=id).first()
        session.close()
        return estado_pedido
    
    def modificar_estado_pedido(self):
        session = Session()
        session.query(EstadoPedido).filter_by(id=self.id).update({
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()

    def eliminar_estado_pedido(self):
        session = Session()
        session.query(EstadoPedido).filter_by(id=self.id).delete()
        session.commit()
        session.close()