from sqlalchemy import Column, SmallInteger, Enum
from src.model import session, Base
from sqlalchemy.orm import relationship
from src.model.enums.enum_tipoPersona import TipoPersonaEnum

class TipoPersona(Base):
    __tablename__ = 'tipo_persona'
    id = Column(SmallInteger, primary_key=True)
    tipo_persona = Column(Enum(TipoPersonaEnum), nullable=False)

    #se crea relacion con tabla clientes
    cliente = relationship('Clientes',backref='clientes_tipo_persona')
    
    def __init__(self, tipo_persona):
        self.tipo_persona = tipo_persona

    def __repr__(self):
        return f'{self.tipo_persona}'

    def agregar_tipo_persona(self):
        session.add(self)
        session.commit()    

    @staticmethod
    def obtener_tipo_persona():
        return session.query(TipoPersona).all()
    
    @staticmethod
    def obtener_tipo_persona_id(id):
        return session.query(TipoPersona).get(id)
    
    def mostrar_tipo_persona(self):
        return session.query(TipoPersona).filter(TipoPersona.id == self.id).first()
    
    def modificar_tipo_persona(self):
        session.commit()

    def eliminar_tipo_persona(self):
        session.delete(self)
        session.commit()