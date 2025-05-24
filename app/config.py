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