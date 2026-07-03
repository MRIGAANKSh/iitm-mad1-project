from flask import render_template
from flask_login import login_required

from . import user_bp

@user_bp.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "users/dashboard.html"
    )

