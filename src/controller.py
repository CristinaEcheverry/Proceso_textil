from app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template  # render_template es para usar las vistas

@app.route("/") # El "/" -> hace referencia a la pagna de inicio
def index():
    #Aqui puedo agregar procesos
    return render_template("Index.html", title= "Pagina Principal") # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 

@app.route("/Formulario")
def formulario():
    return render_template("Formulario.html", title= "Crear Padido")

@app.route("/Logueo")
def logueo():
    return render_template("Logueo.html", title= "Logueo")