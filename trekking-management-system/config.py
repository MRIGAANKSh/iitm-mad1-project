import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY="MAD1"

    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"instance","trek.db")

    SQLALCHEMY_TRACK_MODIFICATIONS=False
