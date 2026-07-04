from flask import flash
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask import render_template
from flask_login import current_user

from . import user_bp

from app.extensions import db
from app.models import Trek, Booking
from app.utils.decorators import user_required


@user_bp.route("/book/<int:trek_id>")
@login_required
@user_required
def book_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    # Only open treks
    if trek.status != "Open":

        flash("This trek is not open for booking.", "danger")

        return redirect(url_for("user.view_treks"))

    # Prevent overbooking
    if trek.available_slots <= 0:

        flash("No slots available.", "danger")

        return redirect(url_for("user.view_treks"))

    # Prevent duplicate booking
    existing = Booking.query.filter_by(
        user_id=current_user.id,
        trek_id=trek.id,
        status="Booked"
    ).first()

    if existing:

        flash("You have already booked this trek.", "warning")

        return redirect(url_for("user.view_treks"))

    booking = Booking(
        user_id=current_user.id,
        trek_id=trek.id
    )

    db.session.add(booking)

    trek.available_slots -= 1

    db.session.commit()

    flash("Booking Successful!", "success")

    return redirect(url_for("user.booking_history"))



@user_bp.route("/bookings")
@login_required
@user_required
def booking_history():

    bookings = Booking.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "users/bookings.html",
        bookings=bookings
    )


@user_bp.route("/cancel/<int:booking_id>")
@login_required
@user_required
def cancel_booking(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    if booking.user_id != current_user.id:

        flash("Unauthorized", "danger")

        return redirect(url_for("user.booking_history"))

    if booking.status == "Cancelled":

        flash("Booking already cancelled.", "warning")

        return redirect(url_for("user.booking_history"))

    booking.status = "Cancelled"

    booking.trek.available_slots += 1

    db.session.commit()

    flash("Booking Cancelled Successfully.", "success")

    return redirect(url_for("user.booking_history"))