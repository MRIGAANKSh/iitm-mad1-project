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

        from app.models import User
        from werkzeug.security import generate_password_hash

        admin=User.query.filter_by(
            email="admin@trek.com"
        ).first()

        if not admin:
            admin=User(
                name="Administrator",
                email="admin@trek.com",
                password=generate_password_hash("admin123"),
                phone="9999999999",
                role="admin",
                status="active",
            )

            db.session.add(admin)
            db.session.commit()

            print("Default Admin Created")



    return app