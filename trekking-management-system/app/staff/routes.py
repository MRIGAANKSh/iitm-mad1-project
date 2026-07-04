from flask import render_template
from flask_login import login_required
from app.utils.decorators import staff_required


from . import staff_bp

@staff_bp.route("/dashboard")
@login_required
@staff_required
def dashboard():

    return render_template(
        "staff/dashboard.html"
    )

