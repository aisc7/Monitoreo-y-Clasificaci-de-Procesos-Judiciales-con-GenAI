from app import db
from datetime import datetime

class Case(db.Model):
    __tablename__ = 'cases'

    id = db.Column(db.Integer, primary_key=True)
    case_number = db.Column(db.String(100), unique=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    proceedings = db.relationship('Proceeding', back_populates='case', cascade='all, delete-orphan')
    documents = db.relationship('Document', back_populates='case', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'case_number': self.case_number,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'proceedings_count': len(self.proceedings),
            'documents_count': len(self.documents)
        }