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

# trek routes for getting the treks data... 
@admin_bp.route("/treks")


@login_required # login required which require a login to fetch the data 
@admin_required # admin required which require a admin only funtionality to fetch the data.
def view_treks():

    treks =Trek.query.order_by(Trek.id.desc()).all()

    return render_template("admin/treks.html",treks=treks
    )

#trek add route .. this route allows the admin to add the treks ...
@admin_bp.route("/treks/add", methods=["GET", "POST"])

@login_required
@admin_required # its a admin only functionality which is the admin only can creagte a trek ,
def add_trek():

    if request.method == "POST":

        trek =Trek(
            name=request.form["name"],
            location=request.form["location"],
            difficulty=request.form["difficulty"],
            duration=int(request.form["duration"]),
            available_slots=int(request.form["slots"]),
            description=request.form["description"],

            start_date=datetime.strptime(request.form["start_date"],"%Y-%m-%d"
            ).date(), # start date it provide to select the start date for the trek ie start date from which the trek will be started.

            end_date=datetime.strptime(request.form["end_date"],"%Y-%m-%d"
            ).date(), # end date of the trek 

            status="Open"
        )

        db.session.add(trek)
        db.session.commit()

        flash(
            "Trek Aded Successfully","sucess")

        return redirect(url_for("admin.view_treks")
        )

    return render_template("admin/add_trek.html"
    )

#trek edit route this provide the edit route for the trek like editing the trek detail by the admin..
@admin_bp.route("/treks/edit/<int:trek_id>", methods=["GET", "POST"])


@login_required
@admin_required # its the admin only route ie only the admin can acess this route.


def edit_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    if request.method == "POST":

        trek.name = request.form["name"]
        trek.location = request.form["location"]
        trek.difficulty = request.form["difficulty"]
        trek.duration = int(request.form["duration"])
        trek.available_slots = int(request.form["slots"])
        trek.description = request.form["description"]

        trek.start_date = datetime.strptime(request.form["start_date"],"%Y-%m-%d"
        ).date()

        trek.end_date = datetime.strptime(  request.form["end_date"], "%Y-%m-%d"
        ).date()

        db.session.commit()

        flash(  "Trek Updated Successfully","success"
        )

        return redirect(url_for  ("admin.view_treks"))

    return render_template( "admin/edit_trek.html",trek=trek
    )

#trek delete route.. it delete the trek as per the id of the trek ohk ...
@admin_bp.route("/treks/delete/<int:trek_id>")


@login_required
@admin_required # admin required ie its also a admin only route 
def delete_trek(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    db.session.delete(trek)
    db.session.commit()

    flash("Trek Deleted Successfully","success")

    return redirect(
        url_for("admin.view_treks")
    )

#trek assign route --- assign the trek to a particular staff ohk

@admin_bp.route("/treks/assign/<int:trek_id>", methods=["GET", "POST"])
@login_required
@admin_required
def assign_staff(trek_id):

    trek = Trek.query.get_or_404(trek_id)

    staff_members = User.query.filter_by(  role="staff",   status="active"
    ).all()

    if request.method == "POST":

        staff_id = request.form["staff_id"]

        trek.staff_id = staff_id
        db.session.commit()

        flash("Staff Assigned Successfully","success")

        return redirect(url_for("admin.view_treks"))

    return render_template("admin/assign_staff.html",
        trek=trek,
        staff_members=staff_members
    )