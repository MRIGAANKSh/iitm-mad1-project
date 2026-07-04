from functools import wraps

from flask import flash
from flask import redirect
from flask import url_for

from flask_login import current_user


def admin_required(f):

    @wraps(f)

    def decorated_function(*args, **kwargs):

        if current_user.role != "admin":

            flash(
                "Access Denied",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        return f(*args, **kwargs)

    return decorated_function


def staff_required(f):

    @wraps(f)

    def decorated_function(*args, **kwargs):

        if current_user.role != "staff":

            flash(
                "Access Denied",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        return f(*args, **kwargs)

    return decorated_function


def user_required(f):

    @wraps(f)

    def decorated_function(*args, **kwargs):

        if current_user.role != "user":

            flash(
                "Access Denied",
                "danger"
            )

            return redirect(
                url_for("auth.login")
            )

        return f(*args, **kwargs)

    return decorated_function