from flask import Blueprint, render_template, request
from app import db
from app.models import Vehiculo, Cliente

buscar_bp = Blueprint('buscar', __name__)

@buscar_bp.route('/search', methods=['GET'])
def buscar():
    # Filtros para vehículos
    vehiculo_id = request.args.get('vehiculo_id', '').strip()
    marca = request.args.get('marca', '').strip()
    modelo = request.args.get('modelo', '').strip()
    anio = request.args.get('anio', '').strip()
    precio = request.args.get('precio', '').strip()
    disponibilidad = request.args.get('disponibilidad', '')

    vehiculos_query = Vehiculo.query
    if vehiculo_id:
        vehiculos_query = vehiculos_query.filter(Vehiculo.id == vehiculo_id)
    if marca:
        vehiculos_query = vehiculos_query.filter(Vehiculo.marca.ilike(f"%{marca}%"))
    if modelo:
        vehiculos_query = vehiculos_query.filter(Vehiculo.modelo.ilike(f"%{modelo}%"))
    if anio:
        vehiculos_query = vehiculos_query.filter(Vehiculo.anio == anio)
    if precio:
        vehiculos_query = vehiculos_query.filter(Vehiculo.precio <= precio)
    if disponibilidad:
        if disponibilidad == "1":
            vehiculos_query = vehiculos_query.filter(Vehiculo.disponibilidad == True)
        elif disponibilidad == "0":
            vehiculos_query = vehiculos_query.filter(Vehiculo.disponibilidad == False)


    vehiculos = vehiculos_query.all()

    # Filtros para clientes
    cliente_id = request.args.get('cliente_id', '').strip()
    nombre = request.args.get('nombre', '').strip()
    dpi = request.args.get('dpi', '').strip()

    clientes_query = Cliente.query
    if cliente_id:
        clientes_query = clientes_query.filter(Cliente.id == cliente_id)
    if nombre:
        clientes_query = clientes_query.filter(Cliente.nombre.ilike(f"%{nombre}%"))
    if dpi:
        clientes_query = clientes_query.filter(Cliente.dpi == dpi)

    clientes = clientes_query.all()

    return render_template('index4.html', vehiculos=vehiculos, clientes=clientes)
