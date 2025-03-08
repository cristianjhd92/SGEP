from app import create_app
from flask import redirect, url_for
from flask_login import current_user

app = create_app()

# Definir ruta raíz explícita
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.home'))  # Redirige al dashboard
    return redirect(url_for('auth.login'))  # Si no está autenticado, lo lleva al login

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)