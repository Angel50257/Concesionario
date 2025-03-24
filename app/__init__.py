from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configuration import Config

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.vehiculos import vehiculos_bp
    app.register_blueprint(vehiculos_bp)
    
    from app.clientes import clientes_bp
    app.register_blueprint(clientes_bp)
    
    from app.ventas import ventas_bp
    app.register_blueprint(ventas_bp)
    
    from app.buscar import buscar_bp
    app.register_blueprint(buscar_bp)

    return app