from flask import render_template
from flask import request

from flask_login import login_required

from . import admin_bp

from app.models import User
from app.models import Trek

from app.utils.decorators import admin_required

# to search the bookings or users or treks etc

@admin_bp.route("/search")
@login_required
@admin_required
def search():

    keyword = request.args.get("q", "").strip()

    treks = []
    staff = []
    users = []

    if keyword:

        treks = Trek.query.filter(
            (Trek.name.ilike(f"%{keyword}%")) |
            (Trek.location.ilike(f"%{keyword}%"))
        ).all()

        staff = User.query.filter(
            (User.role == "staff") &
            (
                User.name.ilike(f"%{keyword}%") |
                User.email.ilike(f"%{keyword}%")
            )
        ).all()

        users =User.query.filter(
            (User.role == "user") &
            (
                User.name.ilike(f"%{keyword}%") |
                User.email.ilike(f"%{keyword}%")
            )
        ).all()

    return render_template(
        "admin/search.html",
        keyword=keyword,
        treks=treks,
        staff=staff,
        users=users
    )