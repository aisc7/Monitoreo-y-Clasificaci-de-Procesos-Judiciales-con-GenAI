import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # MySQL configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File storage configuration
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

    # AI service configuration
    AI_API_KEY = os.environ.get('AI_API_KEY')
    AI_MODEL = os.environ.get('AI_MODEL') or 'gpt-4'
    JUDICIAL_API_URL = os.environ.get('JUDICIAL_API_URL', 'https://api.ramajudicial.gov.co/consulta')
    JUDICIAL_API_KEY = os.environ.get('JUDICIAL_API_KEY', '')
    JUDICIAL_API_TIMEOUT = int(os.environ.get('JUDICIAL_API_TIMEOUT', '30'))