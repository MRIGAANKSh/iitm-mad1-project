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
from flask_login import login_required



from . import auth_bp

from app.models import User
from app.extensions import db
@auth_bp.route("/")
def home():
    return render_template("index.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form["email"]

        password =request.form["password"]
        user = User.query.filter_by(
            email=email
        ).first()
        if not user:
            flash("Invalid email or password.", "danger")
            return redirect(
                url_for("auth.login")
            )

        if not check_password_hash(
            user.password,
            password
        ):
            flash("Invalid email or password.", "danger")
            return redirect(
                url_for("auth.login")
            )
        if user.status == "blacklisted":
            flash(
                "Account Blacklisted",
                "danger"
            )
            return redirect(
                url_for("auth.login")
            )

        if user.role == "staff" and user.status == "pending":



            flash(
                "Wait for Admin Approval",
                "warning"
            )
            return redirect(
                url_for("auth.login")
            )

        login_user(user)

        flash(
            "Login Successful",
            "success"
        )
        if user.role == "admin":
            return redirect(
                url_for(
                    "admin.dashboard"
                )
            )
        elif user.role == "staff":
            return redirect(
                url_for(
                    "staff.dashboard"
                )
            )

        return redirect(
            url_for(
                "user.dashboard"
            )
        )
    return render_template(
        "auth/login.html"
    )


#login route

@auth_bp.route("/register", methods = ["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]
        role = request.form["role"]
        existing = User.query.filter_by(
            email = email
        ).first()
        if existing:
            flash(
                "Email already exists",
                "danger"
            )
            return redirect(
                url_for("auth.register")
            )
        status = "active"
        if role == "staff":
            status = "pending"
        user = User(
            name = name,
            email = email,
            phone = phone,
            password = generate_password_hash(password),
            role = role,
            status = status
        )
        db.session.add(user)
        db.session.commit()
        flash(
            "Registration Successful",
            "success"

        )
        return redirect(url_for("auth.login"))
    return render_template(

        "auth/register.html"

    )

#logout route
@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()
    flash(
        "Logged Out Successfully",
        "success"
    )
    return redirect(
        url_for("auth.login")
    )