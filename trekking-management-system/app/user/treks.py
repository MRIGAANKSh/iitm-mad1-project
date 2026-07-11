from flask import render_template
from flask import request

from flask_login import login_required

from . import user_bp

from app.models import Trek

from app.utils.decorators import user_required


@user_bp.route("/treks")
@login_required
@user_required
def view_treks():

    difficulty = request.args.get("difficulty", "")
    location = request.args.get("location", "").strip()

    query = Trek.query.filter_by(status="Open")

    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    if location:
        query = query.filter(
            Trek.location.ilike(f"%{location}%")
        )

    treks = query.all()

    return render_template(
        "users/trek.html",
        treks=treks,
        difficulty=difficulty,
        location=location
    )


@user_bp.route("/treks/<int:trek_id>")
@login_required
@user_required
def trek_details(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    return render_template(
        "users/trek_details.html",
        trek=trek
    )