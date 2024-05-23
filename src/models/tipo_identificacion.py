from sqlalchemy import Column, SmallInteger, String, Enum
from src.models import Base, Session

class TipoIdentificacion(Base):
    __tablename__ = 'tipo_identificacion'
    id = Column(SmallInteger, primary_key=True)
    tipo_identificacion = Column(Enum('CC', 'CE', 'TI','PA', 'NIT', 'RUT', 'OTRO'))
    descripcion = Column(String(40))
    
    def __init__(self, tipo_identificacion, descripcion):
        self.tipo_identificacion = tipo_identificacion
        self.descripcion = descripcion

    def __str__(self): # esta funcion es para que cuando se imprima el objeto se muestre de esta manera
        return f'{self.tipo_identificacion} {self.descripcion}'

    def agregar_tipo_identificacion(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_tipo_identificacion():
        session = Session()
        tipo_identificacion = session.query(TipoIdentificacion).all()
        session.close()
        return tipo_identificacion

    @staticmethod
    def obtener_tipo_identificacion_por_id(id):
        session = Session()
        tipo_identificacion = session.query(TipoIdentificacion).filter_by(id=id).first()
        session.close()
        return tipo_identificacion

    def modificar_tipo_identificacion(self):
        session = Session()
        session.query(TipoIdentificacion).filter_by(id=self.id).update({
            'tipo_identificacion': self.tipo_identificacion,
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()