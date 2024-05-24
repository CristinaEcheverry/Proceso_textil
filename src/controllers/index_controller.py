from flask import render_template, request, redirect, url_for, flash  # render_template es para usar las vistas
from src.app import app, engine
from src.models.usuarios import Usuarios
from src.models.Model_user import ModelUser
from flask_controller import FlaskController
from flask_login import LoginManager, login_user, login_required, logout_user


class IndexController(FlaskController):
    def __init__(self):
        super().__init__()


    @LoginManager.usuarios_loader
    def load_user(id):
        return ModelUser.obtener_usuario_por_id(engine, id)

    @app.route("/")
    def index():
        #Aqui puedo agregar procesos
        return redirect(url_for('login')) # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":            
            usuario = Usuarios(request.form["usuario"], request.form["password"])
            usuario_login = ModelUser.login(engine, usuario)
            if usuario_login != None:
                if usuario_login.password:
                    login_user(usuario_login)
                    return redirect(url_for("mainPage"))
                else:
                    flash("Contraseña incorrecta")
                    return redirect(url_for("index"))
            else:
                flash("Usuario no encontrado")
                return redirect(url_for("index"))
        return render_template("login.html", title= "Iniciar sesión")
    

    @app.route("/cerrar_sesion")
    def cerrar_sesion():
        logout_user()
        return redirect(url_for("index"))
    
    # ejemplo proteger una ruta
    @app.route("/protected")
    @login_required
    def protected():
        return "<h1> Protected route</h1>"
    
    # funcion con try para los mensajes de error

    def error401(error):
        return redirect(url_for("index"))

    def error404(error):
        return "<h1> Página no encontrada</h1>", 404
    