from sqlalchemy import Column, Integer, SmallInteger, String, Enum, ForeignKey
from src.model import session, Base

from src.model.tipoPrenda_model import TipoPrenda 

from sqlalchemy.orm import relationship, joinedload
# Import the necessary modules

class Prenda(Base):

    __tablename__ = 'prenda'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(50), nullable=False)
    tipo_prenda_id = Column(SmallInteger, ForeignKey('tipo_prenda.id'), nullable=False)
    
    def __init__(self, descripcion, tipo_prenda_id):
        self.descripcion = descripcion
        self.tipo_prenda_id = tipo_prenda_id

    def __repr__(self):
        return f'{self.descripcion, self.tipo_prenda_id}'

    def agregar_prenda(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_prendas():
        return session.query(Prenda).all()

    # def mostrar_prenda():
    #     result = session.query(TipoPrenda.descripcion).joinedload(Prenda, Prenda.tipo_prendas_id == TipoPrenda.id).all()
    #     return result
    
   
    # def obtener_prendas(self):
    #     # return session.query(Prenda).filter(Prenda.tipo_prenda_id == self.id).all()
        # prendas = session.query(Prenda).options(joinedload(Prenda.tipo_prenda)).all()
