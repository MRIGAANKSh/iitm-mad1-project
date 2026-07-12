from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Create all database tables here it create all the tables 
    db.create_all()

    # Create default admin if it doesn't exist, 
    if not User.query.filter_by(email="admin@gmail.com").first():

        admin = User(
            name="Administrator",
            email="admin@gmail.com",
            password=generate_password_hash("admin123"),
            role="admin",
            status="active"
        )

        db.session.add(admin)
        db.session.commit()

        print(" Default admin created.")

    else:
        print("ℹ Admin already exists.")