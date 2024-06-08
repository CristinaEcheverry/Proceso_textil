from enum import Enum

class TipoPedidoEnum(Enum):
    PRODUCCION = 'full'
    PATRONAJE = 'patronaje'
    DISENO = 'desing'
    CORTE = 'corte'
    CONFECCION = 'confección'