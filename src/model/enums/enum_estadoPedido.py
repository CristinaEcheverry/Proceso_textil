from enum import Enum

class EstadoPedidoEnum(Enum):
    Devuelto = 1
    Abierto = 2
    Entregado = 3
    Cancelado = 4