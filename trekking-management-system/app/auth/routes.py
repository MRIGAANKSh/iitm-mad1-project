from . import auth_bp

@auth_bp.route("/")
def home():
    return "<h1>Welcome to Trekking Management System</h1>"

