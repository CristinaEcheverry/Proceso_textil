from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey
from src.model import session, Base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

class Clientes(Base, SerializerMixin):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    tipo_identificacion_id = Column(SmallInteger, ForeignKey('tipo_identificacion.id'), nullable=False)
    numero_identificacion = Column(String(15), unique=True, nullable=False)
    tipo_persona = Column(SmallInteger, ForeignKey('tipo_persona.id'), nullable=False)
    nombre = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)
    ciudad = Column(String(40), nullable=False)
    telefono = Column(String(30), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    
    tipo_identificacion = relationship('TipoIdentificacion', backref='clientes')
    
    def __init__(self, tipo_identificacion_id, numero_identificacion, tipo_persona, nombre, direccion, ciudad, telefono, correo):
        self.tipo_identificacion_id = tipo_identificacion_id
        self.numero_identificacion = numero_identificacion
        self.tipo_persona = tipo_persona
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.correo = correo

    def to_dict(self):
        return {
            "id": self.id,
            "numero_identificacion": self.numero_identificacion,
            "tipo_persona": self.tipo_persona,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "telefono": self.telefono,
            "correo": self.correo,
            "tipo_identificacion": self.tipo_identificacion.to_dict()
        }

    def agregar_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente

    def obtener_cliente():
        cliente = session.query(Clientes).all()
        return cliente
    
    def obtener_cliente_id(id):
        cliente = session.query(Clientes).filter_by(id=id).first()
        return cliente.to_dict()

    def modificar_cliente(self):
        session.commit()

    def eliminar_cliente():
        session.delete()
        session.commit()
