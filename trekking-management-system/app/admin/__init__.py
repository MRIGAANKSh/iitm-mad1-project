from flask import Blueprint
admin_bp=Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

from . import routes
from . import trek_routes
from . import staff
from . import users
from . import search
from . import bookings