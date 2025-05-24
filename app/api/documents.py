from flask import request, jsonify, current_app
from app import db
from app.models.document import Document
from app.services.summary_generator import generate_summary
from app.services.storage_service import save_document_file
import os

def get_all_documents():
    # Get query parameters for filtering
    case_id = request.args.get('case_id', type=int)
    proceeding_id = request.args.get('proceeding_id', type=int)
    
    query = Document.query
    
    if case_id:
        query = query.filter_by(case_id=case_id)
    
    if proceeding_id:
        query = query.filter_by(proceeding_id=proceeding_id)
    
    documents = query.all()
    return jsonify({
        'documents': [doc.to_dict() for doc in documents]
    })

def get_document(document_id):
    document = Document.query.get_or_404(document_id)
    return jsonify(document.to_dict())

def upload():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Get associated proceeding and case IDs
    proceeding_id = request.form.get('proceeding_id', type=int)
    case_id = request.form.get('case_id', type=int)
    
    if not proceeding_id or not case_id:
        return jsonify({'error': 'Missing case_id or proceeding_id'}), 400
    
    # Save the file
    file_path = save_document_file(file)
    
    # Process document content
    content, doc_type = process_document(file_path)
    
    # Generate summary with AI
    summary = generate_summary(content)
    
    # Create database record
    document = Document(
        filename=file.filename,
        file_path=file_path,
        doc_type=doc_type,
        summary=summary,
        proceeding_id=proceeding_id,
        case_id=case_id
    )
    
    db.session.add(document)
    db.session.commit()
    
    return jsonify(document.to_dict()), 201

def get_summary(document_id):
    document = Document.query.get_or_404(document_id)
    
    # Return existing summary if available
    if document.summary:
        return jsonify({'summary': document.summary})
    
    # Generate summary if not already available
    content, _ = process_document(document.file_path)
    summary = generate_summary(content)
    
    # Update document with new summary
    document.summary = summary
    db.session.commit()
    
    return jsonify({'summary': summary})