from sqlalchemy import Column,Integer, SmallInteger, String, Enum, ForeignKey
from src.model import session, Base


class TipoPrenda(Base):
    __tablename__ = 'tipo_prenda'
    id = Column(SmallInteger, primary_key=True)
    descripcion = Column(Enum('Prendas superiores', 'Prendas inferiores','Prendas interiores', 'Vestidos', 'Overoles', 'Tela'), nullable=False)
    #agrego prenda como llave foranea
    prenda_id = Column(Integer, ForeignKey('prenda.id'), nullable=False)

    def __init__(self, descripcion, prenda_id):
        self.descripcion = descripcion
        self.prenda_id = prenda_id

    def agregar_tipo_prenda(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_tipo_prendas():
        return session.query(TipoPrenda).all()