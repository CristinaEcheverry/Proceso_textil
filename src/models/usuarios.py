from sqlalchemy import Column, Integer, String, ForeignKey, SmallInteger, Date
from src.models import Base, Session

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuarios(Base, UserMixin):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(45), nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    nombre = Column(String(45), nullable=False)
    apellido = Column(String(45), nullable=False)
    tipo_identificacion = Column(String(45),ForeignKey('tipo_identificacion.tipo_identificacion'), nullable=False)
    num_identificacion = Column(String(45), unique=True, nullable=False)
    correo = Column(String(45), nullable=False)
    telefono = Column(String(45), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
    cargo = Column(String(45), nullable=False)
    rol = Column(String(45),ForeignKey('rol.descripcion'), nullable=False)
    estado = Column(SmallInteger, ForeignKey('estado_usuario.id'), nullable=False)

    def __init__(self, username, password, nombre, apellido, tipo_identificacion, num_identificacion, correo, telefono, fecha_nacimiento, fecha_ingreso, cargo, rol, estado):
        self.username = username
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_identificacion = tipo_identificacion
        self.num_identificacion = num_identificacion
        self.correo = correo
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso = fecha_ingreso
        self.cargo = cargo
        self.rol = rol
        self.estado = estado

    def __str__(self):
        return f'{self.username} {self.password} {self.nombre} {self.apellido} {self.tipo_identificacion} {self.num_identificacion} {self.correo} {self.telefono} {self.fecha_nacimiento} {self.fecha_ingreso} {self.cargo} {self.rol} {self.estado}'
    
    def agregar_usuario(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()

    @staticmethod
    def obtener_usuario():
        session = Session()
        usuario = session.query(Usuarios).all()
        session.close()
        return usuario
    
    @staticmethod
    def obtener_usuario_por_id(id):
        session = Session()
        usuario = session.query(Usuarios).filter_by(id=id).first()
        session.close()
        return usuario
    
    def modificar_usuario(self):
        session = Session()
        session.query(Usuarios).filter_by(id=self.id).update({
            'username': self.username,
            'password': self.password,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'tipo_identificacion': self.tipo_identificacion,
            'num_identificacion': self.num_identificacion,
            'correo': self.correo,
            'telefono': self.telefono,
            'fecha_nacimiento': self.fecha_nacimiento,
            'fecha_ingreso': self.fecha_ingreso,
            'cargo': self.cargo,
            'rol': self.rol,
            'estado': self.estado
        })
        session.commit()
        session.close()

    def eliminar_usuario(self):
        session = Session()
        session.query(Usuarios).filter_by(id=self.id).delete()
        session.commit()
        session.close()


    @classmethod
    def check_password(self, hashed_password,password):
        return check_password_hash(hashed_password, password)
    
# print(generate_password_hash('1234Jk')) # para generar la contraseña encriptada

