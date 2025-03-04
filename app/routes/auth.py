from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models.user import User
from werkzeug.security import check_password_hash

# Blueprint de autenticación
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cedula = request.form['cedula']
        password = request.form['password']
        rol = request.form['rol']
        
        user = User.query.filter_by(cedula=cedula, rol=rol).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Inicio de sesión exitoso', 'success')
            
            # Redirigir al dashboard según el rol
            if user.rol == 'Administrador':
                return redirect(url_for('dashboard.admin_dashboard'))
            elif user.rol == 'Supervisor':
                return redirect(url_for('dashboard.supervisor_dashboard'))
            elif user.rol == 'Maestro de Obra':
                return redirect(url_for('dashboard.maestro_dashboard'))
            
        else:
            flash('Credenciales incorrectas', 'danger')
    
    return render_template('auth/login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('auth.login'))
