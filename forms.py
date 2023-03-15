#!/usr/bin/env python3
"""
Handles anything to do with forms in the application
"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
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