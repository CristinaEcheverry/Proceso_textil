from app import app
# from model import * -> Aquí se tiene que importar todos los modelos o clases
from flask import render_template  # render_template es para usar las vistas

@app.route("/") # El "/" -> hace referencia a la pagna de inicio
def index():
    #Aqui puedo agregar procesos
    # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 
    return render_template("index.html", title= "Proceso textil") 