# Trekking Management System

## Project Overview

The Trekking Management System is a Flask-based web application developed to simplify the management of trekking events. It supports three different roles:

* Admin
* Trek Staff
* Trekker (User)

The system allows administrators to manage treks and staff, trek staff to manage assigned treks, and users to browse and book trekking events.

---

## Technologies Used

* Python 3.x
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* Jinja2
* Bootstrap 5
* HTML
* CSS

---

## Features

### Admin

* Login
* Dashboard
* Add/Edit/Delete Treks
* Approve Staff
* Blacklist Users and Staff
* Assign Staff to Treks
* View All Bookings
* Search Users, Staff and Treks

### Trek Staff

* Registration
* Login
* View Assigned Treks
* Update Trek Status
* Update Available Slots
* View Trek Participants

### Trekker

* Registration
* Login
* Browse Treks
* Search Treks
* Book Trek
* View Booking History
* Edit Profile

---

## Database

SQLite is used as the backend database.

The database is created programmatically using SQLAlchemy models.

No manual database creation is required.

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd Trekking-Management-System
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv myvenv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

```bash
python create_db.py
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Default Admin Credentials

Email

```
admin@gmail.com
```

Password

```
admin123
```

---

## Project Structure

```
app/
    admin/
    auth/
    staff/
    user/
    static/
    templates/
    models.py
    extensions.py

instance/
    app.db

app.py
config.py
create_db.py
requirements.txt
README.md
```

---

## Future Enhancements

* Trek Images
* Trek Reviews
* Email Notifications
* Weather API Integration
* REST APIs
* Analytics Dashboard

---

## Author

MRIGAANK SHARMA
