from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Vehiculo

# Definir el Blueprint
vehiculos_bp = Blueprint('vehiculo', __name__)

# Página principal - Lista de vehiculos
@vehiculos_bp.route('/car')
def index():
    vehiculos = Vehiculo.query.all()
    return render_template('index.html', vehiculos=vehiculos)

# Formulario para agregar vehiculo
@vehiculos_bp.route('/add_car', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        anio = request.form['anio']
        precio = request.form['precio']
        disponibilidad = request.form['disponibilidad'] == '1'

        nuevo_vehiculo = Vehiculo(marca=marca, modelo=modelo, anio=anio, precio=precio, disponibilidad=disponibilidad)
        db.session.add(nuevo_vehiculo)
        db.session.commit()
        return redirect(url_for('vehiculo.index'))

    return render_template('add_car.html')

# Formulario para editar vehiculo
@vehiculos_bp.route('/edit_car/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    vehiculo = Vehiculo.query.get_or_404(id)

    if request.method == 'POST':
        vehiculo.marca = request.form['marca']
        vehiculo.modelo = request.form['modelo']
        vehiculo.anio = request.form['anio']
        vehiculo.precio = request.form['precio']
        vehiculo.disponibilidad = request.form['disponibilidad'] == '1'

        db.session.commit()
        return redirect(url_for('vehiculo.index'))

    return render_template('edit_car.html', vehiculo=vehiculo)

# Eliminar vehiculo
@vehiculos_bp.route('/delete_car/<int:id>', methods=['GET'])
def delete_car(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return redirect(url_for('vehiculo.index'))