from sqlalchemy import Column, Integer, String, Enum
from src.model import session, Base

class Prenda(Base):
    __tablename__ = 'prenda'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(50), nullable=False)
    talla = Column(Enum('XS', 'S', 'M', 'L', 'XL', 'XXL'), nullable=False)
    

    def __init__(self, descripcion, talla):
        self.descripcion = descripcion
        self.talla = talla

    def agregar_prenda(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_prendas():
        return session.query(Prenda).all()