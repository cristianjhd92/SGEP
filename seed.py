from app import create_app, db
from app.models.user import User
from werkzeug.security import generate_password_hash

# Inicializar la aplicación Flask
app = create_app()

with app.app_context():
    # Verificar si el usuario administrador ya existe
    if not User.query.filter_by(cedula='123456789').first():
        usuario = User(
            cedula='123456789', 
            nombre='Admin Test', 
            rol='Administrador',
            password_hash=generate_password_hash('admin123')  # Contraseña segura
        )
        db.session.add(usuario)
        db.session.commit()
        print("Usuario administrador creado correctamente.")
    else:
        print("El usuario administrador ya existe.")
