from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import Base, Session

class TipoPedido(Base):
    __tablename__ = 'tipo_pedido'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(30), unique=True, nullable=False )
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.descripcion}'
    
    def agregar_tipo_pedido(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod   
    def obtener_tipo_pedido():
        session = Session()
        tipo_pedido = session.query(TipoPedido).all()
        session.close()
        return tipo_pedido
    
    @staticmethod
    def obtener_tipo_pedido_por_id(id):
        session = Session()
        tipo_pedido = session.query(TipoPedido).filter_by(id=id).first()
        session.close()
        return tipo_pedido
    
    def modificar_tipo_pedido(self):
        session = Session()
        session.query(TipoPedido).filter_by(id=self.id).update({
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()

    def eliminar_tipo_pedido(self):
        session = Session()
        session.query(TipoPedido).filter_by(id=self.id).delete()
        session.commit()
        session.close()