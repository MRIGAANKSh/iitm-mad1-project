from flask import render_template
from flask_login import login_required

from . import admin_bp
from app.models import User, Trek, Booking
from app.utils.decorators import admin_required


@admin_bp.route("/dashboard")
@login_required
@admin_required
def dashboard():

    total_treks = Trek.query.count()

    total_users = User.query.filter_by(
        role="user"
    ).count()

    total_staff = User.query.filter_by(
        role="staff"
    ).count()

    total_bookings = Booking.query.count()

    recent_users = User.query.filter_by(
        role="user"
    ).order_by(
        User.id.desc()
    ).limit(5).all()

    recent_treks = Trek.query.order_by(
        Trek.id.desc()
    ).limit(5).all()

    return render_template(
        "admin/dashboard.html",
        total_treks=total_treks,
        total_users=total_users,
        total_staff=total_staff,
        total_bookings=total_bookings,
        recent_users=recent_users,
        recent_treks=recent_treks
    )