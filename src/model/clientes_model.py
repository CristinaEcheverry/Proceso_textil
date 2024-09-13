from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey
from src.model import session, Base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, joinedload
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.tipoPersona_model import TipoPersona

class Clientes(Base, SerializerMixin):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    tipo_identificacion_id = Column(SmallInteger, ForeignKey('tipo_identificacion.id'), nullable=False)
    numero_identificacion = Column(String(15), unique=True, nullable=False)
    tipo_persona_id = Column(SmallInteger, ForeignKey('tipo_persona.id'), nullable=False)
    nombre = Column(String(50), nullable=False)
    direccion = Column(String(50), nullable=False)
    ciudad = Column(String(40), nullable=False)
    telefono = Column(String(30), nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    
    #relacion con tabla tipo_identificacion
    tipo_identificacion = relationship('TipoIdentificacion', backref='clientes')
    #relacion con tabla tipo_persona
    tipo_persona = relationship('TipoPersona', backref='clientes')

    def __init__(self, tipo_identificacion_id, numero_identificacion, tipo_persona_id, nombre, direccion, ciudad, telefono, correo):
        self.tipo_identificacion_id = tipo_identificacion_id
        self.numero_identificacion = numero_identificacion
        self.tipo_persona_id = tipo_persona_id
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.correo = correo

    def to_dict(self):
        return {
            "id": self.id,
            "tipo_identificacion": self.tipo_identificacion.codigo.value,
            "numero_identificacion": self.numero_identificacion,
            "tipo_persona_id": self.tipo_persona_id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "ciudad": self.ciudad,
            "telefono": self.telefono,
            "correo": self.correo
        }

    def agregar_cliente(cliente):
        cliente = session.add(cliente)
        session.commit()
        return cliente

    def obtener_cliente():
        cliente = session.query(Clientes).all()
        return cliente
    
    def obtener_cliente_id(id):
        return session.query(Clientes).filter_by(id=id).first()
    
    def obtener_cliente_numeroId(numeroId):
        clientes = session.query(Clientes).filter_by(numero_identificacion=numeroId).options(
            joinedload(Clientes.tipo_identificacion),
            joinedload(Clientes.tipo_persona)).one_or_none()
        if clientes:
            return {"cliente": 
                    [{"id": clientes.id, 
                    "nombre": clientes.nombre, 
                    "direccion": clientes.direccion, 
                    "ciudad": clientes.ciudad, 
                    "telefono": clientes.telefono, 
                    "correo": clientes.correo}],
                    "tipo_identificacion_id":
                    [{"id": clientes.tipo_identificacion.id,
                    "codigo": clientes.tipo_identificacion.codigo}],
                    "numero_identificacion": clientes.numero_identificacion,
                    "tipo_persona_id": 
                    [{"id": clientes.tipo_persona.id, 
                    "tipo_persona": clientes.tipo_persona.tipo_persona}]
                    }
        else:
            return None 

    def obtener_cliente_criterio(tipo_identificacion=None, num_identificacion=None, nombre=None):
        query = session.query(Clientes).join(Clientes.tipo_identificacion).join(Clientes.tipo_persona)
        query = query.options(joinedload(Clientes.tipo_identificacion),joinedload(Clientes.tipo_persona))
        if tipo_identificacion:
            query = query.filter(TipoIdentificacion.codigo == tipo_identificacion)
        elif num_identificacion:
            query = query.filter(Clientes.numero_identificacion == num_identificacion)
        elif nombre:
            query = query.filter(Clientes.nombre == nombre)
        return query.all()

    def modificar_cliente():
        '''Función que actualiza el cliente.'''
        session.commit()

    def eliminar_cliente(self):
        session.delete(self)
        session.commit()
