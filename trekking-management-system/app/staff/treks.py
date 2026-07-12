from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required
from flask_login import current_user

from . import staff_bp

from app.models import Trek

from app.extensions import db

from app.utils.decorators import staff_required

#staff trek route
@staff_bp.route("/trek/<int:trek_id>",methods=["GET","POST"])

@login_required
@staff_required
def manage_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)
    if trek.staff_id != current_user.id:

        flash( "Unauthorized", "danger" )

        return redirect( url_for("staff.dashboard")  )

    if request.method=="POST":

        trek.available_slots=int(   request.form["slots"]  )

        trek.status=request.form["status"]

        db.session.commit()
        flash(   "Trek Updated",  "success" )

        return redirect(   url_for("staff.dashboard") )
    
    return render_template(    "staff/manage_trek.html",  trek=trek  )