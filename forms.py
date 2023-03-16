#!/usr/bin/env python3
"""
Handles anything to do with forms in the application
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class SpeakOutForm(FlaskForm):
    """
    Form that users will be filling to be reached out to
    """
    first_name = StringField('Your first name', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Your last name', validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = IntegerField('Enter your phone number', validators=[DataRequired()])
    email_address = StringField('Your email address', validators=[DataRequired(), Email()])
    age = IntegerField('Enter your age', validators=[DataRequired()])
    issue_textual = TextAreaField('Tell us about it(30 characters minimum)', validators=[DataRequired(), Length(min=30)])
    submit = SubmitField("Submit")


class AdminSignUp(FlaskForm):
    """
    Responsible for signing the admin up
    """
    prefered_username = StringField('Enter the admin\'s username', validators=[DataRequired(), Length(min=3)])
    email_address = StringField('Enter the admin\'s email address', validators=[DataRequired(), Email()])
    password = PasswordField('Create a password for the admin', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8), EqualTo('password')])
    submit = SubmitField('create admin')

class LoginForm(FlaskForm):
    """
    This form is repsonsible for logging the user into the platform
    """
    email_address = StringField('Enter email address', validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('log in')

class HelpOthersForm(FlaskForm):
    """
    This form is responsible for registering helpers into the platform
    """
    email_address = StringField('Enter email address', validators=[DataRequired(), Email()])
    first_name = StringField('Your first name', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Your last name', validators=[DataRequired(), Length(min=2, max=20)])
    what_they_will_do = TextAreaField('Tell us what you will be doing to help and how exactly you will be doing that(30 characters minimum)', validators=[DataRequired(), Length(min=30)])
    submit = SubmitField("submit")