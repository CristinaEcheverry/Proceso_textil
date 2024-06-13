from enum import Enum

class EstadoUsuarioEnum(Enum):
    Activo = 'activo'
    Inactivo = 'inactivo'
    Bloqueado = 'bloqueado'
    Eliminado = 'eliminado'