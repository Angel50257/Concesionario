from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Cliente

# Definir el Blueprint
clientes_bp = Blueprint('clientes', __name__)

# Página principal - Lista de clientes
@clientes_bp.route('/customer')
def index():
    clientes = Cliente.query.all()
    return render_template('index2.html', clientes=clientes)

# Formulario para agregar cliente
@clientes_bp.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        nombre = request.form['nombre']
        dpi = request.form['dpi']
        correo = request.form['correo']
        telefono = request.form['telefono']

        nuevo_cliente = Cliente(nombre=nombre, dpi=dpi, correo=correo, telefono=telefono)
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('add_customer.html')

# Formulario para editar cliente
@clientes_bp.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.dpi = request.form['dpi']
        cliente.correo = request.form['correo']
        cliente.telefono = request.form['telefono']

        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('edit_customer.html', cliente=cliente)

# Eliminar cliente
@clientes_bp.route('/delete_customer/<int:id>', methods=['GET'])
def delete_customer(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes.index'))