from sqlalchemy import Column, Integer, Enum
from src.model import Base, session
from src.model.enums.enum_estadoMaterial import EstadoMaterialEnum
from sqlalchemy.orm import relationship

class EstadoMaterial(Base):
    __tablename__ = 'estado_material'
    id = Column(Integer, primary_key=True)
    estado_material = Column(Enum(EstadoMaterialEnum), nullable=False)

    #relacion con tabla material
    materiales = relationship('Material', back_populates='estado_material')

    def __init__(self, estado_material):
        self.estado_material = estado_material
    
    def to_dict(self):  
        return {
            'id': self.id,
            'estado_material': self.estado_material.value
        }
    
    def obtener_estado_material():
        return session.query(EstadoMaterial).all()
    