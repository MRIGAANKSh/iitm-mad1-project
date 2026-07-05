from flask import Blueprint

user_bp = Blueprint(
    "user",
    __name__,
    url_prefix="/user"
)

from . import dashboard
from . import treks
from . import bookings
from . import profile

from . import profile