
from datetime import datetime
from flask_login import UserMixin
from app.extensions import db

class User(UserMixin,db.Model):

    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    phone=db.Column(db.String(15))
    role=db.Column(db.String(20),nullable=False)
    status=db.Column(db.String(20),default="active")
    created_at=db.Column(db.DateTime,default=datetime.utcnow)

    #realtionships

    assigned_treks=db.relationship(
        "Trek",
        foreign_keys="Trek.staff_id",
        backref="staff",
        lazy=True
    )

    bookings=db.relationship(
        "Booking",
        backref="user",
        lazy=True
    )


class Trek(db.Model):  
        __tablename__="treks"
        id=db.Column(db.Integer,primary_key=True)
        name=db.Column(db.String(100),nullable=False)
        location=db.Column(db.String(100),nullable=False)
        difficulty=db.Column(db.String(20),nullable=False)
        duration=db.Column(db.Integer)
        available_slots=db.Column(db.Integer)
        description=db.Column(db.Text)

        status=db.Column(
            db.Integer,
            default="Upcoming"
        )

        start_date=db.Column(db.Date)

        end_date=db.Column(db.Date)

        staff_id=db.Column(
            db.Integer,
            db.ForeignKey("users.id")
        )

        bookings=db.relationship(
            "Booking",
            backref="trek",
            lazy=True
        )
        description = db.Column(db.Text)

        price = db.Column(db.Float)

        image = db.Column(db.String(255))

        max_altitude = db.Column(db.Integer)

        meeting_point = db.Column(db.String(200))

        
class Booking(db.Model):
      __tablename__="bookings"
      __table_args__ = (
    db.UniqueConstraint(
        "user_id",
        "trek_id",
        name="unique_booking"
    ),
)
      id=db.Column(db.Integer,primary_key=True)

      bookings_date=db.Column(
            db.DateTime,
            default=datetime.utcnow
      )

      status=db.Column(
            db.String(20),
            default="Booked"
      )
      user_id=db.Column(
            db.Integer,
            db.ForeignKey("users.id")
      )

      trek_id=db.Column(
            db.Integer,
            db.ForeignKey("treks.id")
      )
