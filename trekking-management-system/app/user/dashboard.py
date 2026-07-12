from flask import render_template

from flask_login import login_required
from flask_login import current_user

from . import user_bp

from app.models import Trek
from app.models import Booking

from app.utils.decorators import user_required

# dashboard route... for the user dashboard 
@user_bp.route("/dashboard")
@login_required
@user_required
def dashboard():

    # it shows the total availanle treks , those status is open 
    available_treks = Trek.query.filter_by( status="Open" ).count()

    # it shows the booked treks of the user from the booking table by filtering through the user id .
    booked_treks = Booking.query.filter_by( user_id=current_user.id, status="Booked" ).count()

    # completed treks through the status is completed.
    completed_treks = Booking.query.filter_by( user_id=current_user.id, status="Completed" ).count()


    # cancelled treks .. status is cancelled...
    cancelled_treks = Booking.query.filter_by(  user_id=current_user.id,  status="Cancelled" ).count()

    # bookings... it shwos the bookings 
    bookings = Booking.query.filter_by( user_id=current_user.id).order_by(  Booking.bookings_date.desc() ).all()


    # render tempplate and pass the values to the html page...
    return render_template(
        "users/dashboard.html",
        available_treks=available_treks,
        booked_treks=booked_treks,
        completed_treks=completed_treks,
        cancelled_treks=cancelled_treks,
        bookings=bookings
    )