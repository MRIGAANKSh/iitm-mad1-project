from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from . import staff_bp

from app.extensions import db
from app.models import Trek
from app.models import Booking

from app.utils.decorators import staff_required

# staff route for viewing the participants... 

@staff_bp.route("/participants/<int:trek_id>")

@login_required

@staff_required # staff route is required ohk 

def participants(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    # conditions if the  trek id not equal to the current user id then flash unauthorised.

    if trek.staff_id != current_user.id:

        flash(  "Unauthorized",  "danger"   ) # flash msgs

        return redirect(   url_for("staff.dashboard") )

    bookings = trek.bookings


    # return the template or redner the page.... 
    return render_template( "staff/participants.html", trek=trek, bookings=bookings  )


# complete bookig rout of the staff ....

@staff_bp.route("/booking/<int:booking_id>/complete")

@login_required

@staff_required # staff required only route
def complete_booking(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    if booking.trek.staff_id != current_user.id:

        flash(   "Unauthorized","danger" ) # unauthorised 

        return redirect(  url_for("staff.dashboard")   )

    booking.status = "Completed"

    db.session.commit()

    flash( "Participant marked as completed.", "success"  )

    return redirect( url_for(  "staff.participants",   trek_id=booking.trek_id)   )

# cancel booking route for the staff.... of the participants or the user..

@staff_bp.route("/booking/<int:booking_id>/cancel")
@login_required # login required 
@staff_required # staff required 
def cancel_booking(booking_id):

    booking = Booking.query.get_or_404(booking_id)

    if booking.trek.staff_id != current_user.id:

        flash( "Unauthorized", "danger"  )

        return redirect(  url_for("staff.dashboard")  )

    booking.status = "Cancelled"

    booking.trek.available_slots += 1

    db.session.commit()

    flash(   "Booking cancelled successfully.", "warning" )

    return redirect( url_for( "staff.participants",  trek_id=booking.trek_id  ) )