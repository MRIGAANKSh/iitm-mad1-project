from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from . import admin_bp

from app.models import User
from app.extensions import db
from app.utils.decorators import admin_required



@admin_bp.route("/staff")

@login_required
@admin_required
def manage_staff():

    staff = User.query.filter_by(
        role="staff"
    ).all()

    return render_template(
        "admin/staff.html",
        staff=staff
    )



@admin_bp.route("/staff/approve/<int:user_id>")

@login_required
@admin_required
def approve_staff(user_id):

    staff = User.query.filter_by(
    id=user_id,
    role="staff"
).first_or_404()

    staff.status = "active"

    db.session.commit()

    flash(
        "Staff Approved Successfully",
        "success"
    )

    return redirect(
        url_for("admin.manage_staff")
    )




@admin_bp.route("/staff/blacklist/<int:user_id>")
@login_required
@admin_required
def blacklist_staff(user_id):

    staff = User.query.filter_by(
        id=user_id,
        role="staff"
    ).first_or_404()

    staff.status = "blacklisted"

    db.session.commit()

    flash(
        "Staff Blacklisted",
        "warning"
    )

    return redirect(
        url_for("admin.manage_staff")
    )


@admin_bp.route("/staff/reactivate/<int:user_id>")

@login_required
@admin_required
def reactivate_staff(user_id):

    staff = User.query.filter_by(
    id=user_id,
    role="staff"
).first_or_404()

    staff.status = "active"

    db.session.commit()

    flash(
        "Staff Reactivated",
        "success"
    )

    return redirect(
        url_for("admin.manage_staff")
    )