from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas
from src.app import app
from src.models.usuarios import Usuarios
from flask_controller import FlaskController


class IndexController(FlaskController):
    def __init__(self):
        super().__init__()

    def index():
        #Aqui puedo agregar procesos
        return render_template("index.html", title= "Proceso textil") # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 

    def login():
        return render_template("login.html", title= "Iniciar sesión")
    
    def registro():
        return render_template("registro.html", title= "Registro")
    
    def recuperarContrasena():
        return render_template("recuperarContrasena.html", title= "Recuperar contraseña")
    
    def recuperarUsuario():
        return render_template("recuperarUsuario.html", title= "Recuperar usuario")
    
    # funcion con try para los mensajes de error
    

    # def error404():
    #     return render_template("error404.html", title= "Error 404")
    
    # def error500():
    #     return render_template("error500.html", title= "Error 500")
    
    # def error503():
    #     return render_template("error503.html", title= "Error 503")
    
    # def error504():
    #     return render_template("error504.html", title= "Error 504")
    
    # def error505():
    #     return render_template("error505.html", title= "Error 505")
    
