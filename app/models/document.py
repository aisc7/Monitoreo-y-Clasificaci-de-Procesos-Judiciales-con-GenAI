from app import db
from datetime import datetime

class Document(db.Model):
    __tablename__ = 'documents'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(255), nullable=False)
    doc_type = db.Column(db.String(50), nullable=False)  # pdf, csv, etc.
    summary = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Foreign keys
    proceeding_id = db.Column(db.Integer, db.ForeignKey('proceedings.id'), nullable=False)
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=False)
    
    # Relationships
    proceeding = db.relationship('Proceeding', back_populates='documents')
    case = db.relationship('Case', back_populates='documents')
    
    def to_dict(self):
        return {
            'id': self.id,
            'filename': self.filename,
            'doc_type': self.doc_type,
            'summary': self.summary,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'proceeding_id': self.proceeding_id,
            'case_id': self.case_id
        }