from app import db
from datetime import datetime

class Proceeding(db.Model):
    __tablename__ = 'proceedings'

    id = db.Column(db.Integer, primary_key=True)
    proceeding_number = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign key
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=False)
    
    # Relationships
    case = db.relationship('Case', back_populates='proceedings')
    documents = db.relationship('Document', back_populates='proceeding', cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'proceeding_number': self.proceeding_number,
            'title': self.title,
            'description': self.description,
            'date': self.date.isoformat(),
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'case_id': self.case_id,
            'documents_count': len(self.documents)
        }