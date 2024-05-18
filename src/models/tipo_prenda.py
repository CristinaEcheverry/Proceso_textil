from sqlalchemy import Column, Integer, String, Float, ForeignKey
from src.models import Base, Session

class TipoPrenda(Base):
    __tablename__ = "tipo_prenda"
    id = Column(Integer(), primary_key=True)
    tipo_prenda = Column(String(30), unique=True, nullable=False)
    prenda = Column(String(30), ForeignKey('prenda.prenda'),nullable=False)
    # id = Column(Integer, primary_key=True)
    # descripcion = Column(String(300), unique=True, nullable=False)
    # unidad_medida = Column(String(3), unique=False, nullable=False)
    # cantidad_stock = Column(Integer, unique=False, nullable=False)
    # valor_unitario = Column(Float(10,8))
    # categoria = Column(Integer, ForeignKey('categorias.id'),nullable=False)

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