from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['REDIS_URL'] = os.getenv('REDIS_URL')
    app.config['UNIVERSAL_HMAC_KEY'] = os.getenv('UNIVERSAL_HMAC_KEY')
    app.config['GOOGLE_CLIENT_ID'] = os.getenv('GOOGLE_CLIENT_ID')
    app.config['GOOGLE_CLIENT_SECRET'] = os.getenv('GOOGLE_CLIENT_SECRET')
    app.config['FRONTEND_URL'] = os.getenv('FRONTEND_URL')
    
    # Import blueprints from routes
    from .routes import kv_bp
    from .routes import read_bp
    #from .routes import use_kv_bp
    from .routes import get_token_bp
    # Register blueprints
    app.register_blueprint(kv_bp, url_prefix="/encryption")
    app.register_blueprint(read_bp, url_prefix="/decryption")
    #app.register_blueprint(use_kv_bp, url_prefix="/use")
    app.register_blueprint(get_token_bp, url_prefix="/dev")
    return app
   