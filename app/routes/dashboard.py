from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Blueprint de Dashboard
dash_bp = Blueprint('dashboard', __name__)

@dash_bp.route('/admin')
@login_required
def admin_dashboard():
    if current_user.rol != 'Administrador':
        return "Acceso no autorizado", 403
    return render_template('dashboard/admin.html')

@dash_bp.route('/supervisor')
@login_required
def supervisor_dashboard():
    if current_user.rol != 'Supervisor':
        return "Acceso no autorizado", 403
    return render_template('dashboard/supervisor.html')

@dash_bp.route('/maestro')
@login_required
def maestro_dashboard():
    if current_user.rol != 'Maestro de Obra':
        return "Acceso no autorizado", 403
    return render_template('dashboard/maestro.html')
