from flask import render_template
from flask_login import login_required
from flask_login import current_user

from . import user_bp
from app.models import Trek
from app.utils.decorators import user_required


@user_bp.route("/dashboard")
@login_required
@user_required
def dashboard():

    available_treks = Trek.query.filter_by(
        status="Open"
    ).count()

    return render_template(
        "users/dashboard.html",
        available_treks=available_treks
    )