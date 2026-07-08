from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from . import admin_bp

from app.models import User
from app.extensions import db
from app.utils.decorators import admin_required


#users route

@admin_bp.route("/users")
@login_required
@admin_required
def manage_users():

    users = User.query.filter_by(
        role="user"
    ).all()

    return render_template(
        "admin/users.html",
        users=users
    )

#users blacklist route
@admin_bp.route("/users/blacklist/<int:user_id>")
@login_required
@admin_required
def blacklist_user(user_id):

    user = User.query.filter_by(
        id=user_id,
        role="user"
    ).first_or_404()

    user.status = "blacklisted"

    db.session.commit()

    flash(
        "User Blacklisted",
        "warning"
    )

    return redirect(
        url_for("admin.manage_users")
    )

#users activate route

@admin_bp.route("/users/activate/<int:user_id>")
@login_required
@admin_required
def activate_user(user_id):

    user = User.query.filter_by(
        id=user_id,
        role="user"
    ).first_or_404()

    user.status = "active"

    db.session.commit()

    flash(
        "User Activated",
        "success"
    )

    return redirect(
        url_for("admin.manage_users")
    )

#users seach route
@admin_bp.route("/users/search")
@login_required
@admin_required
def search_users():

    keyword = request.args.get("q", "").strip()

    users = User.query.filter(
        User.role == "user",
        (
            User.name.ilike(f"%{keyword}%")
        ) | (
            User.email.ilike(f"%{keyword}%")
        )
    ).all()

    return render_template(
        "admin/users.html",
        users=users
    )