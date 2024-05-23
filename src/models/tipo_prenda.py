from sqlalchemy import Column, SmallInteger, String,ForeignKey
from src.models import Base, Session

class TipoPrenda(Base):
    __tablename__ = "tipo_prenda"
    id = Column(SmallInteger, primary_key=True)
    tipo_prenda = Column(String(30), unique=True, nullable=False)
    prenda = Column(String(30), ForeignKey('prenda.prenda'),nullable=False)

    def __init__(self, tipo_prenda, prenda):
        self.tipo_prenda = tipo_prenda
        self.prenda = prenda

    def  agregar_tipo_prenda(tipo_prenda):
        session = Session()
        tipo_prenda = session.add(tipo_prenda)
        session.commit()
        return tipo_prenda
    
    def obtener_tipo_prenda():
        session = Session()
        tipo_prenda = session.query(TipoPrenda).all()
        return tipo_prenda
    
    def obtener_tipo_prenda_por_id(id):
        session = Session()
        tipo_prenda = session.query(TipoPrenda).get(id)
        return tipo_prenda
    
    def actualizar_tipo_prenda(id, tipo_prenda):
        session = Session()
        tipo_prenda = session.query(TipoPrenda).get(id)
        session.commit()
        return tipo_prenda
    
    def eliminar_tipo_prenda(id):
        session = Session()
        tipo_prenda = session.query(TipoPrenda).get(id)
        session.delete(tipo_prenda)
        session.commit()
        return tipo_prenda