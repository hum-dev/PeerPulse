#!/usr/bin/env python3
"""
entry point for this application
"""

from flask import Flask, render_template, redirect, url_for
from forms import SpeakOutForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fe7f90a588d99805a3764b5709e8ddefe862f04e'

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success_submission():
    return render_template('success_submission.html')

@app.route('/talk-to-us', methods=["GET", "POST"])
def talk_to_us():
    form = SpeakOutForm()
    if form.validate_on_submit:
        return redirect(url_for('success_submission'))
        # pass
    return render_template('talk_to_us.html', title="PeerPulse. - talk to us", form=form), 200

if __name__ == "__main__":
    app.run(debug=True)