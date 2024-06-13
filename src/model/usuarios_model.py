import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Column, Integer, String, Enum, Date, DateTime
from src.model import Base, session
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum
from src.model.enums.enum_roles import RolEnum
from src.model.enums.enum_estadoUsuario import EstadoUsuarioEnum


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    primer_nombre = Column(String(50), nullable=False)
    segundo_nombre = Column(String(50))
    primer_apellido = Column(String(50), nullable=False)
    segundo_apellido = Column(String(50))
    fecha_nacimiento = Column(Date, nullable=False)
    tipo_identificacion = Column(Enum(TipoIdentificacionEnum), nullable=False)
    identificacion = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), unique=True, nullable=False)
    rol = Column(Enum(RolEnum), nullable=False)
    status = Column(Enum(EstadoUsuarioEnum), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, tipo_identificacion, identificacion, email, password, rol, status):
        self.primer_nombre = primer_nombre
        self.segundo_nombre = segundo_nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo_identificacion = tipo_identificacion
        self.identificacion = identificacion
        self.email = email
        self.password = password
        self.rol = rol
        self.status = status

    @hybrid_property
    def fullname(self):
        f"{self.primer_nombre} {self.primer_apellido}"
        usuario = session.query(Usuarios).first()
        return print(usuario.fullname)

    def __str__(self):
        return f'<Usuario: {self.primer_nombre} {self.primer_apellido} {self.status}>'
    
    def agregar_usuario(usuario):
        usuario = session.add(usuario)
        session.commit()
        return usuario
    
    def obtener_usuarios():
        usuarios = session.query(Usuarios).all()
        return usuarios
    
    def obtener_usuario_email(email):
        usuario = session.query(Usuarios).filter(Usuarios.email==email).first()
        return usuario
    
    def obtener_usuario_identificacion(identificacion):
        usuario = session.query(Usuarios).filter(Usuarios.identificacion==identificacion).first()
        return usuario
    
    def obtener_usuario_id(id):
        usuario = session.query(Usuarios).filter(Usuarios.id==id).first()
        return usuario
    
    def obtener_usuario_rol(rol):
        usuario = session.query(Usuarios).filter(Usuarios.rol==rol).all()
        return usuario
    
    def obtener_usuario_status(status):
        usuario = session.query(Usuarios).filter(Usuarios.status==status).all()
        return usuario
    
    def modificar_usuario(self):
        session.commit()

    def eliminar_usuario(self):
        session.delete(self)
        session.commit()