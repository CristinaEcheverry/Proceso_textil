from src.app import app
from flask import render_template, request, redirect, url_for 
from src.model.tipoPedido_model import TipoPedido
from src.model.enums.enum_tipoPedido import TipoPedidoEnum

@app.route('/tipoPedido', methods=['GET', 'POST'])
def tipoPedido():
    if request.method == 'POST':
        tipo_pedido = request.form.get('tipo_pedido')
        nuevo_tipo_pedido = TipoPedido(tipo_pedido)
        TipoPedido.agregar_tipo_pedido(nuevo_tipo_pedido)
        return redirect(url_for('tipoPedido'))
    tiposPedido = TipoPedido.obtener_tipo_pedido()
    return render_template('tiposPedido.html', tipoP=tiposPedido, enum_tipoPeValue= TipoPedidoEnum)