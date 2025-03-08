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

    if not User.query.filter_by(cedula='987654321').first():
        usuario = User(
            cedula='987654321', 
            nombre='Superv Test', 
            rol='Supervisor',
            password_hash=generate_password_hash('supervisor123')  # Contraseña segura
        )
        db.session.add(usuario)
        db.session.commit()
        print("Usuario supervisor creado correctamente.")
    else:
        print("El usuario supervisor ya existe.")

    if not User.query.filter_by(cedula='654321987').first():
        usuario = User(
            cedula='654321987', 
            nombre='Maestro Test', 
            rol='Maestro de obra',
            password_hash=generate_password_hash('maestro123')  # Contraseña segura
        )
        db.session.add(usuario)
        db.session.commit()
        print("Usuario maestro creado correctamente.")

    else:
        print("El usuario maestro ya existe.")

    
