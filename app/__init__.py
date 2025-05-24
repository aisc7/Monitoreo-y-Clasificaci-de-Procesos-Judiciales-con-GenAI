from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # Configuración básica
    app.config['SECRET_KEY'] = 'your-secret-key'

    # Habilitar CORS (para que funcione con el frontend en http://localhost:3000)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

    # Registrar blueprints
    from app.api.routes import judicial_bp
    app.register_blueprint(judicial_bp, url_prefix='/api/judicial')

    @app.route('/health')
    def health_check():
        return {"status": "healthy"}

    return app