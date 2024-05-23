from sqlalchemy import Column, Integer, String
from src.models import Base, Session


class Prenda(Base):
    __tablename__ = "prenda"
    id = Column(Integer, primary_key=True)
    prenda = Column(String(30), unique=True, nullable=False)

    def __init__(self, prenda):
        self.prenda = prenda
    
    def agregar_prenda(prenda):
        session = Session()
        prenda = session.add(prenda)
        session.commit()
        return prenda
    
    def obtener_prenda():
        session = Session()
        prenda = session.query(Prenda).all()
        return prenda