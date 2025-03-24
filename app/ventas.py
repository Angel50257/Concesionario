from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Venta

# Definir el Blueprint
ventas_bp = Blueprint('ventas', __name__)

# Página principal - Lista de ventas
@ventas_bp.route('/sale')
def index():
    ventas = Venta.query.all()
    return render_template('index3.html', ventas=ventas)

# Formulario para agregar venta
@ventas_bp.route('/add_sale', methods=['GET', 'POST'])
def add_sale():
    if request.method == 'POST':
        id_vehiculo = request.form['id_vehiculo']
        id_cliente = request.form['id_cliente']
        fecha_venta = request.form['fecha_venta']

        nuevo_venta = Venta(id_vehiculo=id_vehiculo, id_cliente=id_cliente, fecha_venta=fecha_venta)
        db.session.add(nuevo_venta)
        db.session.commit()
        return redirect(url_for('ventas.index'))

    return render_template('add_sale.html')

# Formulario para editar venta
@ventas_bp.route('/edit_sale/<int:id>', methods=['GET', 'POST'])
def edit_sale(id):
    venta = Venta.query.get_or_404(id)

    if request.method == 'POST':
        venta.id_vehiculo = request.form['id_vehiculo']
        venta.id_cliente = request.form['id_cliente']
        venta.fecha_venta = request.form['fecha_venta']

        db.session.commit()
        return redirect(url_for('ventas.index'))

    return render_template('edit_sale.html', venta=venta)

# Eliminar venta
@ventas_bp.route('/delete_sale/<int:id>', methods=['GET'])
def delete_sale(id):
    venta = Venta.query.get_or_404(id)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('ventas.index'))