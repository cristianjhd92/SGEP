from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

# Inicializar extensiones
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Redirige al login si el usuario no está autenticado

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar base de datos y autenticación
    db.init_app(app)
    login_manager.init_app(app)

    # Importar modelos aquí para evitar errores de importación circular
    from app.models.user import User

    # Configurar la función para cargar usuarios
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Importar y registrar Blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.dashboard import dash_bp
    from app.routes.evidences import evidence_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(dash_bp, url_prefix='/dashboard')
    app.register_blueprint(evidence_bp, url_prefix='/evidences')

    return app
