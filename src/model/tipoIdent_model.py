from sqlalchemy import Column, SmallInteger, Enum, String
from src.model import session, Base
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum


class TipoIdentificacion(Base):
    __tablename__ = 'tipo_identificacion'
    id = Column(SmallInteger, primary_key=True)
    codigo = Column(Enum(TipoIdentificacionEnum), nullable=False)
    nameIdent = Column(String(50), nullable=False)

    def __init__(self, codigo, nameIdent):
        self.codigo = codigo
        self.nameIdent = nameIdent

    def to_dict(self):
        return {
            "id": self.id,
            "codigo": self.codigo.value,
            "nameIdent": self.nameIdent
        }

    def agregar_tipo_identificacion(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_tipo_identificacion():
        return session.query(TipoIdentificacion).all()

    @staticmethod
    def obtener_tipo_identificacion_id(id):
        return session.query(TipoIdentificacion).filter_by(id=id).first()

    def mostrar_tipo_identificacion(self):
        return session.query(TipoIdentificacion).filter_by(id=self.id).first()

    def modificar_tipo_identificacion(self):
        session.commit()

    def eliminar_tipo_identificacion(self):
        session.delete(self)
        session.commit()
