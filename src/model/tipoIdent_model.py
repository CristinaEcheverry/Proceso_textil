from sqlalchemy import Column, SmallInteger, Enum, String
from src.model import session, Base
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum
from sqlalchemy.orm import relationship


class TipoIdentificacion(Base):
    __tablename__ = 'tipo_identificacion'
    id = Column(SmallInteger, primary_key=True)
    codigo = Column(Enum(TipoIdentificacionEnum), nullable=False)
    nameIdent = Column(String(50), nullable=False)

    #se crea relacion con tabla pedidos
    pedido = relationship('Pedido',backref='tipo_identificacion')

    def __init__(self, codigo,nameIdent):
        self.codigo = codigo
        self.nameIdent =nameIdent

    def __repr__(self):
        return f'{self.nameIdent}'
    
    def agregar_tipo_identificacion(self):
        session.add(self)
        session.commit()    

    @staticmethod
    def obtener_tipo_identificacion():
        return session.query(TipoIdentificacion).all()
    
    def mostrar_tipo_identificacion(self):
        return session.query(TipoIdentificacion).filter(TipoIdentificacion.id == self.id).first()
    
    def modificar_tipo_identificacion(self):
        session.commit()

    def eliminar_tipo_identificacion(self):
        session.delete(self)
        session.commit()