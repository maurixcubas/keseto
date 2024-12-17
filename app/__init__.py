from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")  # Configuración externa
    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
