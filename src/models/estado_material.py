from sqlalchemy import Column, String, SmallInteger
from src.models import Base, Session

class EstadoMaterial(Base):
    __tablename__ = 'estado_material'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(String(30), unique=True, nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return f'{self.descripcion}'
    
    def agregar_estado_material(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_estado_material():
        session = Session()
        estado_material = session.query(EstadoMaterial).all()
        session.close()
        return estado_material
    
    @staticmethod
    def obtener_estado_material_por_id(id):
        session = Session()
        estado_material = session.query(EstadoMaterial).filter_by(id=id).first()
        session.close()
        return estado_material
    
    def modificar_estado_material(self):
        session = Session()
        session.query(EstadoMaterial).filter_by(id=self.id).update({
            'descripcion': self.descripcion
        })
        session.commit()
        session.close()
    
    def eliminar_estado_material(self):
        session = Session()
        session.query(EstadoMaterial).filter_by(id=self.id).delete()
        session.commit()
        session.close()
     