from flask import render_template
from flask_login import login_required
from . import admin_bp
from app.models import User, Trek, Booking
from app.utils.decorators import admin_required


# admin dashboard routes.

#this is the dashboard route for admins , this route provide the dashboaerd details to the admin.

@admin_bp.route("/dashboard")
@login_required
@admin_required # admin login required is neccessary 
def dashboard():

    # total treks ,users ,staffs..
    total_treks = Trek.query.count()
    total_users =User.query.filter_by(
        role="user").count()


    total_staff =User.query.filter_by(
        role="staff"
    ).count()
 
    # total bookings using booking query 
    total_bookings =Booking.query.count()
    recent_bookings =Booking.query.order_by( Booking.bookings_date.desc())   .limit(5).all()
    

    recent_users = User.query.filter_by( role="user" ).order_by( User.id.desc() # in desc order
).limit(5).all()
    
    
    recent_treks =Trek.query.order_by(Trek.id.desc()).limit(5).all() # only 5 it shows 


    # pending staff through checking the pending status
    pending_staff =User.query.filter_by( role="staff",status="pending").count()
    
    
    completed_treks = Trek.query.filter_by( status="Completed").count()

    open_treks = Trek.query.filter_by( status="Open").count()

    
    cancelled_bookings = Booking.query.filter_by(status="Cancelled" ).count()
    
    
    # assinging the values to the rendertemplate for the flask app
    return render_template(
        "admin/dashboard.html",
        total_treks=total_treks,
        total_users=total_users,
        total_staff=total_staff,
        total_bookings=total_bookings,
    recent_bookings=recent_bookings,
        recent_users=recent_users,
        recent_treks=recent_treks
    )



