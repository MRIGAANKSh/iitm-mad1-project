from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for

from flask_login import login_required
from flask_login import current_user

from . import staff_bp

from app.models import Trek

from app.utils.decorators import staff_required


#participants in the trek...

@staff_bp.route("/participants/<int:trek_id>")
@login_required
@staff_required
def participants(trek_id):

    trek = Trek.query.get_or_404(trek_id)
    if trek.staff_id != current_user.id:
        flash(
            "Unauthorized",
            "danger"
        )
        return redirect(
            url_for("staff.dashboard")
        )

    bookings =trek.bookings

    return render_template(
        "staff/participants.html",
        trek=trek,
        bookings=bookings
    )