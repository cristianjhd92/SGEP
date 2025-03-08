from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.user import User
from functools import wraps

# Blueprint de administración
admin_bp = Blueprint('admin', __name__)

# Verificar que solo administradores accedan
def admin_required(f):
    def wrap(*args, **kwargs):
        if current_user.rol != 'Administrador':
            flash('Acceso no autorizado', 'danger')
            return redirect(url_for('dashboard.admin_dashboard'))
        return f(*args, **kwargs)
    return login_required(wrap)

@admin_bp.route('/usuarios', methods=['GET'])
@admin_required
def listar_usuarios():
    usuarios = User.query.all()
    return render_template('admin/usuarios.html', usuarios=usuarios)

@admin_bp.route('/usuarios/nuevo', methods=['GET', 'POST'])
@admin_required
def crear_usuario():
    if request.method == 'POST':
        cedula = request.form['cedula']
        nombre = request.form['nombre']
        rol = request.form['rol']
        password = request.form['password']
        
        if User.query.filter_by(cedula=cedula).first():
            flash('La cédula ya está registrada', 'danger')
            return redirect(url_for('admin.crear_usuario'))
        
        usuario = User(cedula=cedula, nombre=nombre, rol=rol)
        usuario.set_password(password)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario creado exitosamente', 'success')
        return redirect(url_for('admin.listar_usuarios'))
    
    return render_template('admin/nuevo_usuario.html')

@admin_bp.route('/usuarios/eliminar/<int:id>', methods=['POST'])
@admin_required
def eliminar_usuario(id):
    usuario = User.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado', 'success')
    return redirect(url_for('admin.listar_usuarios'))
