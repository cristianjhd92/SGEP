from app import db

class Obra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    ubicacion = db.Column(db.String(255), nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    maestro_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    estado = db.Column(db.String(50), default='En progreso')  # En progreso, Finalizada, etc.

    supervisor = db.relationship('User', foreign_keys=[supervisor_id])
    maestro = db.relationship('User', foreign_keys=[maestro_id])
