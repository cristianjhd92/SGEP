from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models.evidencia import Evidencia
from app.models.obra import Obra
import os

# Blueprint de evidencias
evidence_bp = Blueprint('evidences', __name__)

UPLOAD_FOLDER = 'static/uploads/'

@evidence_bp.route('/subir', methods=['GET', 'POST'])
@login_required
def subir_evidencia():
    if current_user.rol != 'Maestro de Obra':
        return "Acceso no autorizado", 403
    
    if request.method == 'POST':
        obra_id = request.form['obra_id']
        tipo = request.form['tipo']
        descripcion = request.form.get('descripcion', '')
        file = request.files['file']
        
        if file and file.filename:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            
            evidencia = Evidencia(
                obra_id=obra_id,
                subido_por=current_user.id,
                tipo=tipo,
                filepath=filepath,
                descripcion=descripcion
            )
            db.session.add(evidencia)
            db.session.commit()
            flash('Evidencia subida exitosamente', 'success')
            return redirect(url_for('evidences.subir_evidencia'))
        
    obras = Obra.query.all()
    return render_template('evidences/subir.html', obras=obras)

@evidence_bp.route('/revisar', methods=['GET'])
@login_required
def revisar_evidencias():
    if current_user.rol != 'Supervisor':
        return "Acceso no autorizado", 403

    evidencias = Evidencia.query.all()  # Filtrar por estado 'pendiente' si es necesario
    return render_template('evidences/revisar.html', evidencias=evidencias)

@evidence_bp.route('/aprobar/<int:id>', methods=['POST'])
@login_required
def aprobar_evidencia(id):
    if current_user.rol != 'Supervisor':
        return "Acceso no autorizado", 403
    
    evidencia = Evidencia.query.get_or_404(id)
    evidencia.aprobada = True
    evidencia.aprobada_por = current_user.id
    db.session.commit()
    flash('Evidencia aprobada', 'success')
    return redirect(url_for('evidences.revisar_evidencias'))

@evidence_bp.route('/rechazar/<int:id>', methods=['POST'])
@login_required
def rechazar_evidencia(id):
    if current_user.rol != 'Supervisor':
        return "Acceso no autorizado", 403
    
    evidencia = Evidencia.query.get_or_404(id)
    db.session.delete(evidencia)
    db.session.commit()
    flash('Evidencia rechazada', 'danger')
    return redirect(url_for('evidences.revisar_evidencias'))
