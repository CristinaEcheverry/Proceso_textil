from sqlalchemy import Column, SmallInteger, Enum
from src.model import session, Base
# from src.model.prenda_model import Prenda
from enum import Enum as enum

from sqlalchemy.orm import relationship, joinedload

class TipoPrendaEnum(enum):
    SUPERIORES = 1
    INFERIORES = 2
    INTERIORES = 3
    VESTIDOS = 4
    OVEROLES = 5
    TELA = 6

class TipoPrenda(Base):
    __tablename__ = 'tipo_prenda'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(Enum(TipoPrendaEnum), nullable=False)

    #se relaciona con la tabla prenda
    prenda = relationship('Prenda',backref='tipo_prenda')
    
    #se crea constructor
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __repr__(self):
        return f'{self.descripcion}'

    #se hacen metodos para agregar y obtener los tipos de prendas
    def agregar_tipo_prenda(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_tipo_prendas():
        return session.query(TipoPrenda).all()

    def mostrar_tipo_prenda(self):
        return session.query(TipoPrenda).filter(TipoPrenda.id == self.id).first()
