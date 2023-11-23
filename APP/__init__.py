from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    from .models import Base

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    #Register Blueprints here
    from APP.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    return app 

create_app()

