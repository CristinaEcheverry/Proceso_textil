from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/fashionprocess")
connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

class TipoPrenda(Base):
    __tablename__ = "tipo_prenda"
    id = Column(Integer(), primary_key=True)
    tipo_prenda = Column(String(30), unique=True, nullable=False)
    prenda = Column(String(30), ForeignKey('prenda.id'),nullable=False)
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
    
class Prenda(Base):
    __tablename__ = "prenda"
    id = Column(Integer(), primary_key=True)
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


 

# class Clientes(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)    
#     nombre = db.Column(db.String(100), unique=False, nullable=False)
#     tipo_identificacion = db.Column(db.String(20), unique=False, nullable=False)
#     numero_identificacion = db.Column(db.String(20), unique=True, nullable=False)
#     direccion = db.Column(db.String(300), unique=False, nullable=False)
#     telefono = db.Column(db.String(20), unique=False, nullable=False)
