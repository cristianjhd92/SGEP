from app import db
from datetime import datetime

class Evidencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obra_id = db.Column(db.Integer, db.ForeignKey('obra.id'), nullable=False)
    subido_por = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # Antes, Durante, Después
    filepath = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_subida = db.Column(db.DateTime, default=datetime.utcnow)
    aprobada = db.Column(db.Boolean, default=False)
    aprobada_por = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    fecha_aprobacion = db.Column(db.DateTime, nullable=True)
    
    obra = db.relationship('Obra', backref='evidencias')
    usuario = db.relationship('User', foreign_keys=[subido_por])
    aprobador = db.relationship('User', foreign_keys=[aprobada_por])
