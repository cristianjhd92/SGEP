from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

# Inicialización de la base de datos
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = "Por favor inicia sesión para acceder."


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    
    # Registrar Blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.dashboard import dash_bp
    from app.routes.evidences import evidence_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(dash_bp, url_prefix='/dashboard')
    app.register_blueprint(evidence_bp, url_prefix='/evidences')
    
    return app
