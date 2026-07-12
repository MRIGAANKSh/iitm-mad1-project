from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from . import admin_bp

from app.models import User
from app.extensions import db
from app.utils.decorators import admin_required

# staff route for admin

@admin_bp.route("/staff")

# it require a login
@login_required
@admin_required # admin only route it is  ie it can only accessed by admin
def manage_staff():

    staff = User.query.filter_by(role="staff").all()

    return render_template("admin/staff.html",   staff=staff)


# route for staff approval by admin , providing the staff approval functionality to the user
@admin_bp.route("/staff/approve/<int:user_id>")

@login_required
@admin_required # it is also a admin route...
def approve_staff(user_id):

    staff = User.query.filter_by(id=user_id,role="staff" ).first_or_404()

    staff.status = "active"
    db.session.commit()

    flash("Staff Approved Successfully","success"  )

    return redirect(url_for("admin.manage_staff"))



# for blacklist route.. to show the blacklist staff
@admin_bp.route("/staff/blacklist/<int:user_id>")
@login_required
@admin_required
def blacklist_staff(user_id):

    staff = User.query.filter_by(  id=user_id, role="staff"  ).first_or_404()

    staff.status ="blacklisted"

    db.session.commit()

    flash("Staff Blacklisted",  "warning")

    return redirect( url_for("admin.manage_staff"))

# route for reactivating the blacklist staff by the addin
@admin_bp.route("/staff/reactivate/<int:user_id>")

@login_required
@admin_required
def reactivate_staff(user_id):

    staff = User.query.filter_by( id=user_id,  role="staff" ).first_or_404()

    staff.status ="active"
    db.session.commit()

    flash("Staff Reactivated", "success")

    return redirect(url_for("admin.manage_staff"))