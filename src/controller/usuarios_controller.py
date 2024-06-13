from src.app import app
from flask import render_template, request, redirect, url_for
from src.model.usuarios_model import Usuarios
from src.model.enums.enum_tipoIden import TipoIdentificacionEnum
from src.model.enums.enum_roles import RolEnum
from src.model.enums.enum_estadoUsuario import EstadoUsuarioEnum


@app.route("/ingresoUsuario", methods=["GET", "POST"])
def ingresoUsuario():
    if request.method == "POST":
        primer_nombre = request.form.get("primer_nombre")
        segundo_nombre = request.form.get("segundo_nombre")
        primer_apellido = request.form.get("primer_apellido")
        segundo_apellido = request.form.get("segundo_apellido")
        fecha_nacimiento = request.form.get("fecha_nacimiento")
        tipo_identificacion = request.form.get("tipo_identificacion")
        identificacion = request.form.get("identificacion")
        email = request.form.get("email")
        password = request.form.get("password")
        rol = request.form.get("rol")
        status = request.form.get("status")
        nuevo_usuario = Usuarios(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, tipo_identificacion, identificacion, email, password, rol, status)
        Usuarios.agregar_usuario(nuevo_usuario)        
        return redirect(url_for("ingresoUsuario"))
    usuarios = Usuarios.obtener_usuarios()
    return render_template("crearUsuarios.html", usuarios=usuarios, enum_tipoIden=TipoIdentificacionEnum, enum_rol=RolEnum, enum_estadoUsuario=EstadoUsuarioEnum)
