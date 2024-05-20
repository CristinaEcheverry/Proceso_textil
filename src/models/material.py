from sqlalchemy import Column, Integer, String, ForeignKey, Float, SmallInteger, Date, DateTime
from src.models import Base, Session

class Materiales(Base):
    __tablename__ = 'materiales'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(45), nullable=False)
    estado_material = Column(SmallInteger, ForeignKey('estado_material.id'), nullable=False)

    def __init__(self, nombre, descripcion, estado_material):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado_material = estado_material

    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.estado_material}'
    
    def agregar_material(self):

        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_material():
        session = Session()
        material = session.query(Materiales).all()
        session.close()
        return material
    
    @staticmethod
    def obtener_material_por_id(id):
        session = Session()
        material = session.query(Materiales).filter_by(id=id).first()
        session.close()
        return material
    

    def modificar_material(self):
        session = Session()
        session.query(Materiales).filter_by(id=self.id).update({
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'estado_material': self.estado_material
        })
        session.commit()
        session.close()

    def eliminar_material(self):
        session = Session()
        session.query(Materiales).filter_by(id=self.id).delete()
        session.commit()
        session.close()