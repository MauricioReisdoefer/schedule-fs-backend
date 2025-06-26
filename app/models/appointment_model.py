from db import db

class Appointment(db.Table):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullale=True)
    data = db.Column(db.DateTime, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 
    user = db.relationship('User', back_populates='appointments')