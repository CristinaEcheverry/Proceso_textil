# from flask_sqlalchemy import SQLAlchemy


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#   pass

# class Productos(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     descripcion = db.Column(db.String(300), unique=True, nullable=False)
#     unidad_medida = db.Column(db.String(3), unique=False, nullable=False)
#     cantidad_stock = db.Column(db.Integer, unique=False, nullable=False)
#     precio = db.Column(db.Integer, unique=False, nullable=False)
    
#     def __init__(self) -> None:
#         pass
    
#     def past(self):
#         return a+s
    
# class Clientes(db.Model):
    
#     id = db.Column(db.Integer, primary_key=True)    
#     nombre = db.Column(db.String(100), unique=False, nullable=False)
#     tipo_identificacion = db.Column(db.String(20), unique=False, nullable=False)
#     numero_identificacion = db.Column(db.String(20), unique=True, nullable=False)
#     direccion = db.Column(db.String(300), unique=False, nullable=False)
#     telefono = db.Column(db.String(20), unique=False, nullable=False)
