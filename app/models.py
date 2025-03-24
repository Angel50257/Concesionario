from app import db
class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    anio = db.Column(db.String(4), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    disponibilidad = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f"<Vehiculo {self.marca} {self.modelo}>"
    
class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dpi = db.Column(db.String(13), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(11), nullable=False)
    
    def __repr__(self):
        return f"<Cliente {self.nombre}>"
    
class Venta(db.Model):
    __tablename__ = 'ventas'
    id = db.Column(db.Integer, primary_key=True)
    id_vehiculo = db.Column(db.Integer, db.ForeignKey('vehiculos.id'), nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    fecha_venta = db.Column(db.Date(), nullable=False)

    vehiculo = db.relationship('Vehiculo', backref='ventas', lazy=True)
    cliente = db.relationship('Cliente', backref='ventas', lazy=True)
    
    def __repr__(self):
        return f"<Venta {self.id} - Cliente {self.id_cliente} - Vehiculo {self.id_vehiculo}>"
    
