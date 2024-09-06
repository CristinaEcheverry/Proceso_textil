from sqlalchemy import Column, Float, SmallInteger, Integer, String, Enum, Date, DateTime, ForeignKey, func, or_
from src.model import session, Base
from sqlalchemy.orm import relationship, joinedload
from src.model.clientes_model import Clientes
from src.model.tipoIdent_model import TipoIdentificacion
from src.model.estadoPedido_model import EstadoPedido

class Pedido(Base):
    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    numero_pedido = Column(String(10), nullable=False)
    clientes_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    estado_pedido_id = Column(SmallInteger, ForeignKey('estado_pedido.id'), nullable=False)
    fecha_pedido = Column(Date)
    fecha_documento = Column(DateTime)
    fecha_despacho = Column(Date)
    tipo_pedido_id = Column(SmallInteger, ForeignKey('tipo_pedido.id'), nullable=False)

    #relacion con tabla clientes
    clientes = relationship('Clientes', backref='pedido')
    #relacion con tabla Detalle_pedido
    detalle_pedido = relationship('PedidoDetalle', backref='pedido')
    #relacion con tabla estado_pedido
    estado_pedido = relationship('EstadoPedido', backref='pedido')
    #relacion con tabla tipo_pedido
    tipo_pedido = relationship('TipoPedido', backref='pedido')

    def __init__(self, numero_pedido, clientes_id, estado_pedido_id, 
    fecha_pedido, fecha_documento, fecha_despacho, tipo_pedido_id):    # tipo_prenda_id, prenda_id, material,cantidad
        self.numero_pedido = numero_pedido
        self.clientes_id = clientes_id
        self.estado_pedido_id = estado_pedido_id
        self.fecha_pedido = fecha_pedido
        self.fecha_documento = fecha_documento
        self.fecha_despacho = fecha_despacho
        self.tipo_pedido_id = tipo_pedido_id

    #serializar los datos de pedido
    def to_dict(self):
        return {
            "id": self.id,
            "numero_pedido": self.numero_pedido,
            "clientes_id": self.clientes_id,
            "estado_pedido_id": self.estado_pedido_id,
            "fecha_pedido": self.fecha_pedido,
            "fecha_documento": self.fecha_documento,
            "fecha_despacho": self.fecha_despacho,
            "tipo_pedido_id": self.tipo_pedido_id
        }

    def agregar_pedido(self):
        session.add(self)
        session.commit()

    @staticmethod
    def obtener_pedido():
        return session.query(Pedido).all()
    
    @staticmethod
    def obtener_pedido_id(id):
        return session.query(Pedido).filter_by(id=id).first()
    
    def obtener_pedido_dato(numero_pedido):
        pedido = session.query(Pedido).filter_by(numero_pedido=numero_pedido).options(
            joinedload(Pedido.clientes),
            joinedload(Pedido.estado_pedido),
            joinedload(Pedido.tipo_pedido),
            joinedload(Pedido.detalle_pedido)).one_or_none()   
        
        if pedido:
            return {"pedido": [{"id": pedido.id, "numero_pedido": pedido.numero_pedido,
            "fecha_pedido": pedido.fecha_pedido,
            "fecha_documento": pedido.fecha_documento,
            "fecha_despacho": pedido.fecha_despacho,
            "tipo_pedido_id": pedido.tipo_pedido_id}],
            "clientes_id": [{"tipo_identificacion":pedido.clientes.tipo_identificacion_id,"numero_identificacion": pedido.clientes.numero_identificacion,"nombre":pedido.clientes.nombre, "direccion": pedido.clientes.direccion, "ciudad": pedido.clientes.ciudad, "telefono": pedido.clientes.telefono, "correo": pedido.clientes.correo}],
            "estado_pedido": pedido.estado_pedido_id,
            "tipo_pedido": pedido.tipo_pedido_id,
            "detalles": [{"tipo_prenda_id": detalle.tipo_prenda_id, "prenda_id": detalle.prenda_id, "material": detalle.material,"cantidad": detalle.cantidad} for detalle in pedido.detalle_pedido]
            }
        else:
            return None  

    def modificar_pedido(self):
        '''Función que actualiza el pedido.'''
        for pedido in self:
            session.update(pedido)
        session.commit()

    def eliminar_pedido(self):
        '''Función que elimina el pedido.'''
        session.delete(self)
        session.commit()

    @staticmethod
    def obtener_ultimo_id():
        ultimo_id = session.query(func.max(Pedido.id)).scalar()
        return ultimo_id if ultimo_id is not None else 0

    
class PedidoDetalle(Base):
    __tablename__ = 'pedido_detalle'
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'), nullable=False)
    tipo_prenda_id = Column(SmallInteger, ForeignKey('tipo_prenda.id'), nullable=False)
    prenda_id = Column(Integer, ForeignKey('prenda.id'), nullable=False)
    material = Column(String(50), nullable=False)
    cantidad = Column(Float(10.3), nullable=False)

    def __init__(self, pedido_id, tipo_prenda_id, prenda_id, material, cantidad):
        self.pedido_id = pedido_id
        self.tipo_prenda_id = tipo_prenda_id
        self.prenda_id = prenda_id
        self.material = material
        self.cantidad = cantidad

    #serializar los datos de pedido_detalle
    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "tipo_prenda_id": self.tipo_prenda_id,
            "prenda_id": self.prenda_id,
            "material": self.material,
            "cantidad": self.cantidad
        }

    def agregar_detalle(self):
        session.add(self)
        session.commit()

    def obtener_pedido_detalle():
        return session.query(PedidoDetalle).options(joinedload(PedidoDetalle.pedido).joinedload(Pedido.clientes)).all()
        # return session.query(PedidoDetalle).all()

    @staticmethod
    def obtener_detalle(pedido_id):
        return session.query(PedidoDetalle).filter_by(pedido_id=pedido_id).all()

    #una función que recibe cualquier dato(numero de pedido y/o numero identificación y/o fechas, etc) y lo busca en la tabla pedido_detalle
    @staticmethod
    def obtener_detalle_por_criterio(tipo_identificacion=None, num_identificacion=None, nombre=None, estado_pedido_id=None, num_pedido=None, fecha_pedido=None, fecha_despacho=None):
        query = session.query(Pedido).join(Pedido.clientes).join(Pedido.estado_pedido)
    
        # Incluye las relaciones en la carga de la consulta
        query = query.options(joinedload(Pedido.clientes).joinedload(Clientes.tipo_identificacion), joinedload(Pedido.estado_pedido))
        if num_pedido:
            query = query.filter(Pedido.numero_pedido == num_pedido)
        if tipo_identificacion:
            query = query.filter(TipoIdentificacion.codigo == tipo_identificacion)
        if num_identificacion:
            query = query.filter(Clientes.numero_identificacion == num_identificacion)
        if nombre:
            query = query.filter(Clientes.nombre == nombre)
        if estado_pedido_id:
            query = query.filter(EstadoPedido.estados == estado_pedido_id)
        if fecha_pedido:
            query = query.filter(Pedido.fecha_pedido == fecha_pedido)
        if fecha_despacho:
            query = query.filter(Pedido.fecha_despacho == fecha_despacho)

        return query.all()

    def modificar_detalle(self):
        '''Función que modifica el detalle del pedido.'''
        for pedido in self:
            session.dirty(pedido)
            # session.new(pedido)
        session.commit()

    def eliminar_pedido_detalle(self):
        '''Función que elimina el detalle pedido y el pedido.'''
        for pedido in self:
            session.delete(pedido)
        session.commit() 
