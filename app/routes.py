"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template


@app.route("/")
def home():
    """Landing page."""
    return 'Web App with Python Flask!'

@app.route('/about')
def about():
    return 'About Python Flask!'