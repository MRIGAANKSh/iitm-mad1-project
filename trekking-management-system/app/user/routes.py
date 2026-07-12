from flask import render_template
from flask_login import login_required
from app.utils.decorators import user_required

from . import user_bp

@user_bp.route("/dashboard")
@login_required
@user_required
def dashboard():

    return render_template( "users/dashboard.html" )

