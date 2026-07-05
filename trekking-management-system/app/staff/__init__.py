from flask import Blueprint

staff_bp = Blueprint(
    "staff",
    __name__,
    url_prefix="/staff"
)

from . import dashboard
from . import treks
from . import participants