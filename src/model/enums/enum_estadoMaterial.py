from enum import Enum

class EstadoMaterialEnum(Enum):
    ACTIVO = 1
    INACTIVO = 2
    BLOQUEADO = 3
    ELIMINADO = 4
    PENDIENTE = 5
    EN_PROCESO = 6
    FINALIZADO = 7
    CANCELADO = 8
    RECHAZADO = 9
    APROBADO = 10
    ENVIADO = 11
    RECIBIDO = 12
    DEVUELTO = 13
    REPARADO = 14
    REEMPLAZADO = 15
    DESCARTADO = 16
    DISPONIBLE = 17
    NO_DISPONIBLE = 18
    EN_USO = 19
    EN_REPARACION = 20
    EN_REEMPLAZO = 21
    EN_DESCARTE = 22
    EN_DESUSO = 23
    EN_MANTENIMIENTO = 24
    EN_REVISION = 25
    EN_TRASLADO = 26
    EN_REUBICACION = 27
    EN_LIMPIEZA = 28
    EN_CALIBRACION = 29
    EN_CALIFICACION = 30
    EN_VALIDACION = 31
    EN_VERIFICACION = 32
    EN_CERTIFICACION = 33
    EN_ETIQUETADO = 34
    
    def __int__(self):
        return self.value
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def from_string(value):
        return EstadoMaterial[value]

    