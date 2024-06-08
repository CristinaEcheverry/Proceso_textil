from src.app import app
from flask import render_template, request, redirect, url_for
from src.model.estadoPedido_model import EstadoPedido
from src.model.enums.enum_estadoPedido import EstadoPedidoEnum

@app.route('/estadoPedido', methods=['GET', 'POST'])
def estadoPedido():
    if request.method == 'POST':
        estados = request.form.get('estados')
        nuevo_estado_pedido = EstadoPedido(estados)
        EstadoPedido.agregar_estado_pedido(nuevo_estado_pedido)
        return redirect(url_for('estadoPedido'))
    estadosPedido = EstadoPedido.obtener_estado_pedido()
    return render_template('estadosPedido.html', estadosP=estadosPedido, enum_estadoPeValue=EstadoPedidoEnum)

