from enum import Enum

class EstadoPedidoEnum(Enum):
    Devuelto = 'Devuelto'
    Abierto = 'Abierto'
    Entregado = 'Entregado'
    Cancelado = 'Cancelado'