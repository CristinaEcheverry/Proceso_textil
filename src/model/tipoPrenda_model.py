from sqlalchemy import Column, SmallInteger, Enum
from src.model import session, Base
from sqlalchemy.orm import relationship
from src.model.enums.enum_tipoPrenda import TipoPrendaEnum



class TipoPrenda(Base):
    __tablename__ = 'tipo_prenda'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(Enum(TipoPrendaEnum), nullable=False)

    #se relaciona con la tabla prenda
    prenda = relationship('Prenda',backref='tipo_prenda')
    
    #se crea constructor
    def __init__(self, descripcion):
        self.descripcion = descripcion

    #Serializar un enum
    def to_dict(self):
        return {
            'id': self.id,
            'descripcion': self.descripcion.value
        }

    #se hacen metodos para agregar y obtener los tipos de prendas
    def agregar_tipo_prenda(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_tipo_prendas():
        return session.query(TipoPrenda).all()

    def mostrar_tipo_prenda(self):
        return session.query(TipoPrenda).filter(TipoPrenda.id == self.id).first()

    def modificar_tipo_prenda(self):
        session.commit()

    def eliminar_tipo_prenda(self):
        session.delete(self)
        session.commit()
