from flask import Flask
from config import Config
from app.extensions import db, login_manager

def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from app.auth import auth_bp
    from app.admin import admin_bp
    from app.staff import staff_bp
    from app.user import user_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(user_bp)

    return app