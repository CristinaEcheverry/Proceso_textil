from sqlalchemy import Column, Integer, ForeignKey, Date
from src.models import Base, Session

class Despacho(Base):
    __tablename__ = 'despacho'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date, nullable=False)
    num_pedido = Column(Integer, ForeignKey('pedido.id'), nullable=False)

    def __init__(self, fecha, num_pedido):
        self.fecha = fecha
        self.num_pedido = num_pedido

    def __str__(self):
        return f'{self.fecha} {self.num_pedido}'
    
    def agregar_despacho(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_despacho():
        session = Session()
        despacho = session.query(Despacho).all()
        session.close()
        return despacho
    
    @staticmethod
    def obtener_despacho_por_id(id):
        session = Session()
        despacho = session.query(Despacho).filter_by(id=id).first()
        session.close()
        return despacho
    
    def modificar_despacho(self):
        session = Session()
        session.query(Despacho).filter_by(id=self.id).update({
            'fecha': self.fecha,
            'num_pedido': self.num_pedido
        })
        session.commit()
        session.close()

    def eliminar_despacho(self):
        session = Session()
        session.query(Despacho).filter_by(id=self.id).delete()
        session.commit()
        session.close()