from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import Base, Session

class Rol(Base):
    __annotations__ = 'rol'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(30), unique=True, nullable=False )

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.descripcion}'
    
    def agregar_rol(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod   
    def obtener_rol():
        session = Session()
        rol = session.query(rol).all()
        session.close()
        return rol
    
    @staticmethod
    def obtener_rol_por_id(id):
        session = Session()
        rol = session.query(rol).filter_by(id=id).first()
        session.close()
        return rol
    
    def modificar_rol(self):
        session = Session()
        session.query(Rol).filter_by(id=self.id).update({
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()

    def eliminar_rol(self):
        session = Session()
        session.query(Rol).filter_by(id=self.id).delete()
        session.commit()
        session.close()
    
