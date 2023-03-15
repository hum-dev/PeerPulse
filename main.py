#!/usr/bin/env python3
"""
entry point for this application
"""

from datetime import datetime
from uuid import uuid4
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import SpeakOutForm, AdminSignUp, LoginForm
from flask_login import LoginManager,UserMixin
from flask_login import login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fe7f90a588d99805a3764b5709e8ddefe862f04e'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///peer_pulse.db"

db = SQLAlchemy(app=app)
login_manager = LoginManager(app)
# login_manager.login_view = 'login_admin'

@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(int(user_id))


class HelpSeeker(db.Model):
    """
    Table for those seeking help
    """
    __tablename__ = "Help_seekers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    issue_textual = db.Column(db.String, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    random_user_id = db.Column(db.String, default=str(uuid4()))

    def __repr__(self):
        """
        Represents the user object as a beatiful string
        """
        return "u/{}.{}".format(self.first_name, self.email_address)

class Admins(db.Model, UserMixin):
    """
    Table for those seeking help
    """
    __tablename__ = "administrators"
    id = db.Column(db.Integer, primary_key=True)
    prefered_username = db.Column(db.String, nullable=False)
    email_address = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/success', methods=["GET", "POST"])
def success_submission():
    return render_template('success_submission_t.html')

@app.route('/talk-to-us', methods=["GET", "POST"])
def talk_to_us():
    form = SpeakOutForm()
    if form.validate_on_submit():
        user_to_create = HelpSeeker(first_name=form.first_name.data, last_name=form.last_name.data, phone_number=form.phone_number.data, email_address=form.email_address.data, age=form.age.data, issue_textual = form.issue_textual.data)
        print(user_to_create)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('success_submission'))
        # pass
    return render_template('talk_to_us.html', title="PeerPulse. - talk to us", form=form), 200

@app.route('/all-submissions', methods=["GET", "POST"])
@login_required
def all_submissions():
    all_issues = HelpSeeker.query.order_by(HelpSeeker.date_posted.desc()).all()
    return render_template('all_submissions.html', all_issues=all_issues), 200

@app.route('/admin-login', methods=["GET", "POST"])
def login_admin():
    form = LoginForm()
    if form.validate_on_submit():
        email_address = form.email_address.data
        password = form.password.data
        user_logging_in = Admins.query.filter_by(email_address=email_address).first()
        if user_logging_in and user_logging_in.password == password:
            login_user(user_logging_in)
            return redirect(url_for('all_submissions'))
    return render_template('login.html', title="PerPulse - login to your account", form=form), 200

@app.route('/create-admin', methods=["GET", "POST"])
def create_admin():
    """
    Responsible for creating an admin
    """
    form = AdminSignUp()
    if form.validate_on_submit():
        admin_to_create = Admins(prefered_username=form.prefered_username.data, email_address=form.email_address.data, password = form.password.data)
        db.session.add(admin_to_create)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_admin.html', title="PeerPulse - Create and admin", form=form), 200

if __name__ == "__main__":
    app.run(debug=True)