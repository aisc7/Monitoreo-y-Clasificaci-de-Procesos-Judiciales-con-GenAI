import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app

def save_document_file(file):
    """
    Save an uploaded file with a secure unique name
    
    Args:
        file: FileStorage object from request.files
    
    Returns:
        str: Path where the file is stored
    """
    # Generate a unique filename to avoid collisions
    filename = secure_filename(file.filename)
    unique_id = str(uuid.uuid4())
    unique_filename = f"{unique_id}_{filename}"
    
    # Create upload directory if it doesn't exist
    upload_dir = os.path.join(current_app.config['UPLOAD_FOLDER'])
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save the file
    file_path = os.path.join(upload_dir, unique_filename)
    file.save(file_path)
    
    return file_path