from enum import Enum

class RolEnum(Enum):
    Administrador = 'admin'
    JefeConfeccion = 'jefe_confeccion'
    JefeCorte = 'jefe_corte'
    jefeDiseño = 'jefe_diseño'
    jefePatronaje = 'jefe_patronaje'
    JefeAlmacen = 'jefe_almacen'
    JefeProduccion = 'jefe_produccion'
    JefeVentas = 'jefe_ventas'
    JefeCompras = 'jefe_compras'
    auxConfeccion = 'aux_confeccion'
    auxCorte = 'aux_corte'
    auxDiseño = 'aux_diseño'
    auxPatronaje = 'aux_patronaje'
    auxAlmacen = 'aux_almacen'
    auxProduccion = 'aux_produccion'
    auxVentas = 'aux_ventas'
    auxCompras = 'aux_compras'
    User = 'user'

