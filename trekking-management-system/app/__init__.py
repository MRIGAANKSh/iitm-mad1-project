from flask import Flask

from config import Config
from app.extensions import db
from app.extensions import login_manager

def create_app():
    
    app=Flask(__name__,instance_relative_config=True)

    app.config.from_object(Config)
    db.init_app(app)

    login_manager.init_app(app)

    from app.auth.routes import auth_bp

    app.register_blueprint(auth_bp)

    with app.app_context():
        from app import models
        db.create_all()

    return app