from flask import Flask
from flask_migrate import Migrate
from app import create_app, db

# Inicializa la aplicación Flask
app = create_app()

# Inicializa Flask-Migrate
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
