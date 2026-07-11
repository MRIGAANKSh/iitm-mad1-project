from flask import render_template
from flask import request
from flask_login import login_required
from . import admin_bp
from app.models import Booking
from app.utils.decorators import admin_required


@admin_bp.route("/bookings")
@login_required
@admin_required

# this function view the bookings to the admins.
def view_bookings():
    status =request.args.get("status")


    query =Booking.query
    if status:
        query = query.filter_by(status=status)

    bookings = query.order_by(  Booking.bookings_date.desc()
                              
    ).all()



    return render_template("admin/bookings.html",
        bookings=bookings,
        selected_status=status
    )