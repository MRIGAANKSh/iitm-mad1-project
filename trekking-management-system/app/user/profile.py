from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from . import user_bp

from app.extensions import db
from app.utils.decorators import user_required


# profile route of the user 
# shows the profile data of the user and allows to change the usewr data as per the need
 

@user_bp.route("/profile", methods=["GET", "POST"])
@login_required
@user_required #user required....
def profile():

    if request.method == "POST":

        current_user.name = request.form["name"]
        current_user.email = request.form["email"]
        current_user.phone = request.form["phone"]

        db.session.commit()

        flash("Profile Updated Successfully", "success")

        return redirect(url_for("user.profile"))

    return render_template(   "users/profile.html" )


# modules for password hashing and storing in the db 
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash



# change password route allowing the user to change the password for the user,.

@user_bp.route("/change-password", methods=["GET", "POST"])
@login_required
@user_required # user required...
def change_password():

    if request.method == "POST":

        old_password = request.form["old_password"] #old pw
        new_password = request.form["new_password"]# new pw

        if not check_password_hash(current_user.password, old_password):
            flash("Current password is incorrect.", "danger")
            return redirect(url_for("user.change_password"))

        current_user.password = generate_password_hash(new_password)

        db.session.commit()

        flash("Password changed successfully.", "success")
        return redirect(url_for("user.profile"))

    return render_template("users/change_password.html")