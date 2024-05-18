from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from app import app
from flask_controller import FlaskController


class IndexController(FlaskController):
    def __init__(self):
        super().__init__()

    def index():
        #Aqui puedo agregar procesos
        return render_template("index.html", title= "Proceso textil") # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 
