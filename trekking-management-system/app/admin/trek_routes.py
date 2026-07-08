from datetime import datetime

from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from . import admin_bp

from app.extensions import db
from app.models import Trek, User
from app.utils.decorators import admin_required

# trek routes
@admin_bp.route("/treks")
@login_required
@admin_required
def view_treks():

    treks =Trek.query.order_by(Trek.id.desc()).all()

    return render_template(
        "admin/treks.html",
        treks=treks
    )

#trek add route
@admin_bp.route("/treks/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_trek():

    if request.method == "POST":

        trek =Trek(
            name=request.form["name"],
            location=request.form["location"],
            difficulty=request.form["difficulty"],
            duration=int(request.form["duration"]),
            available_slots=int(request.form["slots"]),
            description=request.form["description"],

            start_date=datetime.strptime(
                request.form["start_date"],
                "%Y-%m-%d"
            ).date(),

            end_date=datetime.strptime(
                request.form["end_date"],
                "%Y-%m-%d"
            ).date(),

            status="Open"
        )

        db.session.add(trek)
        db.session.commit()

        flash(
            "Trek Added Successfully",
            "success"
        )

        return redirect(
            url_for("admin.view_treks")
        )

    return render_template(
        "admin/add_trek.html"
    )

#trek edit route
@admin_bp.route("/treks/edit/<int:trek_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    if request.method == "POST":

        trek.name = request.form["name"]
        trek.location = request.form["location"]
        trek.difficulty = request.form["difficulty"]
        trek.duration = int(request.form["duration"])
        trek.available_slots = int(request.form["slots"])
        trek.description = request.form["description"]

        trek.start_date = datetime.strptime(
            request.form["start_date"],
            "%Y-%m-%d"
        ).date()

        trek.end_date = datetime.strptime(
            request.form["end_date"],
            "%Y-%m-%d"
        ).date()

        db.session.commit()

        flash(
            "Trek Updated Successfully",
            "success"
        )

        return redirect(
            url_for("admin.view_treks")
        )

    return render_template(
        "admin/edit_trek.html",
        trek=trek
    )

#trek delete route
@admin_bp.route("/treks/delete/<int:trek_id>")
@login_required
@admin_required
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    db.session.delete(trek)
    db.session.commit()

    flash(
        "Trek Deleted Successfully",
        "success"
    )

    return redirect(
        url_for("admin.view_treks")
    )

#trek assign route

@admin_bp.route("/treks/assign/<int:trek_id>", methods=["GET", "POST"])
@login_required
@admin_required
def assign_staff(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    staff_members = User.query.filter_by(
        role="staff",
        status="active"
    ).all()

    if request.method == "POST":

        staff_id = request.form["staff_id"]

        trek.staff_id = staff_id

        db.session.commit()

        flash(
            "Staff Assigned Successfully",
            "success"
        )

        return redirect(
            url_for("admin.view_treks")
        )

    return render_template(
        "admin/assign_staff.html",
        trek=trek,
        staff_members=staff_members
    )