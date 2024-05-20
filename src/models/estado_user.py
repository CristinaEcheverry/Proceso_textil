from sqlalchemy import Column, SmallInteger, String
from src.models import Base, Session

class EstadoUser(Base):
    __tablaname__ = 'estado_user'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(String(30), unique=True, nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.descripcion}'
    
    def agregar_estado_user(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_estado_user():
        session = Session()
        estado_user = session.query(EstadoUser).all()
        session.close()
        return estado_user
    
    @staticmethod
    def obtener_estado_user_por_id(id):
        session = Session()
        estado_user = session.query(EstadoUser).filter_by(id=id).first()
        session.close()
        return estado_user
    
    def modificar_estado_user(self):
        session = Session()
        session.query(EstadoUser).filter_by(id=self.id).update({
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()

    def eliminar_estado_user(self):
        session = Session()
        session.query(EstadoUser).filter_by(id=self.id).delete()
        session.commit()
        session.close()
        