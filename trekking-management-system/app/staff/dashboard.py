from flask import render_template

from flask_login import login_required
from flask_login import current_user
from . import staff_bp

from app.models import Trek
from app.utils.decorators import staff_required


#dashboard staff route..
# its the dashboard staff route providing the staff routes for its dashbaord.
@staff_bp.route("/dashboard")
@login_required
@staff_required # staff login is required 
def dashboard():
    treks =Trek.query.filter_by(staff_id=current_user.id
    ).all() # if the userid and staff id become equal it shows the treks with those id 

    return render_template( "staff/dashboard.html",  treks=treks
    )