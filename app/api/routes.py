from flask import Blueprint, request, jsonify
from app.models import document, case, proceeding

api_bp = Blueprint('api', __name__)

# Document routes
@api_bp.route('/documents', methods=['GET'])
def get_documents():
    return document.get_all_documents()

@api_bp.route('/documents/<int:document_id>', methods=['GET'])
def get_document(document_id):
    return document.get_document(document_id)

@api_bp.route('/documents', methods=['POST'])
def upload_document():
    return document.upload()

@api_bp.route('/documents/<int:document_id>/summary', methods=['GET'])
def get_document_summary(document_id):
    return document.get_summary(document_id)

# Case routes
@api_bp.route('/cases', methods=['GET'])
def get_cases():
    return case.get_all_cases()

@api_bp.route('/cases/<int:case_id>', methods=['GET'])
def get_case(case_id):
    return case.get_case(case_id)

@api_bp.route('/cases', methods=['POST'])
def create_case():
    return case.create()

# Proceeding routes
@api_bp.route('/proceedings', methods=['GET'])
def get_proceedings():
    return proceeding.get_all_proceedings()

@api_bp.route('/proceedings/<int:proceeding_id>', methods=['GET'])
def get_proceeding(proceeding_id):
    return proceeding.get_proceeding(proceeding_id)

@api_bp.route('/proceedings', methods=['POST'])
def create_proceeding():
    return proceeding.create()

@api_bp.route('/proceedings/<int:proceeding_id>/documents', methods=['GET'])
def get_proceeding_documents(proceeding_id):
    return proceeding.get_documents(proceeding_id)