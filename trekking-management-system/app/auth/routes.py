from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user



from . import auth_bp

from app.models import User
from app.extensions import db

@auth_bp.route("/")
def home():
    return redirect(url_for("auth.login"))

@auth_bp.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bp.route("/register")
def register():
    return render_template("auth/register.html")
