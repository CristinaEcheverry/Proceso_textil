from app import app
from model import TipoPrenda, Prenda # Aquí se tiene que importar todos los modelos o clases
from flask import render_template, request, redirect, url_for  # render_template es para usar las vistas


@app.route("/") # El "/" -> hace referencia a la pagna de inicio
def index():
    #Aqui puedo agregar procesos
    return render_template("index.html", title= "Proceso textil") # el primer argumento es el que llama a la vista o template, el 2° argumento es el parametro que se traslada 

@app.route("/mainPage")
def mainPage():
    return render_template("mainPage.html", title= "Página Principal")

@app.route("/crearPedido")
def crearPedido():
    return render_template("crearPedido_form.html", title= "Crear pedido")

@app.route("/modificarPedido")
def modificarPedido():
    return render_template("modificarPedido_form.html", title= "Modificar pedido")

@app.route("/consultarPedido")
def consultarPedido():
    return render_template("consultarPedido_form.html", title= "Consultar pedido")

@app.route("/ingresarMateriales")
def ingresoMaterial():
    return render_template("ingresoMaterial_form.html", title= "Ingresar material")

@app.route("/modificarRefMeaterial")
def modificarRefMeaterial():
    return render_template("modificarRefMeaterial_form.html", title= "Modifica Meaterial")

@app.route("/consultarMaterial")
def consultarMaterial():
    return render_template("consultarMaterial_form.html", title= "Consultar Material")
    
@app.route("/crearCliente")
def crearCliente():
    return render_template("crearCliente.html", title= "CrearCliente")


@app.route("/crearTipoPrenda", methods=['GET','POST'])
def crearTipoPrenda():
    if request.method == 'POST':
        tipo_prenda = request.form.get('tipo_prenda')
        prenda = request.form.get('prenda')
        tipo_prenda = TipoPrenda(tipo_prenda,prenda)
        TipoPrenda.agregar_tipo_prenda(tipo_prenda)
        return redirect(url_for('tipo_prenda'))
    prenda = Prenda.obtener_prenda()
    return render_template("crearTipoPrenda.html", prenda=prenda)

@app.route("/tipo_prenda")
def tipo_prenda():
    tipo_prenda = TipoPrenda.obtener_tipo_prenda()
    return render_template("tipo_prenda.html",tipo_prenda=tipo_prenda)

@app.route("/crearPrenda", methods=['GET','POST'])
def crearPrenda():
    if request.method == 'POST': #si la info que llega viene de un formulario guardarlo en la db
        prenda = request.form.get('prenda')
        tipo_prenda = request.form.get('tipo_prenda')
        prenda = Prenda(prenda,tipo_prenda)
        Prenda.agregar_prenda(prenda)
        return redirect(url_for('prendas'))
    tipo_prenda = TipoPrenda.obtener_tipo_prenda()
    return render_template("crearPrenda.html", tipo_prenda=tipo_prenda)

@app.route("/prendas")
def prendas():
    prendas = Prenda.obtener_prenda()
    return render_template("prendas.html",prendas=prendas)
