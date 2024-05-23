from sqlalchemy import Column, String, ForeignKey, SmallInteger
from src.models import Base, Session

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(SmallInteger, primary_key=True)
    tipo_cliente = Column(String(30), nullable=False)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    tipo_identificacion = Column(String(45),ForeignKey('tipo_identificacion.tipo_identificacion'), nullable=False)
    num_identificacion = Column(String(45), nullable=False)
    direccion = Column(String(45), nullable=False)
    ciudad = Column(String(45), nullable=False)
    correo = Column(String(45), nullable=False)
    telefono = Column(String(45), nullable=False)

    def __init__(self, tipo_cliente, nombre, apellido, tipo_identificacion, num_identificacion, direccion, ciudad, correo, telefono):
        self.tipo_cliente = tipo_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_identificacion = tipo_identificacion
        self.num_identificacion = num_identificacion
        self.direccion = direccion
        self.ciudad = ciudad
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'{self.tipo_cliente} {self.nombre} {self.apellido} {self.tipo_identificacion} {self.num_identificacion} {self.direccion} {self.ciudad} {self.correo} {self.telefono}'
    
    def agregar_cliente(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_cliente():
        session = Session()
        cliente = session.query(Cliente).all()
        session.close()
        return cliente
    
    @staticmethod

    def obtener_cliente_por_id(id):
        session = Session()
        cliente = session.query(Cliente).filter_by(id=id).first()
        session.close()
        return cliente
    
    def modificar_cliente(self):
        session = Session()
        session.query(Cliente).filter_by(id=self.id).update({
            'tipo_cliente': self.tipo_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'tipo_identificacion': self.tipo_identificacion,
            'num_identificacion': self.num_identificacion,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'correo': self.correo,
            'telefono': self.telefono
        })
        session.commit()
        session.close()

    def eliminar_cliente(self):
        session = Session()
        session.query(Cliente).filter_by(id=self.id).delete()
        session.commit()
        session.close()

        
