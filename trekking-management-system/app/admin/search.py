from flask import render_template
from flask import request

from flask_login import login_required

from . import admin_bp

from app.models import User, Trek
from app.utils.decorators import admin_required


@admin_bp.route("/search")
@login_required
@admin_required
def search():

    keyword = request.args.get("q", "").strip()
    search_type = request.args.get("type", "all")

    treks = []
    staff = []
    users = []

    if keyword:

        if search_type in ["all", "trek"]:

            treks = Trek.query.filter(
                (Trek.name.ilike(f"%{keyword}%")) |
                (Trek.location.ilike(f"%{keyword}%"))
            ).all()

        if search_type in ["all", "staff"]:

            staff = User.query.filter(
                (User.role == "staff") &
                (
                    User.name.ilike(f"%{keyword}%") |
                    User.email.ilike(f"%{keyword}%")
                )
            ).all()

        if search_type in ["all", "user"]:

            users = User.query.filter(
                (User.role == "user") &
                (
                    User.name.ilike(f"%{keyword}%") |
                    User.email.ilike(f"%{keyword}%")
                )
            ).all()

    return render_template(
        "admin/search.html",
        keyword=keyword,
        search_type=search_type,
        treks=treks,
        staff=staff,
        users=users
    )