"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from WebBlog import app
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from datetime import datetime
from flask_moment import Moment
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(505)
def internal_server_error(e):
    return render_template('505.html'), 505

@app.route('/username/<name>')
def username(name):
    return render_template('username.html', name=name, current_time=datetime.utcnow())

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


@app.route('/redi')
def redi():
    return redirect('http://www.example.com')

@app.route('/req')
def req():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/res')
def res():
    return '<h1>Bad Request</h1>', 400

@app.route('/make_res')
def make_res():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
