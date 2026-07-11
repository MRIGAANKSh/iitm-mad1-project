from flask import render_template

from flask_login import login_required
from flask_login import current_user

from . import user_bp

from app.models import Trek
from app.models import Booking

from app.utils.decorators import user_required


@user_bp.route("/dashboard")
@login_required
@user_required
def dashboard():

    # Total available treks
    available_treks = Trek.query.filter_by(
        status="Open"
    ).count()

    # User statistics
    booked_treks = Booking.query.filter_by(
        user_id=current_user.id,
        status="Booked"
    ).count()

    completed_treks = Booking.query.filter_by(
        user_id=current_user.id,
        status="Completed"
    ).count()

    cancelled_treks = Booking.query.filter_by(
        user_id=current_user.id,
        status="Cancelled"
    ).count()

    # Booking history
    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Booking.bookings_date.desc()
    ).all()

    return render_template(
        "users/dashboard.html",
        available_treks=available_treks,
        booked_treks=booked_treks,
        completed_treks=completed_treks,
        cancelled_treks=cancelled_treks,
        bookings=bookings
    )